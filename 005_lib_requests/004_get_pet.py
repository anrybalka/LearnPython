
import requests
import json

response = requests.get('https://petstore.swagger.io/v2/pet/10997', verify=False)

print(response)

# Проверяем успешность запроса и корректность заголовка
if response.status_code == 200 and response.headers.get("Content-Type", "").startswith("application/json"):
    response_json = response.json()
    response_pretty = json.dumps(response_json, indent=4, ensure_ascii=False)
    print(response_pretty)
