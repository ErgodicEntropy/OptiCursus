 // Function to update the displayed value for sliders
 function updateValue(value, elementId) {
    document.getElementById(elementId).innerText = value;
}

// Function to show the loading overlay
function showLoading() {
    document.getElementById('loading-overlay').style.display = 'flex';
}

// Function to hide the loading overlay
function hideLoading() {
    document.getElementById('loading-overlay').style.display = 'none';
}

// Function to update the loading message
function updateLoadingMessage(message) {
    document.getElementById('loading-message').textContent = message;
}

function showCustomDomain(select){
    const overlay = document.getElementById("domainOverlay");
    if (select.value === "AddDomain") {
        overlay.style.display = 'block';
    }
}

function SaveUserDomain(){
    const overlay = document.getElementById("domainOverlay");
    overlay.style.display = 'none';
}

function showCustomGoal(select){
    const overlay = document.getElementById("goalOverlay");
    if (select.value === "AddGoal") {
        overlay.style.display = 'block';
    }
}

function SaveUserGoal(){
    const overlay = document.getElementById("goalOverlay");
    overlay.style.display = 'none';
}

function showCustomCursusLevel(select){
    const overlay = document.getElementById("levelOverlay");
    if (select.value === "AddLevel") {
        overlay.style.display = 'block';
    }
}

function SaveCursusLevel(){
    const overlay = document.getElementById("levelOverlay");
    overlay.style.display = 'none';
}

function showCustomStudentLevel(select){
    const overlay = document.getElementById("studentlevelOverlay");
    if (select.value === "AddStudentLevel") {
        overlay.style.display = 'block';
    }
}

function SaveStudentLevel(){
    const overlay = document.getElementById("studentlevelOverlay");
    overlay.style.display = 'none';
}


document.getElementById('mainForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission

    showLoading();
    updateLoadingMessage('Processing your request. Please wait...');

    // Gather all form data
    const formData = new FormData(this);

    // Submit to the /data endpoint
    fetch('/data', {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.ok) {
            // Update the loading message
            updateLoadingMessage('Almost there! Thanks for your patience');

            // Submit the hidden form to /output (POST request)
            document.getElementById('redirectForm').submit();
        } else {
            console.error('Error submitting to /data:', response.status);
            updateLoadingMessage('Something went wrong. Please try again.');
            hideLoading(); // Hide the loading overlay on error
        }
    }).catch(error => {
        console.error('Error submitting to /data:', error);
        updateLoadingMessage('Something went wrong. Please try again.');
        hideLoading(); // Hide the loading overlay on error
    });
});


