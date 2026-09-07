const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('[data-menu-button]');
const nav = document.querySelector('[data-nav]');

window.addEventListener('scroll', () => header?.classList.toggle('is-scrolled', window.scrollY > 24));
menuButton?.addEventListener('click', () => {
  nav.classList.toggle('is-open');
  menuButton.classList.toggle('is-open');
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => nav.classList.remove('is-open')));

document.querySelectorAll('[data-filters] button').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('[data-filters] button').forEach(item => item.classList.remove('active'));
  button.classList.add('active');
  const filter = button.dataset.filter;
  document.querySelectorAll('.vehicle-card').forEach(card => { card.hidden = filter !== 'all' && card.dataset.category !== filter; });
}));

document.querySelectorAll('[data-vehicle]').forEach(link => link.addEventListener('click', () => {
  const vehicle = document.querySelector('[name="vehicle"]');
  if (vehicle) vehicle.value = link.dataset.vehicle;
}));

const today = new Date().toISOString().split('T')[0];
const pickup = document.querySelector('[name="pickup_date"]');
const returnDate = document.querySelector('[name="return_date"]');
if (pickup && returnDate) {
  pickup.min = today;
  returnDate.min = today;
  pickup.addEventListener('change', () => { returnDate.min = pickup.value || today; });
}

document.querySelectorAll('form[data-api]').forEach(form => form.addEventListener('submit', async event => {
  event.preventDefault();
  const status = form.querySelector('.form-status');
  const button = form.querySelector('button[type="submit"]');
  if (!form.checkValidity()) { form.reportValidity(); return; }
  button.disabled = true;
  status.textContent = 'Sending...';
  try {
    const response = await fetch(form.dataset.api, { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(Object.fromEntries(new FormData(form))) });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || 'Please try again.');
    status.textContent = result.message;
    form.reset();
  } catch (error) { status.textContent = error.message; }
  finally { button.disabled = false; }
}));
