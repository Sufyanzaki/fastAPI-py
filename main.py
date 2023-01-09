import uvicorn
from fastapi import FastAPI, Body, Depends
import requests
from app.model import UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT

users = []

app = FastAPI()

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# route handlers

@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

@app.get("/temperature")
def get_temperature(country: str, city: str):
    weather_data = requests.get(f"https://api.weatherbit.io/v2.0/current?city={city}&country={country}&key=49c00ab7edd1404589f58a5d033c7381").json()
    # Extract the temperature from the weather data
    data = weather_data["data"]
    app_temp = data[0]["app_temp"]
    return {"temperature": app_temp}
