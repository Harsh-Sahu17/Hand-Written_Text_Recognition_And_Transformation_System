document.getElementById('image-upload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.getElementById('input-preview');
            img.src = e.target.result;
            img.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('process-button').addEventListener('click', function() {
    const fileInput = document.getElementById('image-upload');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please upload an image.');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);
    formData.append('font_size', document.getElementById('font-size').value);
    formData.append('text_color', document.getElementById('text-color').value);
    
    fetch('/process-image', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const outputImage = document.getElementById('output-image');
        outputImage.src = url;
        outputImage.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
