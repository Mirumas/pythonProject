from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"ФИО": "Бобошко Илья Павлович"}

@app.get('/users')
async def f_index():
    return {"Телефон": "8-923-792-95-10"}

@app.get('/tools')
async def f_index():
    return {"Навыки разработчика": "делал лабораторные в университете"}
