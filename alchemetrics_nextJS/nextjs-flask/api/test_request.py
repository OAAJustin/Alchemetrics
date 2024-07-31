import requests
import json

# The URL for the Flask server endpoint
url = "http://localhost:8080/add-item"

# The data to be sent in the POST request
data = {
    'Title': 'Example Title',
    'Medium': 'Oil on Canvas',
    'Size': '24',
    'Qty': 1,
    'Price': 200,
    'Artist': 'John Doe'
}

try:
    # Send the POST request
    response = requests.post(url, json=data)

    # Print the raw response content for debugging
    print(f'Raw response content: {response.text}')

    # Check if the response is successful
    if response.status_code == 200:
        print('Response received')
        # Attempt to parse the JSON response
        response_json = response.json()
        print('Response JSON:', response_json)
    else:
        print(f'Failed to receive response. Status code: {response.status_code}, Message: {response.text}')
except requests.exceptions.RequestException as e:
    print(f'Error sending request: {e}')
except json.JSONDecodeError as e:
    print(f'Error decoding JSON response: {e}')
