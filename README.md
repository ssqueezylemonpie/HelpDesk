# Helpdesk Application

A fully functional Helpdesk ticketing system built with **Flask (Python)**, **MariaDB**, **HTML**, and **Vanilla CSS**.

## ✨ Features
- **User Authentication**: Secure Sign Up and Log In system with password hashing (`werkzeug.security`).
- **Ticket Management**: Create, view, and update support tickets.
- **Status Tracking**: Keep track of tickets with dynamic status badges (*Open*, *In Progress*, and *Closed*) and priorities.
- **User Dashboard**: See all active and past tickets at a glance with live statistics.
- **Premium UI**: A clean, modern, fully responsive dark-themed interface built from scratch without bulky CSS frameworks.

## 🛠 Prerequisites
Before running the application, make sure you have the following installed:
- [Python 3.x](https://www.python.org/)
- [MariaDB](https://mariadb.org/)

## 📁 Project Structure
```text
Helpdesk/
│
├── app.py                 # Main Flask application and routes
├── database.py            # Database connection setup
├── schema.sql             # SQL code to define database tables
├── run_schema.py          # Script to initialize tables in MariaDB
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (DB credentials)
├── README.md              # Project documentation
│
├── static/                # Static assets
│   ├── css/
│   │   └── style.css      # Vanilla CSS styles (Premium Dark Theme)
│   └── images/            # Image assets
│
└── templates/             # HTML templates
    ├── base.html          # Base layout template and Navbar
    ├── index.html         # Dashboard / Ticket list
    ├── create_ticket.html # Form to submit a new ticket
    ├── view_ticket.html   # Detailed view of a single ticket
    ├── login.html         # User login page
    └── register.html      # User registration page
```

## 🚀 Setup Instructions

### 1. Database Configuration
1. Log in to your MariaDB console:
   ```bash
   mariadb -u root -p
   ```
2. Create the database for the helpdesk:
   ```sql
   CREATE DATABASE helpdesk;
   EXIT;
   ```

### 2. Environment Setup
1. Open a terminal in the project directory.
2. Create and activate a virtual environment:
   - **Windows**: 
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Application Configuration
Ensure your `.env` file in the root of the project has your actual database credentials:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_actual_password
DB_NAME=helpdesk
FLASK_SECRET_KEY=super_secret_key
```

### 4. Initialize the Database
Run the setup script to instantly create the required `users` and `tickets` tables in MariaDB:
```bash
python run_schema.py
```
*(You should see "Database tables created successfully!")*

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:5000` in your web browser.

## 🎯 Next Steps
- Link user accounts directly to the specific tickets they create.
- Setup an Admin Role to securely assign tickets to specific staff members.
- Setup email notifications for ticket updates.
