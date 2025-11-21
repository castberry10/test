# #pip install uvicorn
# #pip install fastapi
# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def a():
#     return {"message": "hello world"}

# @app.get("/abc")
# def abc():
#     return {"message": "abc"}

# # uvicorn simpleserver:app --reload --host 0.0.0.0
# ---------------------------------------
# 봐봐요 개쩔죠 localhost/ 랑 localhost/abc에 들어가게해서 개쉽다는걸 알게하기 
# 
# from fastapi import FastAPI
# app = FastAPI()
# data = []
# @app.get("/")
# def a():
#     return {"message": "hello world"}

# @app.post("/body")
# def ab(aa, bb):
#     return aa

# @app.get("/add")
# def abc():
#     return {"message": "hello world"}

# @app.get("/print")
# def abc():
#     return {"message": "hello world"}
# ---------------------------------
# from fastapi import FastAPI
# app = FastAPI()
# data = []
# @app.get("/")
# def a():
#     return {"message": "hello world"}

# @app.post("/chat")
# def ab(c):
#     data.append(c)
#     return data
# --------------------------------
from fastapi import FastAPI
from fastapi import Body
app = FastAPI()
data = []
@app.get("/")
def a():
    return {"message": "hello world"}

@app.post("/chat")
def ab(chat):
    data.append(chat)
    return data

@app.post("/chat2")
def ab(user: str = Body(...), chat: str = Body(...)):
    data.append(user + ": " + chat)
    return data

@app.post("/chat3")
def ab(user, chat):
    data.append(user + ": " + chat)
    return data