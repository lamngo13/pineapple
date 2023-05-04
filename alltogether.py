#bruh machine
#electrician plumbing 
import requests
import json
import os, time
import base64


# Set up the API URL and parameters
url = "https://api.spotify.com/v1/search?q=genre%Rap&type=track&limit=50"
#TODO change Rap to other genres 
file = open(".secret", "r", encoding="utf-8")
#print(file.read())
#print("AYOASDFDAS")
shword = file.readlines()

client_id = shword[0].strip("\n")
client_secret = shword[1]
#id first then secret
print(client_id)

imidiot = client_id + ":" + client_secret
auth_url = 'https://accounts.spotify.com/api/token'
auth_headers = {'Authorization': 'Basic ' + base64.b64encode(imidiot.encode('ascii')).decode('ascii') }
auth_form = {"grant_type": 'client_credentials'}

auth_response = requests.post(auth_url, headers=auth_headers, data=auth_form)

if auth_response.status_code == 200:
    auth_response =json.loads(auth_response.text)
    token = auth_response['access_token']
else:
    print(f"Request failed with status code {auth_response.status_code}: {auth_response.text}")



# Add the track_id to the URL
full_url = url

# Set up the Bearer token
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

data=json.loads(data)
#print(len(data['audio_features']))

#print(data['audio_features'][:-3])


bigfile = data['audio_features'][:-3]
smallfile = data['audio_features'][-3:]

file = open("bigfile.json", "w")
json.dump({'bruh': bigfile}, file, ensure_ascii=False, indent=4)
file.close()

file = open("smallfile.json", "w")
json.dump({'bruh': smallfile}, file, ensure_ascii=False, indent=4)
file.close()

'''
file = open("bigfile.json", "a")
file.write(bigfile)
file.close()

file = open("smallfile.json", "a")
file.write(smallfile)
file.close()
'''
#file = open("shoob1.json", "a")
#file.write(data)

