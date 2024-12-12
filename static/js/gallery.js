document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.gallery-container img');
    const lightbox = document.createElement('div');
    lightbox.classList.add('lightbox');
    document.body.appendChild(lightbox);

    const img = document.createElement('img');
    lightbox.appendChild(img);

    images.forEach(image => {
        image.addEventListener('click', () => {
            console.log('Image clicked:', image.src);
            lightbox.style.display = 'flex';
            img.src = image.src;
        });
    });

    lightbox.addEventListener('click', () => {
        console.log('Lightbox clicked');
        lightbox.style.display = 'none';
    });
});
