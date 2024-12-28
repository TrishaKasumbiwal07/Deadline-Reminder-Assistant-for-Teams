from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import schedule
import time

app = Flask(__name__)

# In-memory storage for deadlines (use SQLite for production)
deadlines = []

# Add a new deadline
@app.route('/add_deadline', methods=['POST'])
def add_deadline():
    data = request.json
    deadline = {
        'task': data['task'],
        'deadline_date': data['deadline_date'],
        'email': data['email']
    }
    deadlines.append(deadline)
    return jsonify({'message': 'Deadline added successfully!', 'data': deadline})

# Get all deadlines
@app.route('/deadlines', methods=['GET'])
def get_deadlines():
    return jsonify(deadlines)

# Email Reminder (dummy function, replace with SendGrid API)
def send_email_reminder(email, task):
    print(f"Sending reminder to {email} for task: {task}")

# Scheduler to send reminders
def reminder_scheduler():
    for deadline in deadlines:
        deadline_date = datetime.strptime(deadline['deadline_date'], "%Y-%m-%d")
        if deadline_date - timedelta(days=1) <= datetime.now():
            send_email_reminder(deadline['email'], deadline['task'])

schedule.every().day.at("09:00").do(reminder_scheduler)

if __name__ == '__main__':
    app.run(debug=True)
