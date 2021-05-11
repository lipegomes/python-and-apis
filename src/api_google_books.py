import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"

query = "moby dick"

params = {"q": query, "maxResults": 3}

response = requests.get(endpoint, params=params).json()
print(response)

for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume["title"]
    published = volume["publishedDate"]
    subtitle= volume["subtitle"]
    print(f"{title} ({published}) | {subtitle}")
