document.getElementById('loadButton').addEventListener('click', function () {
  fetch('/content', { method: 'POST' })
    .then(response => response.text())
    .then(data => {
      document.getElementById('content').textContent = data;
    });
});