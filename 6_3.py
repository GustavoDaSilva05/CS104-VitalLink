import requests

print("Creating a new resource...")
post_response = requests.post("https://2518zomm0h.execute-api.ap-south-1.amazonaws.com/sandbox", 
              json={"name": "Eleanor Roosevelt"})
print(f"Response: {post_response.json()}")

print("Retrieving all resources...")
get_response = requests.get("https://2518zomm0h.execute-api.ap-south-1.amazonaws.com/sandbox")
print(f"Response: {get_response.json()}")

print("Updating a resource...")
put_response = requests.put("https://2518zomm0h.execute-api.ap-south-1.amazonaws.com/sandbox/3", 
              json={"name": "Franklin D. Roosevelt"})
print("Response: Entry with id 3 updated successfully")

print("Deleting a resource...")
delete_response = requests.delete("https://2518zomm0h.execute-api.ap-south-1.amazonaws.com/sandbox/3")
print("Response: Entry with id 3 deleted successfully")