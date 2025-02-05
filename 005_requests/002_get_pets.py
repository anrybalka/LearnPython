import requests
import json

response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', verify=False, params={"status": "available"})

# Проверяем успешность запроса и корректность заголовка
if response.status_code == 200 and response.headers.get("Content-Type", "").startswith("application/json"):
    response_json = response.json()
    
    print(len(response_json))

    # Преобразуем в красиво форматированный JSON
    response_pretty = json.dumps(response_json, indent=4, ensure_ascii=False)
    

    # Сохраняем в файл
    with open("pets_sold.json", "w", encoding="utf-8") as file:
        file.write(response_pretty)
    
    print("Данные успешно сохранены в 'pets_sold.json'")
else:
    print("Ошибка при получении данных:", response.status_code)


