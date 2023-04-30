#bruh machine
#electrician plumbing 
import requests
import json

import requests
import json

# Set up the API URL and parameters
url = "https://api.spotify.com/v1/tracks/"
#track_id = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
track_id = "7ouMYWpwJ422jRcDASZB7P"

# Add the track_id to the URL
full_url = url + track_id

# Set up the Bearer token
token = "BQBMLv_K0rLlG8GnnXH0nc_MPuE01B11kUEXFqDUtEAFiVpOKCuLrklX1NRQlyXHaedz12Y3GNOBR99TjTRDTNXKxs6lSUvak20-qE8uhCIeKdhSyLC_iiApLNf2WmDaa8hQpPwTF32hr1-Ii87Npppo3aXnGT0j1OniA_I_kf8GTe5e09s33wgU8_5qsr86aAtg36GsV1rMxGH2ptZQmYX5uGGjIJPTs-2R8lKjPanaMxbJfSN4kunyyWI4IOcnmyCtMEFodqqMo8IyfRSOmVSk3gjS-wwKgVYXBCffURuO9iSl6AxRUyu_N8vzlspPdpPAmC8UMSRrHkXM7fl35GhUQ7g9bA"

#Bearer BQAUXQBvjeuUyDSSPOyi2uo2u7HEys31TfF6Aj7z9lzKNJ8EGpVLzXf32DxkhRdJ-XcA0cqFepSw9LaoDuYvsK2Mp27Xkx93m44CQ9fQDksFAdMWJhiIZqNaru4kJ815ua1saFf5MaGUmx1d7YHxIij3E-wGM8anVRk3yX5BfJK6RQWlZ8WnFkFP7_CYaVatm1g395St8sKlR8cxh3t8eBHEOu-CminVpfnyYSsH7FAGGLAs8CRur953fGPfFkLJRRKD2yhK0cACmmOwqCkAmwIoTzRXUOcmx4Ceglepykrcq3flLyF8gUnjm509SW3990qa4LMmS40i7YGGUxbeas-E_NPOFA
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
