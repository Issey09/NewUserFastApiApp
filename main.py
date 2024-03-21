from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel


app =  FastAPI()

class NewUser(BaseModel):
    nick_name: str
    age: int
    GPS: int | None = None

task = []





@app.get('/user/')
def create_user(new: Annotated[NewUser, Depends()]):
    task.append({'nick': new.nick_name,'age': new.age, 'gps': new.GPS})
    return 'Пользователь зарегистрирован'
@app.post('/user/')
async def user():
    return task