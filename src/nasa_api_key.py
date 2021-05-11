import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace YOUR_KEY below with your own key if you generated one.
# Create your key in https://api.nasa.gov/

api_key = "YOUR_KEY"
query_params = {"api_key": api_key, "earth_date": "2021-05-10"}
response = requests.get(endpoint, params=query_params)

print(f"{response}\n")

print(f"{response.json()}\n")

photos = response.json()["photos"]
print(f"Found {len(photos)} photos.\n")
print(photos[4]["img_src"])
