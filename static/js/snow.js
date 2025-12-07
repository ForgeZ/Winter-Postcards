const petalColors = ['#ffffff', '#f2f2f2', '#e9eef6', '#dde7fa'];

for (let i = 0; i < 40; i++) {
  const petal = document.createElement('div');
  petal.classList.add('petal');

  const size = 6 + Math.random() * 14;
  petal.style.width = size + 'px';
  petal.style.height = size + 'px';

  petal.style.left = Math.random() * 100 + 'vw';
  petal.style.background = petalColors[Math.floor(Math.random() * petalColors.length)];

  petal.style.animationDuration = (5 + Math.random() * 5) + 's';
  petal.style.animationDelay = (Math.random() * 5) + 's';

  document.body.appendChild(petal);
}
