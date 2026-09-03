# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing a school library using the FastAPI framework. You will practice HTTP methods, path parameters, JSON request bodies, Pydantic validation, and the interactive API documentation FastAPI generates automatically.

## 📝 Tasks

### 🛠️ Create the API and Read Endpoints

#### Description

Use the provided starter code to create a FastAPI application that exposes a collection of library books. Start the application with Uvicorn and implement endpoints for listing all books and retrieving one book by its ID.

#### Requirements

Completed program should:

- Create a FastAPI application instance
- Define a `Book` model with an integer ID, title, author, and availability status
- Return all books from `GET /books`
- Return one matching book from `GET /books/{book_id}`
- Return a `404` response when a requested book ID does not exist
- Show the endpoints in FastAPI's generated documentation at `/docs`


### 🛠️ Add Create, Update, and Delete Operations

#### Description

Extend the API so library staff can manage the collection. Use request-body models to validate incoming JSON data and return useful HTTP status codes for successful and unsuccessful operations.

#### Requirements

Completed program should:

- Add a new book with `POST /books` and return the created book
- Reject invalid book data, such as an empty title or author, with validation errors
- Update an existing book with `PUT /books/{book_id}`
- Remove an existing book with `DELETE /books/{book_id}`
- Return a `404` response when update or delete requests use an unknown book ID
- Preserve the existing books while the application is running

Example request for `POST /books`:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "available": true
}
```


### 🛠️ Test and Improve the API

#### Description

Use the interactive `/docs` page or an HTTP client to test every route. Add one useful feature that makes the library API easier to use, then document how a user can run and test your application.

#### Requirements

Completed program should:

- Test at least one successful and one failing request for each route
- Add one improvement, such as filtering books by author or searching titles
- Include clear response messages for operations that change or remove data
- Add a short run instruction comment or section explaining the Uvicorn command
- Demonstrate the API with at least three example requests and their expected results
