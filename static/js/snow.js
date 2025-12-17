console.log("❄️ snow.js loaded");

const snowImages = [
  '/static/images/snowflake1.png',
  '/static/images/snowflake2.png',
  '/static/images/snowflake3.png'
];

for (let i = 0; i < 45; i++) {
  const snow = document.createElement('div');
  snow.classList.add('snowflake');

  const size = 6 + Math.random() * 14;
  snow.style.width = size + 'px';
  snow.style.height = size + 'px';

  snow.style.left = Math.random() * 100 + 'vw';
  snow.style.backgroundImage =
    `url(${snowImages[Math.floor(Math.random() * snowImages.length)]})`;

  snow.style.animationDuration = (6 + Math.random() * 6) + 's';
  snow.style.animationDelay = Math.random() * 5 + 's';

  document.body.appendChild(snow);
}
