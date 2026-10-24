from pydantic import BaseModel, Field

class Task(BaseModel):
    title: str
    description: str | None = None
    priority: int = Field(ge=1, le=5)
    completed: bool = False