from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db_connection
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev_secret_key')


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets ORDER BY created_at DESC")
    tickets = cursor.fetchall()
    cursor.close()
    conn.close()

    stats = {
        'total': len(tickets),
        'open': sum(1 for t in tickets if t['status'] == 'open'),
        'in_progress': sum(1 for t in tickets if t['status'] == 'in_progress'),
        'closed': sum(1 for t in tickets if t['status'] == 'closed'),
    }
    return render_template('index.html', tickets=tickets, stats=stats)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Check if user already exists
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        if cursor.fetchone():
            flash('Username or email already exists.', 'error')
            cursor.close()
            conn.close()
            return redirect(url_for('register'))

        password_hash = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_hash)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            # Save user info in the session
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


@app.route('/ticket/new', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        category = request.form.get('category')
        name = request.form.get('name')
        email = request.form.get('email')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tickets (title, description, priority, category, name, email) VALUES (%s, %s, %s, %s, %s, %s)",
            (title, description, priority, category, name, email)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash('Your ticket has been submitted successfully! We will get back to you shortly.', 'success')
        return redirect(url_for('index'))

    return render_template('create_ticket.html')


@app.route('/ticket/<int:ticket_id>')
def view_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets WHERE id = %s", (ticket_id,))
    ticket = cursor.fetchone()
    cursor.close()
    conn.close()

    if not ticket:
        flash('Ticket not found.', 'error')
        return redirect(url_for('index'))

    return render_template('view_ticket.html', ticket=ticket)


@app.route('/ticket/<int:ticket_id>/update', methods=['POST'])
def update_ticket(ticket_id):
    new_status = request.form.get('status')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tickets SET status = %s WHERE id = %s",
        (new_status, ticket_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    flash('Ticket status updated.', 'success')
    return redirect(url_for('view_ticket', ticket_id=ticket_id))


if __name__ == '__main__':
    app.run(debug=True)
