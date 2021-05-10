import requests

response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response)

print(response.request)

request = response.request

# print request and url
print(request, request.url)

print(request.path_url)

# print method
print(request.method)

print(f"{request.headers}\n")

print(f"{response.text}\n")

print(f"{response.status_code}\n")

print(response.headers)
