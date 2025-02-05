import requests
import json

response = requests.put('https://petstore.swagger.io/v2/pet', verify=False, headers={"Content-Type":"application/json"}, json={
    "id": 9223372036854764524,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "fish",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "Super Cool Fish"
        }
    ],
    "status": "available"
})

print(response.status_code)
print(response.text)




