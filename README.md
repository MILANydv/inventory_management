# Inventory Management Django Project

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/MILANydv/inventory_management.git)

---

> **Educational Use Only**
>
> This project is provided for educational purposes for students of **PCPS, Patan College For Professional Studies**.
>
> - **Address:** 162, Patan 44700 Kupondole Rd, Lalitpur 44700
> - **Website:** [patancollege.edu.np](https://patancollege.edu.np)
>
> Please use this repository as a learning resource. Do not use in production environments.

---

## Assignment Instructions for Students

1. **Fork this repository** to your own GitHub account using the GitHub web interface.
2. **Clone your forked repository** to your local machine.
3. **Complete the remaining routes** or any additional features as assigned by your instructor.
4. **Commit and push your changes** to your forked repository.
5. **Submit your repository link** as per your instructor's instructions.

---

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
git clone https://github.com/MILANydv/inventory_management.git
cd inventory_management
```

### 2. Create and Activate Virtual Environment

#### On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows (CMD):

```cmd
python -m venv venv
venv\Scripts\activate
```

#### On Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you encounter a `ModuleNotFoundError` for `rest_framework_simplejwt` or `drf_yasg`, install them manually:

```bash
pip install djangorestframework-simplejwt drf-yasg
```

Then update your requirements:

```bash
pip freeze > requirements.txt
```

### 4. Update Django Settings

Add `'drf_yasg'` to your `INSTALLED_APPS` in `core/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'drf_yasg',
]
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server (with venv activated)

```bash
source venv/bin/activate
python manage.py runserver
```

The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 7. API Documentation (Swagger UI)

After starting the server, access the interactive API docs at:

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## API Endpoints

Below is a summary of all available API routes. All inventory endpoints require JWT authentication (use the login endpoint to obtain a token).

| Resource      | Method | Path                            | Description                          |
| ------------- | ------ | ------------------------------- | ------------------------------------ |
| Register      | POST   | /api/auth/register/             | Register a new user                  |
| Login         | POST   | /api/auth/login/                | Obtain JWT access and refresh tokens |
| Token Refresh | POST   | /api/token/refresh/             | Refresh JWT access token             |
| Categories    | GET    | /api/inventory/categories/      | List all categories                  |
| Categories    | POST   | /api/inventory/categories/      | Create a new category                |
| Categories    | GET    | /api/inventory/categories/{id}/ | Retrieve a category by ID            |
| Categories    | PUT    | /api/inventory/categories/{id}/ | Update a category by ID              |
| Categories    | PATCH  | /api/inventory/categories/{id}/ | Partially update a category by ID    |
| Categories    | DELETE | /api/inventory/categories/{id}/ | Delete a category by ID              |
| Suppliers     | GET    | /api/inventory/suppliers/       | List all suppliers                   |
| Suppliers     | POST   | /api/inventory/suppliers/       | Create a new supplier                |
| Suppliers     | GET    | /api/inventory/suppliers/{id}/  | Retrieve a supplier by ID            |
| Suppliers     | PUT    | /api/inventory/suppliers/{id}/  | Update a supplier by ID              |
| Suppliers     | PATCH  | /api/inventory/suppliers/{id}/  | Partially update a supplier by ID    |
| Suppliers     | DELETE | /api/inventory/suppliers/{id}/  | Delete a supplier by ID              |
| Customers     | GET    | /api/inventory/customers/       | List all customers                   |
| Customers     | POST   | /api/inventory/customers/       | Create a new customer                |
| Customers     | GET    | /api/inventory/customers/{id}/  | Retrieve a customer by ID            |
| Customers     | PUT    | /api/inventory/customers/{id}/  | Update a customer by ID              |
| Customers     | PATCH  | /api/inventory/customers/{id}/  | Partially update a customer by ID    |
| Customers     | DELETE | /api/inventory/customers/{id}/  | Delete a customer by ID              |
| Products      | GET    | /api/inventory/products/        | List all products                    |
| Products      | POST   | /api/inventory/products/        | Create a new product                 |
| Products      | GET    | /api/inventory/products/{id}/   | Retrieve a product by ID             |
| Products      | PUT    | /api/inventory/products/{id}/   | Update a product by ID               |
| Products      | PATCH  | /api/inventory/products/{id}/   | Partially update a product by ID     |
| Products      | DELETE | /api/inventory/products/{id}/   | Delete a product by ID               |
| Orders        | GET    | /api/inventory/orders/          | List all orders                      |
| Orders        | POST   | /api/inventory/orders/          | Create a new order                   |
| Orders        | GET    | /api/inventory/orders/{id}/     | Retrieve an order by ID              |
| Orders        | PUT    | /api/inventory/orders/{id}/     | Update an order by ID                |
| Orders        | PATCH  | /api/inventory/orders/{id}/     | Partially update an order by ID      |
| Orders        | DELETE | /api/inventory/orders/{id}/     | Delete an order by ID                |

> Replace `{id}` with the actual resource ID.

## Project Structure

- `core/` - Main Django project settings and URLs
- `accounts/` - User registration and authentication logic
- `inventory/` - Inventory management logic (categories, products, suppliers, customers, orders)
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Notes

- All API endpoints are designed for easy integration with modern, responsive frontends (React, Vue, mobile, etc.).
- The backend is ready for extension with additional inventory management features.
- For frontend, follow Airbnb's design and UX principles for a professional, responsive, and theme-compatible UI.
- Use the provided Postman collection for quick API testing, including JWT token handling and all major endpoints.

## Troubleshooting

- If you see `ModuleNotFoundError: No module named 'rest_framework_simplejwt'` or `No module named 'drf_yasg'`, run `pip install djangorestframework-simplejwt drf-yasg`.
- If you add new dependencies, update `requirements.txt` with `pip freeze > requirements.txt`.
- If Swagger UI at `/swagger/` fails, ensure `'drf_yasg'` is in `INSTALLED_APPS` and the package is installed in your venv.

### API Documentation (Swagger & Redoc)

- **Swagger UI** ([http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)) provides an interactive, try-it-out interface for all endpoints. You can authorize with your JWT token and test all API calls directly from the browser.
- **Redoc** ([http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)) offers a clean, readable reference for all endpoints, models, and parameters.

**Usage Tips:**

- Use Swagger UI to explore, test, and debug your API interactively.
- Use Redoc for a quick, professional reference of all endpoints and data models.
- Both docs update automatically as you change your API code.

### Postman Collection

A ready-to-use Postman collection (`postman_collection.json`) is included for quick API testing. It covers all major endpoints and automatically handles JWT token storage after login.


