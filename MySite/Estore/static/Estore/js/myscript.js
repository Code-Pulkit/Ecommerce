$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        // WHen the Screen Width is 0
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        // WHen the Screen Width is 600
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        // WHen the Screen Width is 1000
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})