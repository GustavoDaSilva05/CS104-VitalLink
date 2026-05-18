import requests

response = requests.post("https://2518zomm0h.execute-api.ap-south-1.amazonaws.com/sandbox", 
              json={"name": "John Doe"})

print(response.status_code)

response_json = response.json()
entry_id = response_json.get("id")

print("Response JSON:", response_json)
print("Entry ID:", entry_id)