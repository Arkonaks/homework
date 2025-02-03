from fastapi import FastAPI, status, Body, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

# python -m  uvicorn module_16_5:app

app = FastAPI()

templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_users(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse('users.html', {'request': request, 'user': user})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> User:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="Users was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="Users was not found")
