from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return f'Главная страница'

@app.get("/user")
async def info_user(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

@app.get("/user/admin")
async def admin():
    return f'Вы вошли как администратор'

@app.get("/user/{user_id}")
async def user(user_id: int):
    return f'Вы вошли как пользователь №{user_id}'

