import requests
import datetime
headers = {
    "x-app-id": "", # Enter app id
    "x-app-key": "" # Enter app key
}
body = {
    "query": input("What exercise did you do?"),
}

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_url, headers=headers, json=body)
print(response)
print(response.json())
response_data = response.json()["exercises"][0]

today = datetime.datetime.today().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%X")

google_sheet_url = "https://api.sheety.co/ enter your link"
google_sheet_body = {
    "workout": {
            "date": today,
            "time": current_time,
            "exercise": response_data["name"].title(),
            "duration": response_data["duration_min"],
            "calories": response_data["nf_calories"]
        }
}
response_2 = requests.post(url=google_sheet_url, json=google_sheet_body)
print(response_2)
print(response_2.json())
print(response_2.text)
