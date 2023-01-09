# fastAPI-py
 FASTAPI jwt authentication weather app

in my case i have installed python3.11, python 2.x - python 3.6 might not support the this code

install all the dependencies from requirments.txt as => python3 -m pip install -r requirements.txt

some other dependencies are => python3.11 -m pip install requests
python3.11 -m pip install python-decouple
python3.11 -m pip install jwt

activate ther server with => python3 -m uvicorn main:app --reload

default server running at host => http://127.0.0.1:8000/

dynamic API docs by OPENAPI avaliable at host => http://127.0.0.1:8000/docs

main.py containing api routes

model.py containing prototype of database model schemas

auth_handler containing decoding, encoding, returning jwt token
