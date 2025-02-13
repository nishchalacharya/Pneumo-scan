  
    var swiper = new Swiper(".mySwiperservices", {
      slidesPerView: 1,
      spaceBetween: 10,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        700: {
          slidesPerView: 1,
          spaceBetween: 40,
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
      },
    });

    /*==team===*/
    var swiper = new Swiper(".mySwiperteam", {
      slidesPerView: 1,
      spaceBetween: 10,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      breakpoints: {
        560: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        950: {
          slidesPerView: 3,
          spaceBetween: 40,
        },
        1250: {
          slidesPerView: 4,
          spaceBetween: 50,
        },
      },
    });
  