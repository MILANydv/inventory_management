# Inventory Management Django Project

## Overview

This project is a robust, professional Django-based inventory management system. It follows best practices for code quality, DRY principles, and is designed for performance and maintainability. The authentication system uses JWT (JSON Web Tokens) for secure, scalable API access, and the codebase is structured for easy extension and theming.

## Features

- **User registration & JWT login**
- **CRUD for Category, Product, Supplier, Customer, Order**
- **DRY, robust, and professional code**
- **API-first, ready for responsive frontend**
- **Easily extendable for advanced features (filtering, search, RBAC, etc.)**

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd inventory_management
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you encounter a `ModuleNotFoundError` for `rest_framework_simplejwt`, install it manually:

```bash
pip install djangorestframework-simplejwt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints

### Registration

- **URL:** `/api/auth/register/`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password",
    "password2": "your_password"
  }
  ```
- **Response:** `201 Created` on success

### Login (JWT Token)

- **URL:** `/api/auth/login/`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response:** `200 OK` with `access` and `refresh` tokens

### Token Refresh

- **URL:** `/api/token/refresh/`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "refresh": "<refresh_token>"
  }
  ```
- **Response:** `200 OK` with new `access` token

### Inventory Management

All endpoints require JWT authentication (include `Authorization: Bearer <access_token>` header).

- **Categories:** `/api/inventory/categories/`
- **Suppliers:** `/api/inventory/suppliers/`
- **Customers:** `/api/inventory/customers/`
- **Products:** `/api/inventory/products/`
- **Orders:** `/api/inventory/orders/`

Supports full CRUD (create, list, retrieve, update, delete) via standard REST methods (POST, GET, PUT/PATCH, DELETE).

#### Example: Create a Product

POST `/api/inventory/products/`

```json
{
  "name": "Sample Product",
  "category": 1,
  "supplier": 1,
  "price": 100.0,
  "stock": 50,
  "description": "A sample product."
}
```

#### Example: List Orders

GET `/api/inventory/orders/`

## Project Structure

- `core/` - Main Django project settings and URLs
- `accounts/` - User registration and authentication logic
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Notes

- All API endpoints are designed for easy integration with modern, responsive frontends (React, Vue, mobile, etc.).
- The backend is ready for extension with additional inventory management features.
- For frontend, follow Airbnb's design and UX principles for a professional, responsive, and theme-compatible UI.

## Troubleshooting

- If you see `ModuleNotFoundError: No module named 'rest_framework_simplejwt'`, run `pip install djangorestframework-simplejwt`.
- If you add new dependencies, update `requirements.txt` with `pip freeze > requirements.txt`.

## License

MIT (or your preferred license)
