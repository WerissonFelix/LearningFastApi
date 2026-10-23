from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

'''
{
  "name": "Summer Offer",
  "description": "A special offer for developers",
  "price": 199.99,
  "items": [
    {
      "name": "Programming Kit",
      "description": "Everything you need to start coding",
      "price": 149.99,
      "tax": 10.5,
      "tags": ["python", "programming", "python"],
      "images": [
        {
          "url": "https://example.com/images/keyboard.jpg",
          "name": "Programming Keyboard"
        },
        {
          "url": "https://example.com/images/mouse.jpg",
          "name": "Gaming Mouse"
        }
      ]
    },
    {
      "name": "Notebook",
      "description": null,
      "price": 49.99,
      "tags": ["stationery", "office"],
      "images": null
    }
  ]
}
''' 