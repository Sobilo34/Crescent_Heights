// document.addEventListener('DOMContentLoaded', () => {
//     let currentIndex = 0;
//     const items = document.querySelectorAll('.testimonial-item');
//     const totalItems = items.length;
//     const nextButton = document.getElementById('next-btn');
//     const prevButton = document.getElementById('prev-btn');
//     let interval;
  
//     function showTestimonial(index) {
//       items.forEach((item, i) => {
//         if (i === index) {
//           item.classList.add('active');
//         } else {
//           item.classList.remove('active');
//         }
//       });
//     }
  
//     function showNextTestimonial() {
//       currentIndex = (currentIndex + 1) % totalItems;
//       showTestimonial(currentIndex);
//     }
  
//     function showPrevTestimonial() {
//       currentIndex = (currentIndex - 1 + totalItems) % totalItems;
//       showTestimonial(currentIndex);
//     }
  
//     function startAutoSlide() {
//       interval = setInterval(showNextTestimonial, 5000);
//     }
  
//     function stopAutoSlide() {
//       clearInterval(interval);
//     }
  
//     nextButton.addEventListener('click', showNextTestimonial);
//     prevButton.addEventListener('click', showPrevTestimonial);
  
//     const slider = document.getElementById('testimonial-slider');
//     slider.addEventListener('mouseenter', stopAutoSlide);
//     slider.addEventListener('mouseleave', startAutoSlide);
  
//     startAutoSlide();
//   });