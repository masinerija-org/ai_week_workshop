from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse


class User(BaseModel):
    id: int
    name: str = "John Doe"
    friends: List[int] = []


app = FastAPI()

# Example in-memory "database"
fake_users = {
    1: User(id=1, name="Jane", friends=[2, 3]),
    2: User(id=2, name="Alice", friends=[1]),
    3: User(id=3, name="Bob", friends=[1]),
}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id == 4:
        return {"id": "non-integer", "name": None, "friends": None}

    user = fake_users.get(user_id)
    if user:
        return user
    return JSONResponse(status_code=404, content={"detail": "User not found"})
