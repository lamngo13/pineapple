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
token= "BQDjc8WYc35i6MIbhSx5YaB6XKsiKVtVI_taFFPWmFN7eAT0kPpJx5kEuD_8hYgBKiwxInxLAoywvrVikZ_2pREQj91AvjBwL6yEw8snOKwrtpSHNH-Utd4F63JY-jIK79sp4acD-fE1TVMtQX4laG4XUxdlWTa2Bq9_v4oLWuiPxz84NUHO5jt8-7n6_QpcvxTmFDL5c6iywHjgJ1cftqIhWawcuGMlDmzoc9MS411Qbn1f6GaAFTnB-cAxndHeYnihjFjoUyVQ00ZJg45vCVJxoW2tf5EndTmovMMj054F4ZwZ-LjR6FGu_roX_HVwcJV2B4vkp5SRqyIfggddJpzbRB_0EQ"
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

#file = open("shoob1.json", "a")
#file.write(data)