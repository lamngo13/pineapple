#bruh machine
#electrician plumbing 
import requests
import json
import os, time

# Set up the API URL and parameters
url = "https://api.spotify.com/v1/search?q=genre%Rap&type=track&limit=50"
#TODO change Rap to other genres 


# Add the track_id to the URL
full_url = url

# Set up the Bearer token
token= "BQAvx2G47XmSlfk4nhMSKcNKXzHxMFIbmFEkpry6TKipjIf_cqnqlci80tjaKieNfYlw6TXoZfRknPkhIVOfVcT0MTOUxNXQdo3GA6zuJ6DXPql1abeAQEHEyK0XeL4S1YFuJCPa55aL1AAQEAdBSoUTTsJ55L7fr5XZ3RW7c2xy8kVdE0Koc2f91aBkCmpbAeBHvnc9k60pha_m2JOSDgjAPlYAbA0np7KDPzgd9tOI1zZd_HMd2AyasscKC4lZcxD7vOXOQIrhY2oFzxxn8ymoSCnHK1a4navy40CXFtEACYJIVY64BA27qCCFmckrBAnk_u7lF3PQQGLSlTezKDrkzO4APw"
#Bearer BQAUXQBvjeuUyDSSPOyi2uo2u7HEys31TfF6Aj7z9lzKNJ8EGpVLzXf32DxkhRdJ-XcA0cqFepSw9LaoDuYvsK2Mp27Xkx93m44CQ9fQDksFAdMWJhiIZqNaru4kJ815ua1saFf5MaGUmx1d7YHxIij3E-wGM8anVRk3yX5BfJK6RQWlZ8WnFkFP7_CYaVatm1g395St8sKlR8cxh3t8eBHEOu-CminVpfnyYSsH7FAGGLAs8CRur953fGPfFkLJRRKD2yhK0cACmmOwqCkAmwIoTzRXUOcmx4Ceglepykrcq3flLyF8gUnjm509SW3990qa4LMmS40i7YGGUxbeas-E_NPOFA
headers = {"Authorization": f"Bearer {token}"}

# Make the GET request
response = requests.get(full_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data
    #response_json['tracks']['items'][0]['uri']
    data = json.loads(response.text)
    holder = ""
    for i in range(0, 20, 1):
        holder += data['tracks']['items'][i]['uri']
    #data = data['tracks']['items'][0]['uri']
    data = holder

else:
    print(f"Request failed with status code {response.status_code}: {response.text}")

#take "getting spotify ids"
data = data.replace("spotify:track:", ",")[1:]

#now make the call w this stuff

# Set up the API URL and parameters
url = "https://api.spotify.com/v1/audio-features?ids="

# Add the track_id to the URL
full_url = url + data

# Set up the Bearer token
headers = {"Authorization": f"Bearer {token}"}

# Make the GET request
response = requests.get(full_url, headers=headers)

# Check if the request was successful
holder = ""
if response.status_code == 200:
    # Load the JSON data
    data = json.loads(response.text)
    data = str(data)

else:
    print(f"Request failed with status code {response.status_code}: {response.text}")

#genreify the data
data=data.replace('\'danceability\'', '\'genre\': Rap, \'danceability\'')

file = open("shoob.json", "a")
file.write(data)