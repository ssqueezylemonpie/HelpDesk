from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dev_secret_key'

# --- Mock data for UI preview (replace with real DB queries later) ---
MOCK_TICKETS = [
    {'id': 1, 'title': 'Cannot connect to school WiFi', 'status': 'open', 'priority': 'high', 'category': 'Network', 'name': 'Ola Nordmann', 'email': 'ola@school.no', 'description': 'I am unable to connect to the school WiFi on my laptop. It worked fine yesterday.', 'created_at': '2026-03-20 09:15'},
    {'id': 2, 'title': 'Projector not working in room 204', 'status': 'in_progress', 'priority': 'medium', 'category': 'Hardware', 'name': 'Kari Hansen', 'email': 'kari@school.no', 'description': 'The HDMI projector in room 204 does not display anything when connected to my laptop.', 'created_at': '2026-03-21 11:30'},
    {'id': 3, 'title': 'Forgot password for Office 365', 'status': 'closed', 'priority': 'low', 'category': 'Account', 'name': 'Per Olsen', 'email': 'per@school.no', 'description': 'I have forgotten my password and cannot reset it myself.', 'created_at': '2026-03-22 14:00'},
    {'id': 4, 'title': 'Python not installed on lab PCs', 'status': 'open', 'priority': 'high', 'category': 'Software', 'name': 'Ida Berg', 'email': 'ida@school.no', 'description': 'Python 3 is not installed on the computers in the IT lab. We need it for class.', 'created_at': '2026-03-23 08:45'},
]

@app.route('/')
def index():
    stats = {
        'total': len(MOCK_TICKETS),
        'open': sum(1 for t in MOCK_TICKETS if t['status'] == 'open'),
        'in_progress': sum(1 for t in MOCK_TICKETS if t['status'] == 'in_progress'),
        'closed': sum(1 for t in MOCK_TICKETS if t['status'] == 'closed'),
    }
    return render_template('index.html', tickets=MOCK_TICKETS, stats=stats)

@app.route('/ticket/new', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        flash('Your ticket has been submitted successfully! We will get back to you shortly.', 'success')
        return redirect(url_for('index'))
    return render_template('create_ticket.html')

@app.route('/ticket/<int:ticket_id>')
def view_ticket(ticket_id):
    ticket = next((t for t in MOCK_TICKETS if t['id'] == ticket_id), None)
    if not ticket:
        flash('Ticket not found.', 'error')
        return redirect(url_for('index'))
    return render_template('view_ticket.html', ticket=ticket)

@app.route('/ticket/<int:ticket_id>/update', methods=['POST'])
def update_ticket(ticket_id):
    flash('Ticket status updated.', 'success')
    return redirect(url_for('view_ticket', ticket_id=ticket_id))

if __name__ == '__main__':
    app.run(debug=True)
