# Mechanic Shop API with Documentation and Testing

This project focuses on Backend specialization in database design and development. It involves building a Mechanic Shop API with Documentation and Testing with Flask, SQLAlchemy, Marshmallow, and MySQL. The project is developed using Python frameworks and functional programming concepts.

- Follow the file structure below to build the Mechanic Shop Advanced API using the Application Factory Pattern.

### Project Structure

##File Layout of a Mechanic Shop Advanced API using the Application Factory Pattern

/project
├
├── /application
├ ├
├ ├
│ ├── **init**.py - create_app() lives here
│ ├── extensions.py <--- Where we will initialize 3rd party extensions
│ │
│ │
│ │
│ ├── /blueprints
│ ├ ├──/customer
│ ├ ├──**init**.py - Initialize Customer Blueprint
│ ├ ├── routes.py - Create Customer Controllers/routes
├ │ └── schemas.py
│ │
│ │
│ ├── /static <--- New Folder
│ │ │
│ │ └── swagger.yaml <--- New File
│ │
├ │
├ ├── /utils # <--- New Folder
│ │ └── util.py #<--- File for token functions  
│ ├
├ ├
├ └── models.py
├
│  
├── tests/ <--- New Folder
│ │
│ └── test_customers.py <--- New File
│ ├── test_mechanics.py
│ ├── test_service_tickets.py
│ └── test_inventories.py
│
│
├── app.py
└── config.py

- There are three major components to this application:

  - Models
  - Schemas
  - API Routes

- This advanced API project requires additional production-level protections to securely access its API endpoints.

## Security and Optimization Concepts Implemented

### Rate Limiting and Caching:

    - Protects the API from abuse by limiting the number of requests a client can make in a given period, and speeds up response time by caching frequent requests.
    - Protect against excessive traffic with rate limiting
    - Faster response using caching strategies

### Token Authentication:

    - Ensures that only authorized users or services can access protected API routes by using JSON Web Tokens (JWT) or similar secure tokens.
    - Secure API endpoints using token-based authentication

### Advanced Queries:

    - Allows clients to perform flexible and complex data retrieval operations, such as filtering, sorting, and pagination.
    - Support for advanced queries: filtering, sorting, and pagination

### Utilizing Junction Tables with Additional Fields

    - Defining a Model for the Junction Table: This method involves creating a full model for the junction table, allowing for additional fields and more complex relationships.
    - Complex Many-to-Many Relationships: When you need to store additional data in the junction table, such as metadata or extra attributes.

### API Documentation with Swagger UI

    - Create in API documentation is like a user manual for developers, guiding them through the ins and outs of an API Using with Swagger
    - install --> pip install flask-swagger flask_swagger_ui
    - Added Swagger UI Integration
    - The API documentation is written in OpenAPI format and located at:
      - http://127.0.0.1:5000/api/docs/static/swagger.yaml
    - This file describes all endpoints, methods, schemas, request bodies, and expected responses.

## Unit Testing

- All critical routes are covered with automated unit tests using Python's built-in `unittest`.
- Test-Driven Development (TDD) is a software development approach where tests are written before the code is implemented.
- Test-Driven Development (TDD) principles applied to REST API development, ensuring that code is thoroughly tested before being implemented.
- Red Phase: Write a failing test
- Green Phase: Write just enough code to pass
- Refactoring Phase: Improve code while keeping tests green

#### Test Setup:

- Create a `/tests` folder in the project root
- Covered Test Modules:

  - `test_customers.py` – Auth + CRUD
  - `test_mechanics.py` – Mechanic endpoints
  - `test_service_tickets.py` – Ticket creation, assign, retrieve, delete
  - `test_inventories.py` – Inventory endpoints

## To Run the project:

- Open the terminal and navigate to the project directory

- Set the appropriate path if needed

- Install all dependencies:

  ```To terminal
  --> pip install -r requirements.txt.

  ```

- Ensure your main file is named app.py.

- Database models for customers, mechanics, service_tickets, inventories and mechanic_services, service_inventory association.

- Validated and serialized data using Marshmallow schemas.

- Once save the file to Open the terminal to running the application: py app.py

- Fully functional CRUD endpoints for customers, mechanics, and service_tickets, inventories and testing the each of API endpoints use the Postman.

- Authentication Note:

  - To access protected routes, clients must include a valid JWT token in the request header

  - API Usage with Postman

  - For protected routes, include your JWT token: Authorization: Bearer <your_token_here>

- All required tables will be created in MySQL.

- The application’s endpoints are fully functional and can be tested using Postman. All data is stored in a MySQL database.

- How to run the Swagger:

  - After successfully testing all the API endpoints in Postman, create the API documentation using YAML format.
  - Set up Swagger in app/**init**.py to access documentation and test APIs.
  - Once all is created, save the "Swagger.yaml" file and run: py app.py

  - Open your browser and visit: http://127.0.0.1:5000/api/docs/
  - The API is running on your localhost 127.0.0.1:5000
  - Then endpoint that renders your documentation is /api/docs
  - You can view it by integrating with Swagger UI using /static/swagger.yaml

- How to run Unittest:

  - Running Tests:
    in terminal, run all test files: - python -m unittest discover tests
    Or run a specific test file: - python -m unittest tests.test_customers
