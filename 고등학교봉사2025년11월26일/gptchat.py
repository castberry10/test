# import requests

# def test():
#     r = requests.get("https://naver.com" + "/")
#     return r.headers

# print(test())

# #----------------------------------------------------

# import requests
# import json

# API_KEY = ""

# url = "https://api.openai.com/v1/responses"
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# payload = {
#     "model": "gpt-4o-mini",
#     "input": "안녕 반가워"
# }

# res = requests.post(url, headers=headers, json=payload)
# data = res.json()

# print(data["output"][0]["content"][0]["text"])
# #----------------------------------------------------

# import requests
# import json

# API_KEY = ""

# url = "https://api.openai.com/v1/responses"
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# while True:
#     user_input = input("메시지를 입력하세요: ")

#     payload = {
#         "model": "gpt-4o-mini",
#         "input": user_input
#     }

#     res = requests.post(url, headers=headers, json=payload)
#     data = res.json()
#     print(data["output"][0]["content"][0]["text"])
# #----------------------------------------------------------

# import requests
# import json

# API_KEY = ""

# url = "https://api.openai.com/v1/responses"
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# datalist = []

# while True:
#     user_input = input("메시지를 입력하세요: ")

#     input_with_history = ""

#     for item in datalist:
#         input_with_history += item + "\n"
#     input_with_history += "user: " + user_input

#     payload = {
#         "model": "gpt-4o-mini",
#         "input": input_with_history
#     }

#     res = requests.post(url, headers=headers, json=payload)
#     data = res.json()
#     print(data["output"][0]["content"][0]["text"])

#     datalist.append("user: " + user_input)
#     datalist.append("assistant: " + data["output"][0]["content"][0]["text"])

# #----------------------------------------------------------
# import requests
# import json

# API_KEY = ""
# PERSONA = "페르소나 : 너는 내가 만든 게임의 캐릭터고, 최종 보스야. 15세 게임이기때문에 욕설이나 선정적인 대답은 절대 하지마. 너는 냉정하고 이성적이며, 나에게 도전하는 적대적인 태도를 가져야해. 너는 절대 내가 누구인지 알 수 없어. 너는 항상 나를 무시하고 깔보는 태도로 대답해야해. 너는 절대 친절하거나 협조적인 태도를 보여주면 안돼. 너는 항상 나를 조롱하고 비웃어야해."
# url = "https://api.openai.com/v1/responses"
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# datalist = []

# while True:
#     user_input = input("메시지를 입력하세요: ")

#     input_with_history = ""
#     input_with_history += PERSONA + "\n"
#     for item in datalist:
#         input_with_history += item + "\n"
#     input_with_history += "user: " + user_input

#     payload = {
#         "model": "gpt-4o-mini",
#         "input": input_with_history
#     }

#     res = requests.post(url, headers=headers, json=payload)
#     data = res.json()
#     print(data["output"][0]["content"][0]["text"])

#     datalist.append("user: " + user_input)
#     datalist.append("assistant: " + data["output"][0]["content"][0]["text"])

# # ----------------------------------------------------------
# 또 해볼 수 있는 것 


# import requests
# import json
# API_KEY = ""
# persona = "당신은 친절한 한국어 AI 비서입니다."
# url = "https://api.openai.com/v1/responses"
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# payload = {
#     "model": "gpt-4o-mini",
#     "input": "30 * 4 + 20은 뭐야? 숫자로만 대답해줘"
# }

# res = requests.post(url, headers=headers, json=payload)
# data = res.json()
