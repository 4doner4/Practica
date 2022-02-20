//Create parallax
function parallax(event) {
    this.querySelectorAll('.background__img').forEach(element => {
        element.style.transform = 'translateX(' + event.clientX / 100 + 'px) translateY(' + event.clientY / 100 +'px)';
    });
}

document.addEventListener('mousemove', parallax);