// Main Code
// Loader fade out and content fade in
window.addEventListener('load', () => {
  setTimeout(() => {
    document.querySelector('.loader').style.display = 'none';
    document.querySelector('nav').classList.add('visible');
    document.querySelector('.body-content').classList.add('active');
  }, 2000); // Adjust timing as needed
});

// Mobile menu toggle
const menuIcon = document.getElementById('menu');
const links = document.querySelector('.links');
menuIcon.addEventListener('click', () => {
  links.classList.toggle('active');
});

// Get the modal and button
const modal = document.getElementById('modal');
const btn = document.getElementById('clean');
const closeBtn = document.getElementById('close-btn');

// Open the modal when clicking the button
btn.onclick = () => {
    modal.style.display = "block";
}

// Close the modal when clicking the close button
closeBtn.onclick = () => {
    modal.style.display = "none";
}

// Close modal when clicking outside the modal content
window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function toggleChat() {
  const popup = document.getElementById("chat-popup");
  popup.style.display = (popup.style.display === "none" || popup.style.display === "") ? "flex" : "none";
}


