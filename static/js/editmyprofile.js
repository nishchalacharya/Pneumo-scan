// Handle photo upload and preview
const fileInput = document.getElementById('file-input');
const profilePreview = document.getElementById('profile-preview');
const fileNameDisplay = document.getElementById('file-name');

fileInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            profilePreview.src = e.target.result;
            fileNameDisplay.textContent = `Selected: ${file.name}`;
        };
        reader.readAsDataURL(file);
    }
});

function togglePhoneInput() {
    const phoneInput = document.getElementById('phone-input');
    phoneInput.classList.toggle('visible');
}

document.getElementById('profile-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', document.getElementById('name').value);
    formData.append('email', document.getElementById('email').value);
    formData.append('phone', document.getElementById('phone').value || null);
    formData.append('isDoctor', document.getElementById('is-doctor').checked);

    if (fileInput.files[0]) {
        formData.append('photo', fileInput.files[0]);
    }

    console.log('Profile data:', {
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        isDoctor: formData.get('isDoctor'),
        photoUploaded: !!fileInput.files.length,
    });

    alert('Profile saved successfully!');
});