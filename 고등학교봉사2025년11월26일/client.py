# python .\client.py
# import requests

# BASE = "http://127.0.0.1:8000"

# def test():
#     r = requests.get(BASE + "/")
#     return r.json()

# print(test())
#============================
# import requests

# BASE = "http://127.0.0.1:8000"
# user = input("당신의 이름은 무엇인가요? ")

# def test():
#     r = requests.get(BASE + "/")
#     return r.json()

# def chat(user, chat):
#     r = requests.post(BASE + "/chat2", json={"user": user, "chat": chat})
#     return r.json()

# while True:
#     message = input("메시지를 입력하세요: ")
#     response = chat(user, message)
#     print("채팅 기록:")
#     print(response)
import requests

BASE = "http://127.0.0.1:8000"
user = input("당신의 이름은 무엇인가요? ")

def test():
    r = requests.get(BASE + "/")
    return r.json()

def chat(user, chat):
    r = requests.post(BASE + "/chat3",params={"user": user, "chat": chat})
    return r.json()

while True:
    message = input("메시지를 입력하세요: ")
    response = chat(user, message)
    print("채팅 기록:")
    print(response)