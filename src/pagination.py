import requests

response = requests.get("https://api.github.com/events?per_page=1&page=0")
print(response.json()[0]["id"])

response = requests.get("https://api.github.com/events?per_page=1&page=1")
print(response.json()[0]["id"])

response = requests.get("https://api.github.com/events?per_page=1&page=2")
print(response.json()[0]["id"])

endpoint = "https://api.github.com/events"
for i in range(100):
    response = requests.get(endpoint)
    print(f"{i} - {response.status_code}")
    if response.status_code != 200:
        break

print (response)

print(response.json())
