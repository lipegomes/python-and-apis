import requests
from requests.api import request

"""
CRUD:

CREATE
READ
UPDATE
DELETE
"""

print("https://api.thedogapi.com/v1/breeds/1")

# POST - Create a new resource
print(f'POST: {requests.post("https://api.thedogapi.com/v1/breeds/1")}')

# GET - Read an existing resource
print(f'GET: {requests.get("https://api.thedogapi.com/v1/breeds/1")}')

# PUT - Update an existing resource
print(f'PUT: {requests.put("https://api.thedogapi.com/v1/breeds/1")}')

# DELETE - Delete an existing resource
print(f'DELETE: {requests.delete("https://api.thedogapi.com/v1/breeds/1")}\n')


print("https://api.filipegomes.dev")

# POST - Create a new resource
print(f'POST: {requests.post("https://api.filipegomes.dev")}')

# GET - Read an existing resource
print(f'GET: {requests.get("https://api.filipegomes.dev")}')

# PUT - Update an existing resource
print(f'PUT: {requests.put("https://api.filipegomes.dev")}')

# DELETE - Delete an existing resource
print(f'DELETE: {requests.delete("https://api.filipegomes.dev")}')
