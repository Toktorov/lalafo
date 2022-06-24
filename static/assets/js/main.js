(function ($) {
    "use strict";


    /*--
		Header Sticky
    -----------------------------------*/
    $(window).on('scroll', function(event) {    
        var scroll = $(window).scrollTop();
        if (scroll < 350) {
            $(".header-sticky").removeClass("sticky");
        } else{
            $(".header-sticky").addClass("sticky");
        }
    });
    

    /*--
        Off Canvas Menu
	-----------------------------------*/
	
	$('.mobile-menu-open').on('click', function(){
        $('.off-canvas-box').addClass('open')
        $('.menu-overlay').addClass('open')
    });
    
    $('.menu-close').on('click', function(){
        $('.off-canvas-box').removeClass('open')
        $('.menu-overlay').removeClass('open')
    });
    
    $('.menu-overlay').on('click', function(){
        $('.off-canvas-box').removeClass('open')
        $('.menu-overlay').removeClass('open')
    });

    /*Variables*/
    var $offCanvasNav = $('.canvas-menu'),
    $offCanvasNavSubMenu = $offCanvasNav.find('.sub-menu, .mega-sub-menu, .menu-item ');

    /*Add Toggle Button With Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.parent().prepend('<span class="mobile-menu-expand"></span>');

    /*Close Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.slideUp();

    /*Category Sub Menu Toggle*/
    $offCanvasNav.on('click', 'li a, li .mobile-menu-expand, li .menu-title', function(e) {
        var $this = $(this);
        if (($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('mobile-menu-expand'))) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length) {
                $this.parent('li').removeClass('active-expand');
                $this.siblings('ul').slideUp();
            } else {
                $this.parent('li').addClass('active-expand');
                $this.closest('li').siblings('li').find('ul:visible').slideUp();
                $this.closest('li').siblings('li').removeClass('active-expand');
                $this.siblings('ul').slideDown();
            }
        }
    });

    $( ".sub-menu, .mega-sub-menu, .menu-item" ).parent( "li" ).addClass( "menu-item-has-children" );
    $( ".mega-sub-menu" ).parent( "li" ).css( "position", "static" );
	


    /*--
        Slider
	-----------------------------------*/
    var slider = new Swiper('.slider-active', {
        speed: 600,
        effect: "fade",
        loop: true,
        pagination: {
            el: '.slider-active .swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        autoplay: {
            delay: 8000,
        },
    });


    /*--
        Product Active
    -----------------------------------*/
    var product = new Swiper('.product-active .swiper-container', {
        slidesPerView: 4,
        spaceBetween: 0,
        loop: true,
        watchSlidesVisibility: true,
        navigation: {
            nextEl: '.product-active .swiper-button-next',
            prevEl: '.product-active .swiper-button-prev',
            hideOnClick: true,
        },
        breakpoints: {
            0: {
              slidesPerView: 1,
            },
            576: {
              slidesPerView: 2,
            },
            768: {
              slidesPerView: 2,
            },
            992: {
              slidesPerView: 3,
            },
            1200: {
              slidesPerView: 4,
            },
        }
    });


    /*--
        Product Active 2
    -----------------------------------*/
    var product = new Swiper('.product-active-2 .swiper-container', {
        slidesPerView: 4,
        spaceBetween: 0,
        loop: true,
        watchSlidesVisibility: true,
        navigation: {
            nextEl: '.product-active-2 .swiper-button-next',
            prevEl: '.product-active-2 .swiper-button-prev',
            hideOnClick: true,
        },
        breakpoints: {
            0: {
              slidesPerView: 1,
            },
            576: {
              slidesPerView: 2,
            },
            768: {
              slidesPerView: 2,
            },
            992: {
              slidesPerView: 3,
            },
            1200: {
              slidesPerView: 4,
            },
            1600: {
              slidesPerView: 6,
            },
        }
    });


    /*--
        Blog Active
    -----------------------------------*/
    var blog = new Swiper('.blog-active .swiper-container', {
        slidesPerView: 3,
        spaceBetween: 30,
        loop: true,
        navigation: {
            nextEl: '.blog-active .swiper-button-next',
            prevEl: '.blog-active .swiper-button-prev',
        },
        breakpoints: {
            0: {
              slidesPerView: 1,
            },
            576: {
              slidesPerView: 1,
            },
            768: {
              slidesPerView: 2,
            },
            992: {
              slidesPerView: 3,
            },
            1200: {
              slidesPerView: 3,
            },
        }
    });


    /*--
        Testimonial Active
    -----------------------------------*/
    var blog = new Swiper('.testimonial-active .swiper-container', {
        slidesPerView: 1,
        spaceBetween: 0,
        loop: true,
        navigation: {
            nextEl: '.testimonial-active .swiper-button-next',
            prevEl: '.testimonial-active .swiper-button-prev',
        },        
    });


    /*--
        Blog Gallery Active
    -----------------------------------*/
    var blog = new Swiper('.gallery-active .swiper-container', {
        slidesPerView: 1,
        spaceBetween: 0,
        loop: true,
        navigation: {
            nextEl: '.gallery-active .swiper-button-next',
            prevEl: '.gallery-active .swiper-button-prev',
        },        
    });


    /*--
		slider range Activation
    -----------------------------------*/
	$( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: 10000,
        values: [ 1000, 8000 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) + " - $" + $( "#slider-range" ).slider( "values", 1 ) );


    /*--
		Color Script
    -----------------------------------*/
    $('.form-check .form-check-input').each(function() {
        var get_color = $(this).attr('data-color');
        $(this).css("background-color", get_color);
        $(this).css("border-color", get_color);
    });


    /*--
		Shop Single Slider
    -----------------------------------*/
    var verticalSliderNav = new Swiper('.vertical-slider-nav', {
        loop: false,
        draggable: false,
        allowTouchMove: false,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
        watchOverflow: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            0: {
                direction: 'horizontal',
                spaceBetween: 10,
                slidesPerView: 3,
                draggable: true,
                allowTouchMove: true,
            },
            576: {
                direction: 'vertical',
                spaceBetween: 10,
                slidesPerView: 4,
            },
        }
    });
    var pdSlider = new Swiper('.pd-vertical-slider', {
        autoplay: false,
        delay: 5000,
        slidesPerView: 1,
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        allowTouchMove: true,
        setWrapperSize: true,
        waitForTransition: true,
        loop: false,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        thumbs: {
            swiper: verticalSliderNav
        }
    });


    /*--
		Quick View Slider
    -----------------------------------*/
    var qvSliderNav = new Swiper('.quick-view-slider-nav', {
        loop: false,
        draggable: false,
        allowTouchMove: false,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
        watchOverflow: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            0: {
                direction: 'horizontal',
                spaceBetween: 10,
                slidesPerView: 3,
                draggable: true,
                allowTouchMove: true,
            },
            576: {
                direction: 'vertical',
                spaceBetween: 10,
                slidesPerView: 4,
            },
        }
    });
    var qvSlider = new Swiper('.quick-view-slider', {
        autoplay: false,
        delay: 5000,
        slidesPerView: 1,
        watchSlidesProgress: true,
        watchSlidesVisibility: true,
        allowTouchMove: true,
        setWrapperSize: true,
        waitForTransition: true,
        loop: false,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        thumbs: {
            swiper: qvSliderNav
        }
    });


    /*--
		Single Product Zoom Activation
    -----------------------------------*/
    $('.zoom').zoom();
    
    
    /*--
		Product Quantity Activation
    -----------------------------------*/
	$('.add').on('click', function () {
        if ($(this).prev().val()) {
            $(this).prev().val(+$(this).prev().val() + 1);
        }
    });
    $('.sub').on('click', function () {
        if ($(this).next().val() > 1) {
            if ($(this).next().val() > 1) $(this).next().val(+$(this).next().val() - 1);
        }
	});


   /*--
		Magnific Popup Activation
    -----------------------------------*/
	$('a.btn-gallery').on('click', function(event) {
		event.preventDefault();
		
		var gallery = $(this).attr('href');
		
		$(gallery).magnificPopup({
		  delegate: 'a',
		  type:'image',
		  gallery: {
			enabled: true
		  }
		}).magnificPopup('open');
	});


    /*--
		Rating
	-----------------------------------*/
    /* 1. Visualizing things on Hover - See next part for action on click */
    $('#stars li').on('mouseover', function(){
        var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
        
        // Now highlight all the stars that's not after the current hovered star
        $(this).parent().children('li.star').each(function(e){
            if (e < onStar) {
                $(this).addClass('hover');
            }
            else {
                $(this).removeClass('hover');
            }
        });
        
    }).on('mouseout', function(){
        $(this).parent().children('li.star').each(function(e){
            $(this).removeClass('hover');
        });
    });
    
    
    /* 2. Action to perform on click */
    var spansCounts =  $('#stars li').length
    $('#stars li').on('click', function(e) {
        console.log($(this).index())
        $('#stars li').removeClass('selected');

        for(var i=0 ; i < $(this).index() + 1; i++){
            $('#stars li').eq(i).addClass('selected')
        }
    })    


    /*--
		select2
	-----------------------------------*/
    $(".select2").select2({
        tags: true
    }); 


    /*--
		Checkout Account Active
	-----------------------------------*/
	$('#account').on('click', function () {
		if ($('#account:checked').length > 0) {
			$('.checkout-account').slideDown();
		} else {
			$('.checkout-account').slideUp();
		}
    });
    

    /*--
		Checkout Shipping Active
	-----------------------------------*/
	$('#shipping').on('click', function () {
		if ($('#shipping:checked').length > 0) {
			$('.checkout-shipping').slideDown();
		} else {
			$('.checkout-shipping').slideUp();
		}
    });
    

    /*--
		Checkout Payment Active
	-----------------------------------*/
	var checked = $('.payment-radio input:checked')
	if (checked) {
		$(checked).siblings('.payment-details').slideDown(500);
	};
	$('.payment-radio input').on('change', function() {
		$('.payment-details').slideUp(500);
		$(this).siblings('.payment-details').slideToggle(500);
	});


    /*--
		Back to top Script
	-----------------------------------*/
    // Show or hide the sticky footer button
    $(window).on('scroll', function (event) {
        if ($(this).scrollTop() > 600) {
            $('.back-to-top').fadeIn(200)
        } else {
            $('.back-to-top').fadeOut(200)
        }
    });

    //Animate the scroll to yop
    $('.back-to-top').on('click', function (event) {
    event.preventDefault();

        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });



    
})(jQuery);

