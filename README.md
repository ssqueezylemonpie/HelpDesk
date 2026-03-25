# Helpdesk Application

A lightweight Helpdesk ticketing system built with **Flask (Python)**, **MariaDB**, **HTML**, and **Vanilla CSS**.

## Features
- **Ticket Management**: Create, view, and update support tickets.
- **Status Tracking**: Keep track of tickets with statuses like *Open*, *In Progress*, and *Closed*.
- **User Dashboard**: See all active and past tickets at a glance.
- **Responsive UI**: A clean, modern interface styled with vanilla CSS.

## Prerequisites
Before running the application, make sure you have the following installed:
- [Python 3.x](https://www.python.org/)
- [MariaDB](https://mariadb.org/)
- pip (Python package manager)

## Project Structure
```text
Helpdesk/
│
├── app.py                 # Main Flask application and routes
├── database.py            # Database connection setup
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (DB credentials)
├── README.md              # Project documentation
│
├── static/                # Static assets
│   ├── css/
│   │   └── style.css      # Vanilla CSS styles
│   └── images/            # Image assets
│
└── templates/             # HTML templates
    ├── base.html          # Base layout template
    ├── index.html         # Dashboard / Ticket list
    ├── create_ticket.html # Form to submit a new ticket
    └── view_ticket.html   # Detailed view of a single ticket
```

## Setup Instructions

### 1. Database Configuration
1. Log in to your MariaDB console:
   ```bash
   mariadb -u root -p
   ```
2. Create the database for the helpdesk:
   ```sql
   CREATE DATABASE helpdesk_db;
   ```
3. *(Optional)* Create a specific user for the application:
   ```sql
   CREATE USER 'helpdesk_user'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON helpdesk_db.* TO 'helpdesk_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

### 2. Environment Setup
1. Clone this repository (or navigate to the project directory).
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`
4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Application Configuration
Create a `.env` file in the root of the project with your database credentials:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=helpdesk_db
FLASK_SECRET_KEY=super_secret_key
```

### 4. Initialize the Database
Run the setup script (if provided) or manually run the SQL schema to create the necessary tables for `users` and `tickets`:
```bash
python run_schema.py
```
*(Alternatively, you can add commands here based on how you initialize your database).*

### 5. Run the Application
Start the Flask development server:
```bash
flask run
```
or
```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:5000` in your web browser.

## Next Steps
- Implement user authentication (Login/Register).
- Add functionality for administrators to assign tickets to specific staff members.
- Setup email notifications for ticket updates.

---
