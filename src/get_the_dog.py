import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/1")

print(f"{response.headers.get('Content-Type')}\n")

print(f"{response.json()}\n")

print(f"{response.json()['origin']}\n")

print(f"{response.json()['name']}\n")
