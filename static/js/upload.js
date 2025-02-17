const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");
const checkBtn = document.getElementById("checkBtn"); // Ensure this exists
const resultDiv = document.getElementById("result"); // Ensure this exists

inputFile.addEventListener("change", uploadImage);

function uploadImage() {
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = `url('${imgLink}')`;

    imageView.textContent = "";
    imageView.style.border = 0;
}

dropArea.addEventListener("dragover", function (e) {
    e.preventDefault();
});

dropArea.addEventListener("drop", function (e) {
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage();
});

checkBtn.addEventListener("click", function (e) {
    e.preventDefault(); // Prevent default refresh

    if (inputFile.files.length === 0) {
        alert("Please upload an X-ray image first.");
        return;
    }

    let formData = new FormData();
    formData.append("xray_image", inputFile.files[0]);

    fetch("http://127.0.0.1:8000/loginapp/pneumoniadiv/", {  // Ensure backend URL is correct
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response:", data);

        // Display the result
        resultDiv.innerHTML = <p><strong>Prediction:</strong> ${data.prediction}</p>;
        resultDiv.style.display = "block";

        // Change background color based on result
        resultDiv.style.backgroundColor = 
            data.prediction === "Pneumonia Detected" ? "#dc3545" : "#28a745";
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong. Please try again.");
    });
});