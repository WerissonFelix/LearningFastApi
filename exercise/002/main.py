from fastapi import FastAPI, Query, HTTPException
from typing import Annotated


app = FastAPI()

@app.get('/books/')
async def get_book_by_title(
    title: Annotated[str, Query(
        min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9\s-]+$",
        description="The title of the book to search for",
        examples=["Harry Potter", "The-Hobbit"],
    )]
):
    return { "title": title, "message": "Book search successful"}
