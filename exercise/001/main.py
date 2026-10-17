from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    published: int = Field(gt=0)
    pages: int = Field(gt=0)
    
books = {
    1: {
        "id": 1,
        "title": "Dom Casmurro",
        "author": "Machado de Assis",
        "published": 1899,
        "pages": 256
    },
    2: {
        "id": 2,
        "title": "O Alienista",
        "author": "Machado de Assis",
        "published": 1882,
        "pages": 96
    },
    3: {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "published": 1949,
        "pages": 328
    }
}

# 1. Path parameter

@app.get('/books/{book_id}')
async def get_book_by_id(book_id: int):
    if book_id in books.keys():
        return {"book's info ": books[book_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# 2. Query parameter

@app.get('/books/')
async def get_book_by_info(
    author: str | None = None, published: int | None = None,
    limit: int = 10
    ):
    
    books_author_published = [ 
        v for v in books.values()
        if (author is None or v['author'] == author) \
        and (published is None or v['published'] == published)
    ]
       
    return books_author_published[:limit]   
       
@app.post('/books')
async def create_book(book: BookCreate):
    ID = max(books.keys(), default=0) + 1
    books[ID] = {'id': ID, **book.model_dump()}
    
    return  books[ID]