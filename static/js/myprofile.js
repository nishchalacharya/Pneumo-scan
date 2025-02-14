function goToEditPage() {
            
    window.location.href = 'editmyprofile.html'; 
}
document.addEventListener("DOMContentLoaded", function() {
    fetch('/get_user_profile/') // Django URL
    .then(response => response.json())
    .then(data => {
        document.querySelector(".field-group:nth-child(1) p").textContent = data.name;
        document.querySelector(".field-group:nth-child(2) p").textContent = data.email;
        document.querySelector(".field-group:nth-child(3) p").textContent = data.phone;
        document.querySelector(".field-group:nth-child(4) p").textContent = data.role;
        document.querySelector(".profile-picture").src = data.profile_picture;
    })
    .catch(error => console.error("Error fetching user profile:", error));
});