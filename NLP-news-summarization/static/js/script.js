// Get the form element and the summary element
const form = document.querySelector('form');
const summary = document.querySelector('.summary');

// Add an event listener for form submission
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  summary.innerHTML = 'Loading...';

  // Get the text input and the selected summary type
  const text = form.text.value;
  const type = form.type.value;

  // Make a POST request to the server to get the summary
  const response = await fetch(`/${type}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text })
  });

  // Display the summary or an error message
  const data = await response.json();
  if (response.ok) {
    summary.innerHTML = data.summary;
  } else {
    summary.innerHTML = data.error;
  }
});
