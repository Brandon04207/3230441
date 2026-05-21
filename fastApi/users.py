#CREACION DE UN CRUD
from fastapi import FastAPI
#Pyantic: libreria que se usa para validar y manejar datos de manera mas rapida 
# Basemodel: Es la clase que se utiliza para definir modlos de datos, para dar la estructura de la imnformacion.

from pydantic import BaseModel

app = FastAPI()

#MALAS PRACTICAS

@app.get("/usersjson")
async def usersjson():
    return[
     {"name":"pedro","username":"la pampara","url":"https:la pampara.com","age": 40},
     {"name":"luis","username":"el mostro","url":"https:el mostro.com","age": 40},
     {"name":"jose","username":"la bestia","url":"https:la bestia.com","age": 40} 
    ]
    
    
#USANDO CLASES

    class User(BaseModel):
        name: str
        username: str
        url: str
        age: int

use_list=[
    User(name="pedro", username="la pampara", url="https:la pampara.com", age=40),
    User(name="luis", username="el mostro", url="https:el mostro.com", age=40),
    User(name="jose", username="la bestia", url="https:la bestia.com", age=40)
]

@app.get("/usersclass")
async def usersclass():
    return use_list