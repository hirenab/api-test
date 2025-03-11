import requests
import json
import random


# Base URL:
base_url = "https://gorest.co.in"

# Auth token:
auth_token = "a8a65ae4595ce0b51ae71ee2550be213e5a2ea7475670677cd3b43f3d1ef5925"

# GET Request
def get_request():
    url = base_url + "/public/v2/users/"
    print("GET URL: " + url)
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON GET response body: ", json_str)
        print(".......GET USER IS DONE.......")
    else:
        print(f"Failed GET request. Status code: {response.status_code}, Response: {response.text}")

# POST Request
def post_request():
    url = base_url + "/public/v2/users"
    print("POST URL: " + url)
    headers = {"Authorization": f"Bearer {auth_token}"}
    data = {
        "name": "Hiren",
        "email": "test" + str(random.randint(1, 1000)) + "@gmail.com",  # To avoid duplicate email issue
        "gender": "male",
        "status": "inactive"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON POST response body: ", json_str)
        user_id = json_data["id"]
        print("User ID ===>", user_id)
        print(".......POST/Create USER IS DONE.......")
        return user_id
    else:
        print(f"Failed POST request. Status code: {response.status_code}, Response: {response.text}")
        return None

# PUT Request
def put_request(user_id):
    if not user_id:
        print("Invalid user ID. PUT request cannot be performed.")
        return
    
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT URL: " + url)
    headers = {"Authorization": f"Bearer {auth_token}"}
    data = {
        "name": "Hiren Automation",
        "email": "Hirentest@gmail.com",
        "gender": "male",
        "status": "inactive"
    }
    
    response = requests.put(url, json=data, headers=headers)
    
    if response.status_code == 200:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("JSON PUT response body: ", json_str)
        print(".......PUT/Update USER IS DONE.......")
    else:
        print(f"Failed PUT request. Status code: {response.status_code}, Response: {response.text}")

# DELETE Request
def delete_request(user_id):
    if not user_id:
        print("Invalid user ID. DELETE request cannot be performed.")
        return
    
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE URL: " + url)
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print(f".......DELETE USER {user_id} IS DONE.......")
    else:
        print(f"Failed DELETE request. Status code: {response.status_code}, Response: {response.text}")

# Call functions
get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
