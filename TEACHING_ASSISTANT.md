# Teaching Assistant Guide: Inventory Management Django Project

## Purpose

This project is designed for educational use at PCPS, Patan College For Professional Studies. It provides a robust, real-world Django REST API for teaching web development, API design, authentication, and best practices.

---

## Main Functions of the Project

- **User Registration & JWT Authentication**: Secure user management and login using industry-standard JWT.
- **CRUD Operations**: Full create, read, update, and delete for Categories, Products, Suppliers, Customers, and Orders.
- **API Documentation**: Interactive Swagger UI and Redoc for exploring and testing endpoints.
- **Filtering & Searching**: Built-in support for filtering and searching on list endpoints.
- **Postman Collection**: Ready-to-use for API testing and demonstration.
- **Comprehensive Tests**: Example tests for registration, authentication, and all CRUD operations.

---

## How to Use for Teaching

1. **Demonstrate Setup**: Walk students through cloning, setting up the venv, installing dependencies, and running the server.
2. **Explore API Docs**: Use Swagger UI and Redoc to show endpoints, models, and try out requests live.
3. **Show Authentication Flow**: Register a user, log in, and use the JWT token for protected endpoints.
4. **CRUD Examples**: Demonstrate creating, listing, updating, and deleting each resource.
5. **Testing**: Run the test suite and explain the importance of automated testing.
6. **Assignments**: Ask students to extend the API (e.g., add new fields, endpoints, or business logic) and write their own tests.

---

## Assessment Tips

- **Code Quality**: Check for DRY, clean, and well-commented code.
- **API Functionality**: Test all CRUD endpoints and authentication.
- **Documentation**: Ensure students update the README and add docstrings/comments.
- **Testing**: Require students to write and pass tests for any new features.
- **Git Usage**: Review commit history for regular, meaningful commits.
- **Presentation**: Ask students to present their work, explaining design choices and demonstrating API usage.

---

## Best Practices for Instructors

- Encourage students to use virtual environments and requirements files.
- Promote the use of API documentation (Swagger/Redoc) for self-discovery.
- Emphasize security (e.g., never commit secrets, use JWT properly).
- Foster collaboration: use GitHub issues, pull requests, and code reviews.
- Provide feedback on both code and documentation.
- Use the provided Postman collection for quick grading and demonstration.

---

## Additional Resources

- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [drf-yasg (Swagger) Docs](https://drf-yasg.readthedocs.io/en/stable/)
- [JWT Auth Docs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [PCPS College Website](https://patancollege.edu.np)

---

**This guide is intended to help instructors maximize the educational value of this project. For questions or suggestions, please contact the project maintainer or your academic coordinator.**

---

## Major Tools & Functions to Prepare/Demonstrate in Class

- **Python 3.x**: Ensure all students have Python installed and understand basic usage.
- **Django & Django REST Framework**: Demonstrate project structure, app creation, and REST API concepts.
- **Virtual Environments (venv)**: Show how to create, activate, and use venv for dependency management.
- **Postman**: Use for API testing, demonstrating requests, authentication, and CRUD operations.
- **Swagger UI & Redoc**: Guide students in using interactive API docs for exploration and testing.
- **Git & GitHub**: Teach version control basics, forking, cloning, committing, pushing, and pull requests.
- **Code Editor (VS Code, PyCharm, etc.)**: Recommend a modern editor with Python/Django support.
- **Database Browser (optional)**: Tools like DB Browser for SQLite to inspect the database directly.
- **Testing Framework**: Show how to run and write tests using Django's test runner and APITestCase.

**Key Functions to Demonstrate:**

- User registration and login (JWT flow)
- Making authenticated API requests
- CRUD operations for all resources
- Filtering, searching, and pagination in API
- Running and interpreting test results
- Using API documentation for self-learning
- Collaborating via GitHub (issues, PRs, code review)

---
