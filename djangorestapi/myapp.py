import requests, json

# URL = "http://127.0.0.1:8000/createclient"
# data = {
#     'client_name':'Nimap',
#     'created_at':'2024-09-27',
#     'created_by':'Rohit'
# }
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data = r.json()
# print(data)

# URL = "http://127.0.0.1:8000/createproject"
# data = {
#     'project_name':'Hiring System',
#     'client': '11',
#     'users': 'Shree Jadhav',
#     'created_at': '',
#     'created_by': 'Shivam'
#
# }
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data = r.json()
# print(data)

##############################################################

URL = "http://127.0.0.1:8000/register"
data = {
    'username': 'shreejadhav@gmail.com',
    'password': '7448293236',
    'email': 'shreejadhav@gmail.com',
    'first_name': 'shreekant',
    'last_name': 'jadhav'

}
json_data = json.dumps(data)

r = requests.post(url=URL, json=data)
data = r.json()
print(data)

########################################################################################

# r = requests.post(url=URL, json=data)  # Correctly pass JSON data
#
# try:
#     # Try to parse the JSON response
#     response_data = r.json()
#     print(response_data)
# except requests.exceptions.JSONDecodeError:
#     # Handle case when response is not JSON
#     print(response_data)



# URL = "http://127.0.0.1:8000/project_details"
# r = requests.get(url=URL)
# data = r.json()
# print(data)

# URL = "http://127.0.0.1:8000/project_details"
# r = requests.get(url=URL)
# data = r.json()
# print(data)