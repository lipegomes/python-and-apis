import requests

response = requests.get("https://cdn.pixabay.com/photo/2020/02/13/21/21/lighthouse-4846855_960_720.jpg")

print(response)

print(response.headers.get("Content-Type"))
file = open("assets\\pictures\\lighthouse.jpeg", "wb")
file.write(response.content)
file.close()
