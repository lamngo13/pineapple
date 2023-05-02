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
data=data.replace('\'danceability\'', '\'genre\': \"Rap\", \'danceability\'')
data=data.replace("\'", "\"")

file = open("shoob.json", "a")
file.write(data)
file.close()

file = open("shoob1.json", "a")
file.write(data)