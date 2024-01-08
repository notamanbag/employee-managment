# Employee Management System

## Overview

The Employee Management System is a web-based application designed to streamline and simplify the process of managing employees within an organization. It provides a centralized platform for HR administrators to efficiently handle employee-related tasks, maintain records, and facilitate communication.

## Features

1. **User Authentication:** Secure user authentication for administrators and employees.

2. **Employee Profiles:** Store and manage detailed profiles for each employee, including personal information, contact details, and job-related details.

3. **Role-Based Access Control:** Different user roles (Admin, HR, Manager, Employee) with varying levels of access to system functionalities..

5. **Leave Management:** Efficiently handle leave requests, approvals, and track employee leave balances.

6. **Task Assignment:** Assign tasks to employees, set deadlines, and track task progress.


8. **Salary and Benefits:** Manage salary information, bonuses, and other benefits for employees.

9. **Reports and Analytics:** Generate reports on employee performance, attendance, and other relevant metrics.

## Technologies Used

- **Frontend:**ReactJS ,MaterialUi
- **Backend:** Python, Django Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Version Control:** Git

## Getting Started

1. Clone the repository:

2. Install dependencies:

    ```bash
    cd employee-management
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at [http://localhost:8000](http://localhost:8000) and log in with the superuser credentials.


