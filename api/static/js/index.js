document.addEventListener('scroll', function() {
  const images = document.querySelectorAll('.img-fluid');
  images.forEach(img => {
    const rect = img.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom > 0) {
      img.classList.add('img-appear');
    }
  });
});
