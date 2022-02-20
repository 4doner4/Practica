let cards = document.querySelectorAll('.card__item');
const halfHeightCard = document.querySelector('.card__item').offsetHeight / 2;

//Create listener for cards
for (let i = 0; i < cards.length; i++) {
	let card = cards[i];
	card.addEventListener('mousemove', MoveCard);
	card.addEventListener('mouseout', StopMoveCard);
}

//Create animation for cards
function StopMoveCard(event) {
	this.style.transform = 'rotateX(0deg) rotate(0deg)';
}

function MoveCard(event) {
	this.style.transform = 'rotateX('+ (halfHeightCard - event.offsetY) / 5 +'deg) rotateY('+ (event.offsetX - halfHeightCard) / 5 +'deg)';
}

//Create animation underline for text
function UnderlineText(event) {
    let childs = this.parentElement.childNodes;
    childs[3].style.width = halfHeightCard + 'px';
}

function DeleteUnderline(event) {
    let childs = this.parentElement.childNodes;
    childs[3].style.width = '0px';
}

//Create Listener for text
document.querySelectorAll('.info__list').forEach(text => {
    text.addEventListener('mouseover', UnderlineText);
    text.addEventListener('mouseout', DeleteUnderline);
});



