import requests
import json

response = requests.get('https://petstore.swagger.io/v2/store/inventory', verify=False)

if response.status_code == 200 and response.headers["Content-Type"]=="application/json":
     response_json = response.json()
     response_pretty = json.dumps(response_json, indent=4, ensure_ascii=False)
     print(response_pretty)


