from os import listdir
from os.path import isfile, join
import sys

print 'Using folder: ', str(sys.argv[1])

print 'Using folder: ', str(directory)

if len(sys.argv) == 0:
    directory = './';

files = [ f for f in listdir(directory) if isfile(join(directory,f)) ]

files.remove('.DS_Store')

# print files

generatedStoryFile = open('generatedStoryFile.markdown','wb')
generatedStoryFile.write('---\n')
generatedStoryFile.write('layout: story\n')
generatedStoryFile.write('slug: "trinity-two"\n')
generatedStoryFile.write('title:  "Life in the Burnzone"\n')
generatedStoryFile.write('description: "The second trip to Trinity"\n')
generatedStoryFile.write('permalink: /stories/trinity-two/\n')
generatedStoryFile.write('storynumber: 55\n')
generatedStoryFile.write('---\n')

for file in files:
    generatedStoryFile.write('![](/images/{{page.slug}}/')
    generatedStoryFile.write(file)
    generatedStoryFile.write(')\n\n')

generatedStoryFile.close()
