from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="School Library API")


class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    available: bool = True


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    available: bool = True


books = [
    Book(id=1, title="A Wrinkle in Time", author="Madeleine L'Engle"),
    Book(id=2, title="The Giver", author="Lois Lowry", available=False),
]


@app.get("/books")
def list_books():
    """Return every book in the library."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book, or a 404 response when it is not found."""
    pass


@app.post("/books")
def create_book(book_data: BookCreate):
    """Add a book to the library."""
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: BookCreate):
    """Replace the details of an existing book."""
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Remove a book from the library."""
    pass


# Run from this directory with: uvicorn starter-code:app --reload
