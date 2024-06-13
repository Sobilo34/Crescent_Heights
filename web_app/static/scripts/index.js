// Upper Slide
document.addEventListener('DOMContentLoaded', () => {
  let slideIndex = 0;
  const slides = document.getElementsByClassName('mySlides');
  const dots = document.getElementsByClassName('dot');

  function showSlides() {
    for (let i = 0; i < slides.length; i++) {
      slides[i].style.display = 'none';
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    for (let i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(' active', '');
    }
    slides[slideIndex-1].style.display = 'block';
    dots[slideIndex-1].className += ' active';
    setTimeout(showSlides, 11000); // Change slide every 11 seconds
  }

  showSlides();
});



document.addEventListener('DOMContentLoaded', () => {
  let currentIndex = 0;
  const testimonials = document.querySelectorAll('.testimonial-item');
  const nextButton = document.querySelector('.testimonial-nav-button.next');
  const prevButton = document.querySelector('.testimonial-nav-button.prev');
  const gap = -230; // Set the gap to 230px
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

    const itemWidth = testimonials[0].offsetWidth + gap;
    testimonials.forEach((testimonial, i) => {
      const offset = (i - currentIndex) * itemWidth; // Calculate offset for each item
      testimonial.style.transform = `translateX(${offset}px)`;
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

  // Start automatic sliding only on large screens
  if (window.innerWidth > 768) {
    startAutoSlide(); // Start automatic sliding
  }
});




document.addEventListener('DOMContentLoaded', () => {
  let currentIndex = 0;
  const newsItems = document.querySelectorAll('.news-item');
  const slider = document.querySelector('.news-slider');
  const nextButton = document.querySelector('.news-nav-button.next');
  const prevButton = document.querySelector('.news-nav-button.prev');
  const gap = -230; // Set the gap to 10px
  let interval;

  function showSlide(index) {
    const maxIndex = newsItems.length - 1;
    if (index < 0) {
      currentIndex = maxIndex;
    } else if (index > maxIndex) {
      currentIndex = 0;
    } else {
      currentIndex = index;
    }

    const offset = -currentIndex * (newsItems[0].offsetWidth + gap);
    newsItems.forEach((news, i) => {
      news.style.transform = `translateX(${offset + (i * (newsItems[0].offsetWidth + gap))}px)`;
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
  newsItems.forEach(news => {
    news.addEventListener('mouseover', stopAutoSlide); // Pause automatic sliding on hover
    news.addEventListener('mouseout', startAutoSlide); // Resume automatic sliding on mouse out
  });

  // Initialize the first slide
  showSlide(currentIndex);

  // Start automatic sliding only on large screens
  if (window.innerWidth > 768) {
    startAutoSlide(); // Start automatic sliding
  } else {
    stopAutoSlide(); // Disable automatic sliding for small screens
  }
});




document.addEventListener('DOMContentLoaded', () => {
  const virtualTourButton = document.querySelector('.virtual-tour-button');

  virtualTourButton.addEventListener('click', () => {
    // Replace the URL with the actual link to your virtual tour
    window.location.href = 'https://your-virtual-tour-link.com';
  });
});


// Path: web_app/static/scripts/index.js
