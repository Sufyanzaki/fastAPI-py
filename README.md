# fastAPI-py
 FASTAPI jwt authentication weather app

in my case i have installed python3.11, python 2.x - python 3.6 might not support the this code

install all the dependencies from requirments.txt as => python3 -m pip install -r requirements.txt

some other dependencies are => python3 -m pip install requests

activate ther server with => python3.11 -m uvicorn main:app --reload

default server running at host => http://127.0.0.1:8000/

dynamic API docs by OPENAPI avaliable at host => http://127.0.0.1:8000/docs

main.py containing api routes

model.py containing prototype of database model schemas

auth_handler containing decoding, encoding, returning jwt token

When doing import jwt it is importing the library JWT as opposed to PyJWT - the latter is the one you want for encoding. I did python3 -m pip uninstall JWT and python3 -m pip uninstall PyJWT then python3 -m pip install -r requirements.txt
