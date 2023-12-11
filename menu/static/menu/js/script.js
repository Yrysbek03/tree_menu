const dropdownBtns = document.querySelectorAll('.dropdown-btn');

dropdownBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    btn.nextElementSibling.classList.toggle('show');
  });
});