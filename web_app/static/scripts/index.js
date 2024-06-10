document.addEventListener('DOMContentLoaded', () => {
  let currentIndex = 0;
  const testimonials = document.querySelectorAll('.testimonial-item');
  const slider = document.querySelector('.testimonial-slider');
  const nextButton = document.querySelector('.testimonial-nav-button.next');
  const prevButton = document.querySelector('.testimonial-nav-button.prev');
  let interval;

  function showSlide(index) {
    const maxIndex = testimonials.length - 1;
    if (index < 0) {
      currentIndex = maxIndex;
    } else if (index > maxIndex) {
      currentIndex = 0;
    } else {
      currentIndex = index;
    }

    const offset = -currentIndex * (testimonials[0].offsetWidth + 20); // 20 is the gap
    testimonials.forEach((testimonial, i) => {
      testimonial.style.transform = `translateX(${offset + (i * (testimonials[0].offsetWidth + 20))}px)`;
    });
  }

  function nextSlide() {
    showSlide(currentIndex + 1);
  }

  function prevSlide() {
    showSlide(currentIndex - 1);
  }

  // Automatic sliding
  function startAutoSlide() {
    interval = setInterval(nextSlide, 3000); // Change slide every 3 seconds
  }

  function stopAutoSlide() {
    clearInterval(interval);
  }

  // Event listeners for buttons
  nextButton.addEventListener('click', () => {
    nextSlide();
    stopAutoSlide(); // Stop auto sliding when manually navigating
    startAutoSlide(); // Restart auto sliding after navigation
  });

  prevButton.addEventListener('click', () => {
    prevSlide();
    stopAutoSlide(); // Stop auto sliding when manually navigating
    startAutoSlide(); // Restart auto sliding after navigation
  });

  // Hover effect
  testimonials.forEach(testimonial => {
    testimonial.addEventListener('mouseover', stopAutoSlide); // Pause automatic sliding on hover
    testimonial.addEventListener('mouseout', startAutoSlide); // Resume automatic sliding on mouse out
  });

  // Initialize the first slide
  showSlide(currentIndex);
  startAutoSlide(); // Start automatic sliding
});








// var swiper = new Swiper(".mySwiper", {
//     slidesPerView: 1,
//     centeredSlides: false,
//     slidesPerGroupSkip: 1,
//     grabCursor: true,
//     keyboard: {
//       enabled: true,
//     },
//     breakpoints: {
//       769: {
//         slidesPerView: 2,
//         slidesPerGroup: 2,
//       },
//     },
//     scrollbar: {
//       el: ".swiper-scrollbar",
//     },
//     navigation: {
//       nextEl: ".swiper-button-next",
//       prevEl: ".swiper-button-prev",
//     },
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//     },
//   });

//   //Global variables
// var element;

// //Detect onclick event
// if (window.matchMedia("(max-width: 920px)").matches === false) {
//     $(".ham").on("click", function(){
//         $(".side_menu").css("right", "0px");
//         $(".overlay").css("opacity","1");
//         $(".overlay").css("z-index","99");
//     });

//     $(".close").on("click", function(){
//         $(".contact").css("top") >= "10%" ? $(".contact").hide().css("top","-100%").fadeOut('100') : $(".side_menu").css("right", "-500px");
//         $(".overlay").css("opacity","0");
//         $(".overlay").css("z-index","-1");
//     });

//     $(".overlay").on("click", function(){
//         $(".contact").css("top") >= "10%" ? $(".contact").hide().css("top","-100%").fadeOut('100') : $(".side_menu").css("right", "-500px");
//         $(".overlay").css("opacity","0");
//         $(".overlay").css("z-index","-1");
//     });
// } else {
//     $(".ham").on("click", function(){
//         $(".side_menu").css("right", "0px");
//         $(".overlay").css("opacity","1");
//         $(".overlay").css("z-index","9");
//     });
    
//     $(".close").on("click", function(){
//         $(".contact").css("top") >= "10%" ? $(".contact").hide().css("top","-100%").fadeOut('100') : $(".side_menu").css("right", "-120%");
//         $(".overlay").css("opacity","0");
//         $(".overlay").css("z-index","-1");
//     });
    
//     $(".overlay").on("click", function(){
//         $(".contact").css("top") >= "10%" ? $(".contact").hide().css("top","-100%").fadeOut('100') : $(".side_menu").css("right", "-120%");
//         $(".overlay").css("opacity","0");
//         $(".overlay").css("z-index","-1");
//     });
// }


// //Scroller Nav
// window.onscroll = function() {
//     if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
//         $("nav").addClass("fixed_nav");
//     } else {
//         $("nav").removeClass("fixed_nav");
//     }
// }


// //DETECT ESC KEY PRESSED
// document.onkeydown = function(evt) {
//     evt = evt || window.event;
//     var isEscape = false;
//     if ("key" in evt) {
//         isEscape = (evt.key === "Escape" || evt.key === "Esc");
//     } else {
//         isEscape = (evt.keyCode === 27);
//     }
//     if (isEscape) {
//         if ($(".overlay").css("opacity") == "1"){
//             $(".contact").css("top") >= "10%" ? $(".contact").hide().css("top","-100%").fadeOut('100') : $(".side_menu").css("right", "-120%");
//             $(".overlay").css("opacity","0");
//             $(".overlay").css("z-index","-1");
//         }
//     }
// };



// //Dropdown
// $(".dropdown").click(function(){
//     if ($(this).children("aside").is(":hidden")){
//         $(this).children("aside").show("slow");
//         $(this).children("a").css("color","var(--white)");
//     } else {
//         $(this).children("aside").hide("slow");
//         $(this).children("a").css("color","var(--lite)");
//     }
// });








// //Global variables
// var slidestoshow, arrowmark;
// if (window.matchMedia("(max-width: 920px)").matches === false) {
//     slidestoshow = 4;
//     arrowmark = true;
// } else {
//     slidestoshow = 1;
//     arrowmark = false;
// }

// $('.blog-slider').slick({
//     slidesToShow: slidestoshow,
//     slidesToScroll: 1,
//     dots: false,
//     arrows: arrowmark,
//     autoplay: true,
//     autoplaySpeed: 2000,
//     infinite: true
// });


// $('.event-slider').slick({
// 	slidesToShow: 1,
// 	slidesToScroll: 1,
// 	dots: false,
// 	arrows: false,
// 	autoplay: true,
// 	autoplaySpeed: 4000,
// 	infinite: true
// });






