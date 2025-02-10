import requests
import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = ""  # Enter pixela token
USERNAME = ""  # Enter pixela username
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph config to ask for the amount of pool lengths swum
graph_config = {
    "id": "graph1",
    "name": "Swimming Graph",
    "unit": "pool lengths",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# req1 = requests.post(url=post_graph_endpoint, json=graph_config, headers=headers)
# print(req1.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

current_date = datetime.datetime(year=2024, month=10, day=7).strftime("%Y%m%d")
pixel_body = {
    "date": current_date,
    "quantity": input("How many pool lengths did you swim today?")
}
response = requests.post(url=graph_endpoint, json=pixel_body, headers=headers)
print(response.text)
