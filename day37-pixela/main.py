import requests
import datetime as dt
USERNAME = 'bomikim'
TOKEN = "dkjlkwperwoeorio3040wjk"
graphID = "graph1"
pixela_endpoint = 'https://pixe.la/v1/users'

user_params ={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"

}
# res = requests.post(pixela_endpoint, json=user_params)

# print(res.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":graphID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url=graph_endpoint, json=graph_params, headers=headers )


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"

today = dt.datetime.now()
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "9.74"
}

update_endpoint = f"{pixel_creation_endpoint}/{today.strftime("%Y%m%d")}"
res = requests.delete(url=update_endpoint, json=pixel_data, headers=headers)
print(res)
# res = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
