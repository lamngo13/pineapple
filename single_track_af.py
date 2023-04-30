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
token = "BQAQuqWHp9F4VVohxuQaF-Xthilkq3gJiYS-kWoFItpCvkPTkkYfKqP6kDmsfKsI0KHUWfKCV3wtBckTSa95XGPwCXGJwkZ-urhVE89YoFipOIlGopUmKzT397Ix_YI78krCjTPbVKL7cfU0CmNyDu-hJ0zipFlhhQ13lu7POtZ0PvRmCaNSwBprj3G83iiCdTRZPGL_U9gDVAiO4ZHvp9vqM2gmFWYj3c_vD2Pn7WRm2eyaa3p-_1oae9hlJLS-ZzNdsG5V5iH6l-V2S9iNwxmSwG4Iu5Uzgb6EYiP7svbJG8MnphADrCGuteSOvOCz0vbJa_zY63zopUbPJb2IMvgDBWBfJg"

#BQAQuqWHp9F4VVohxuQaF-Xthilkq3gJiYS-kWoFItpCvkPTkkYfKqP6kDmsfKsI0KHUWfKCV3wtBckTSa95XGPwCXGJwkZ-urhVE89YoFipOIlGopUmKzT397Ix_YI78krCjTPbVKL7cfU0CmNyDu-hJ0zipFlhhQ13lu7POtZ0PvRmCaNSwBprj3G83iiCdTRZPGL_U9gDVAiO4ZHvp9vqM2gmFWYj3c_vD2Pn7WRm2eyaa3p-_1oae9hlJLS-ZzNdsG5V5iH6l-V2S9iNwxmSwG4Iu5Uzgb6EYiP7svbJG8MnphADrCGuteSOvOCz0vbJa_zY63zopUbPJb2IMvgDBWBfJg
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
