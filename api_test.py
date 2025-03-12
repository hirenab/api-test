import requests
import unittest

# Base URL and Auth Token
base_url = "https://gorest.co.in/public/v2"
auth_token = "a8a65ae4595ce0b51ae71ee2550be213e5a2ea7475670677cd3b43f3d1ef5925"

class TestGetUserAPI(unittest.TestCase):

    def test_get_user(self):
        """Test successful GET request to retrieve user details with auth token"""
        url = f'{base_url}/users/7760953'
        
        # Headers with authorization token
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        
        # GET request
        response = requests.get(url, headers=headers)

        # Checking if the status code is 200 (Success)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code}")

        # Checking if the response contains valid JSON data
        data = response.json()
        self.assertIsNotNone(data, "Expected JSON response, but got None")

        # Checking if a specific field (like 'id') is in the response data
        self.assertIn('id', data, "Expected 'id' in the response, but it was not found")
        self.assertEqual(data['id'], 7760953, f"Expected user ID to be 7760953, but got {data['id']}")

        # Printing the response data
        print("Response Data:", data)


    def test_put_user(self):
        """Test successful PUT request to update user details with auth token"""
        url = f'{base_url}/users/7760953'
        
        # Headers with authorization token
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }

        # Data to update the user
        payload = {
            "name": "Hiren Test",
            "email": "hiren.test@example.com",
            "status": "active"
        }

        # PUT request
        response = requests.put(url, headers=headers, json=payload)

        # Checking if the status code is 200 (Success)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code}")

        # Checking if the response contains valid JSON data
        data = response.json()
        self.assertIsNotNone(data, "Expected JSON response, but got None")

        # Checking if the updated fields match
        self.assertEqual(data['name'], payload['name'], f"Expected name to be {payload['name']}, but got {data['name']}")
        self.assertEqual(data['email'], payload['email'], f"Expected email to be {payload['email']}, but got {data['email']}")
        self.assertEqual(data['status'], payload['status'], f"Expected status to be {payload['status']}, but got {data['status']}")

        # Printing the response data
        print("Updated User Data:", data)

    
    def test_post_user(self):
        """Test successful POST request to create a new user with auth token"""
        url = f'{base_url}/users'
        
        # Headers with authorization token
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }

        # Data to create the new user
        payload = {
            "name": "Mark",
            "email": "mark234@example.com",
            "gender": "male",
            "status": "active"
        }

        # POST request
        response = requests.post(url, headers=headers, json=payload)

        # Checking if the status code is 201 (Created)
        self.assertEqual(response.status_code, 201, f"Expected status code 201, but got {response.status_code}")

        # Checking if the response contains valid JSON data
        data = response.json()
        self.assertIsNotNone(data, "Expected JSON response, but got None")

        # Checking if the created fields match
        self.assertEqual(data['name'], payload['name'], f"Expected name to be {payload['name']}, but got {data['name']}")
        self.assertEqual(data['email'], payload['email'], f"Expected email to be {payload['email']}, but got {data['email']}")
        self.assertEqual(data['status'], payload['status'], f"Expected status to be {payload['status']}, but got {data['status']}")
        self.assertEqual(data['gender'], payload['gender'], f"Expected gender to be {payload['gender']}, but got {data['gender']}")

        # Printing the response data
        print("Created User Data:", data)

    def test_delete_user(self):
        """Test successful DELETE request to delete a user with auth token"""
        user_id = 7762238 
        url = f'{base_url}/users/{user_id}'
        
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }

        # Sending DELETE request
        response = requests.delete(url, headers=headers)

        # Checking if the status code is 204
        self.assertEqual(response.status_code, 204, f"Expected status code 204, but got {response.status_code}")

        # Checking if the resource has been deleted by making a GET request
        get_response = requests.get(url, headers=headers)
        self.assertEqual(get_response.status_code, 404, "Expected status code 404 for deleted user")

        print(f"User {user_id} has been deleted successfully.")

if __name__ == '__main__':
    unittest.main()
