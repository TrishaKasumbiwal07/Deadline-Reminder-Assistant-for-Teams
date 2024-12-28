document.getElementById('add-deadline-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const task = document.getElementById('task').value;
    const deadline_date = document.getElementById('deadline_date').value;
    const email = document.getElementById('email').value;

    const response = await fetch('/add_deadline', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task, deadline_date, email })
    });

    const data = await response.json();
    alert(data.message);
});
