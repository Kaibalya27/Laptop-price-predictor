// script.js

document.addEventListener('DOMContentLoaded', () => {
    const scrollButton = document.getElementById('contributors');
    const targetSection = document.getElementById('contributorsTarget');

    scrollButton.addEventListener('click', () => {
        targetSection.scrollIntoView({ behavior: 'smooth' });
    });
});
