# import requests


# def test():
#     r = requests.get("https://naver.com" + "/")
#     return r.headers

# print(test())

import requests
import json

API_KEY = ""

url = "https://api.openai.com/v1/responses"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4o-mini",
    "input": "안녕 반가워"
}

res = requests.post(url, headers=headers, json=payload)
data = res.json()

print(data["output"][0]["content"][0]["text"])
