#bruh machine
#electrician plumbing 
import requests
import json

import requests
import json

# Set up the API URL and parameters
url = "https://api.spotify.com/v1/audio-features/"
track_id = "7ouMYWpwJ422jRcDASZB7P"

# Add the track_id to the URL
full_url = url + track_id

# Set up the Bearer token
token = "TOKENVAL"
headers = {"Authorization": f"Bearer {token}"}

# Make the GET request
response = requests.get(full_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data
    data = json.loads(response.text)

    # Parse and print the results
    print(json.dumps(data, indent=4))
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
