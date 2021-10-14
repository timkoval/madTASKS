# Doctors and Clients 
"/patients/id"
#id, date of birth, diagnosis, date of creation, jwt

from fastapi import FastAPI, Body, Depends
import databases

from .schemas import PatientSchema, UserSchema, UserLoginSchema
from .auth.auth_bearer import JWTBearer
from .auth.auth_handler import signJWT

from datetime import date, datetime

posts = [
    {
        "id": 1,
        "date_of_birth": "2000-02-22",
        "diagnoses": ("one", "two", "three"),
        "created_at": datetime.now()
    },
        {
        "id": 1,
        "date_of_birth": "2000-03-05",
        "diagnoses": ("one", "two", "three"),
        "created_at": datetime.now()
    },
        {
        "id": 1,
        "date_of_birth": "2111-03-22",
        "diagnoses": ("one", "two", "three"),
        "created_at": datetime.now()
    }
]

users = []

app = FastAPI()

SQLALCHEMY_DATABASE_URL = (
    "sqlite:///test_task.db"
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# @app.get("/clients")
# async def read_clients():
#     query = "SELECT * FROM patients"
#     return await database.fetch_all(query)


# helpers

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.get("/patients", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def get_posts() -> dict:
    return { "data": posts }

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) 
    return signJWT(user.email)

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }