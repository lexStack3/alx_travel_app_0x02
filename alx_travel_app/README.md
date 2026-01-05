# ALX Travel Booking App

## Project Overview
This project is a **Django-based Travel Booking Application** that allows users to browse listings, make bookings, and pay securely using the **Chapa Payment Gateway**. The app also uses **Celery** for background email notifications after successful payments.

The workflow simulates real-world booking and payment scenarios, covering:
- Payment initiation and verification
- Booking confirmation
- Automated confirmation emails
This project aligns with industry standards in backend development for fintech travel, and e-commerce applications.

## Features
- User registration and authentication
- CRUD operations for travel listings and bookings
- Booking payment via **Chapa Payment Gateway**
- Payment status tracking and logging
- Asynchronous email notifications with **Celery**
- Swagger and Redoc API documentation

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Databsae**: MySQL
- **Payment Gateway**: Chapa
- **Asynchronous Tasks**: Celery + Redis
- **API Documentation**: Swagger & Redoc

## Installation & Setup
1. **Clone the repository**
```bash
git clone https://github.com/lexStack3/alx_travel_app_0x02.git
cd alx_travel_app_0x002
```
2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```
3. **Install dependencies
```bash
pip install -r alx_travel_app/requirements.txt
```

## Environment Variables
Create a `.env` file in the root or set in your system:
```bash
DJANGO_SECRET_KEY=<your-django-secret-key>
CHAPA_SCRETE_KEY=<your-chapa-secret-key>

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=<your-mysql-password>
MYSQL_PASSWORD=<your-mysql-password>
MYSQL_DB=alx_travel_app_db
```

## Database Setup
1. Ensure MySQL is running:
```bash
sudo systemctl start mysql # Linux
```
2. Login as `root`:
```mysql
sudo mysql
```
3. Create the database:
```mysql
CERATE DATABASE IF NOT EXISTS `alx_travel_app_db`;
```
4. Create a your app user and grant privileges
```mysql
CREATE USER 'app_mgr'@'localhost' IDENTIFIED BY 'sTrOnGpA$$wOrD';
GRANT ALL PRIVILEGES ON alx_travel_app_db.* TO 'app_mgr'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
5. Apply migrations:
```bash
python3 manage.py migrate
```

## Running the Application
1. Start Django server:
```bash
python3 manage.py runserver
```
2. Access API documentation:
  - **Swagger**: `http://127.0.0.1:8000/api/swagger/`
  - **Redoc**: `http://127.0.0.1:8000/api/redoc/`

## Celery & Email
1. Make sure Redis is running
```bash
sudo systemctl start redis
```
2. Start celery worker:
```bash
celery -A alx_travel_app worker -l info
```

## API Endpoints
- **Listings**
  - `GET /api/listing/` - List all travel listings
  - `POST /api/listing/` - Create a new listing

- **Bookings**
  - `GET /api/booking/` - List all bookings
  - `POST /api/booking/` - Create a new booking

- **Reviews**
  - `GET /api/review/` - List all reviews
  - `POST /api/review/` - Add a review

- **Payments**
  - `POST /api/payments/initiate/<booking_id>/` - Initiate Chapa payment
  - `GET /api/payments/verify/?tx_ref=<tx_ref>` - Verify payment after completion

  ## License
  This project is licensed under the MIT License.
