(function (){
    $('#mobile-dropdown').click(function(){
        $('.site-nav').slideToggle();
    });

    // CHECK TO SEE IF THERE IS A BACK TO TOP BUTTON
    if($('#back-to-top').length){
        // browser window scroll (in pixels) after which the "back to top" link is shown
        var offset = 600,

        //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        // offset_opacity = 1200,

        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,

        //grab the "back to top" link
        $backToTop = $('#back-to-top');

        // hide or show the "back to top" link
        $(window).scroll(function(){
            // ( $(this).scrollTop() > offset ) ? $back-to-top.addClass('animated fadeIn') : $back-to-top.removeClass('animated fadeOut');
            // if( $(this).scrollTop() > offset_opacity ) {
            // 	$back-to-top.addClass('animated fadeOut');
            // }
            if( $(this).scrollTop() > offset ) {
                $backToTop.css('display', 'block')
                $backToTop.removeClass('fadeOutRight');
                $backToTop.addClass('fadeInRight');

            }
            else{
                $backToTop.removeClass('fadeInRight');
                $backToTop.addClass('fadeOutRight');
            }
        });

        //smooth scroll to top
        $backToTop.on('click', function(event){
            // event.preventDefault();
            $('body,html').animate({
                scrollTop: 0 ,
                 }, scroll_top_duration
            );
        });
    }
})();
