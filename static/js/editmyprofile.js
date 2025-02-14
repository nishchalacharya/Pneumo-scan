document.addEventListener('DOMContentLoaded', function () {
    const saveButton = document.querySelector('.save-btn');
    const fileInput = document.getElementById('file-input');
    const profilePreview = document.getElementById('profile-preview');

    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                profilePreview.src = e.target.result; 
            };
            reader.readAsDataURL(file);
        }
    });
    saveButton.addEventListener('click', function () {
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const role = document.getElementById('role').value;
        const fileInput = document.getElementById('file-input');

        const formData = new FormData();
        formData.append('name', name);
        formData.append('email', email);
        formData.append('phone', phone);
        formData.append('role', role);

        if (fileInput.files.length > 0) {
            formData.append('photo', fileInput.files[0]);
        }

        // Get CSRF token from the HTML (Django requires it for security)
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('/save-profile/', { // Django backend endpoint
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Profile saved successfully!');
            } else {
                alert('Error saving profile. Please try again.');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
