
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

    const offset = -currentIndex * (testimonials[0].offsetWidth + 10); // 10 is the gap
    testimonials.forEach((testimonial, i) => {
      testimonial.style.transform = `translateX(${offset + (i * (testimonials[0].offsetWidth + 10))}px)`;
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


document.addEventListener('DOMContentLoaded', () => {
  let currentIndex = 0;
  const newsItems = document.querySelectorAll('.news-item');
  const slider = document.querySelector('.news-slider');
  const nextButton = document.querySelector('.news-nav-button.next');
  const prevButton = document.querySelector('.news-nav-button.prev');
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

    const offset = -currentIndex * (newsItems[0].offsetWidth + 20); // 20 is the gap
    newsItems.forEach((news, i) => {
      news.style.transform = `translateX(${offset + (i * (newsItems[0].offsetWidth + 20))}px)`;
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
  startAutoSlide(); // Start automatic sliding
});


document.addEventListener('DOMContentLoaded', () => {
  const virtualTourButton = document.querySelector('.virtual-tour-button');

  virtualTourButton.addEventListener('click', () => {
    // Replace the URL with the actual link to your virtual tour
    window.location.href = 'https://your-virtual-tour-link.com';
  });
});


// Path: web_app/static/scripts/index.js
