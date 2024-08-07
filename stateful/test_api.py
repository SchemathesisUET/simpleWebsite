import schemathesis
import requests
import uuid

# Define the base URL for the API
# BASE_URL = "http://localhost:5000"
BASE_URL = "https://simplewebsite-1.onrender.com"

# Load the OpenAPI schema with the base URL
schema = schemathesis.from_path("openapi.json", base_url=BASE_URL)

@schema.parametrize()
def test_api(case):
    # Ensure the request headers include 'Content-Type: application/json'
    headers = {"Content-Type": "application/json"}
    
    # Prepare and send the request
    response = case.call(headers=headers)
    
    # Validate the response
    case.validate_response(response)

def test_stateful():
    # Register a new user
    user_data = {
        'username': f'user_{uuid.uuid4()}',
        'password': 'test_password'
    }
    # Ensure the request headers include 'Content-Type: application/json'
    headers = {"Content-Type": "application/json"}
    
    # Send POST request to /register
    register_response = requests.post(f"{BASE_URL}/register", json=user_data, headers=headers)
    assert register_response.status_code == 201
    
    # Extract the user_id
    user_id = register_response.json().get('user_id')

    # Login with the registered user
    login_response = requests.post(f"{BASE_URL}/login", json=user_data, headers=headers)
    assert login_response.status_code == 200
    
    # Validate the login response
    response_json = login_response.json()
    assert 'user_id' in response_json
    assert response_json['user_id'] == user_id
