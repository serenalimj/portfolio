document.getElementById('year').textContent = new Date().getFullYear();
const portfolio = document.getElementById('serena-work');
const filters = portfolio.querySelector('.filters');
const buttons = [...filters.querySelectorAll('button')];
const cards = [...portfolio.querySelectorAll('article')];
filters.hidden = false;
buttons.forEach(button => button.addEventListener('click', () => {
  const category = button.dataset.filter;
  buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  cards.forEach(card => { card.hidden = category !== 'All' && card.dataset.category !== category; });
}));
