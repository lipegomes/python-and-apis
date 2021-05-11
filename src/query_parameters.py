import requests

response1 = requests.get("https://randomuser.me/api/").json()
print(f"{response1}\n")

response2 = requests.get("https://randomuser.me/api/?gender=male").json()
print(f"{response2}\n")

query_params_1 = {"gender": "male", "nat": "br"}
endpoint_1 = "https://randomuser.me/api"
print(f'{requests.get(endpoint_1, params=query_params_1).json()}\n')

query_params_2 = {"q": "labradoodle"}
endpoint_2 = "https://api.thedogapi.com/v1/breeds/search"
print(requests.get(endpoint_2, params=query_params_2).json())
