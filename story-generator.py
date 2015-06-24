from os import listdir
from os.path import isfile, join
import sys

images_directory = './images/'
drafts_directory = './_drafts/'

# Steps to generating a story:
# Create a folder with all your images
# The name of this folder will be the name of your story
# run 'python story-generator.py STORY_NAME'
# This will generate your story in the appr

if len(sys.argv) == 1:
    sys.exit('Please provide an image directory')
else:
	story_name = sys.argv[1]
	directory = images_directory + story_name

print '    Using folder: ', str(directory)

files = [ f for f in listdir(directory) if isfile(join(directory,f)) ]


if '.DS_Store' in files: files.remove('.DS_Store')

# files.remove('.DS_Store')

# print files

generatedStoryFile = open((drafts_directory + story_name + '.markdown'),'wb')
generatedStoryFile.write('---\n')
generatedStoryFile.write('layout: story\n')
generatedStoryFile.write('slug: "' + story_name + '"\n')
generatedStoryFile.write('title:  ""\n')
generatedStoryFile.write('description: ""\n')
generatedStoryFile.write('permalink: /stories/' + story_name + '/\n')
generatedStoryFile.write('storynumber: \n')
generatedStoryFile.write('---\n')

for file in files:
    generatedStoryFile.write('![](/images/{{page.slug}}/')
    generatedStoryFile.write(file)
    generatedStoryFile.write(')\n\n')

generatedStoryFile.close()

print '    Story generated at: ' + drafts_directory + story_name + '.markdown'
