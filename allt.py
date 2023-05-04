#bruh machine
#electrician plumbing 
import requests, json, os, time, base64


# These are the search apis by genre
rapurl = "https://api.spotify.com/v1/search?q=genre%Rap&type=track&limit=50"
rockurl = "https://api.spotify.com/v1/search?q=genre%Rock&type=track&limit=50"
popurl = "https://api.spotify.com/v1/search?q=genre%Pop&type=track&limit=50"

genreList = [rapurl, rockurl, popurl]

#opens the file with the secrets and reads them 
file = open(".secret", "r", encoding="utf-8")
shword = file.readlines()
client_id = shword[0].strip("\n")
client_secret = shword[1]
#id first then secret


#getting the token
#use the client id and secret to get the token
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



#These lines and request below get the song ids by searching through different genres 
headers = {"Authorization": f"Bearer {token}"}

data = ""

#search
for zurl in genreList:
    response = requests.get(zurl, headers=headers)
    if response.status_code == 200:

        data_in= json.loads(response.text)
        holder = ""
        for i in range(0, 20, 1):
            holder += data_in['tracks']['items'][i]['uri']    
        data += holder
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")


#take "getting spotify ids" cleaning up the data
data = data.replace("spotify:track:", ",")[1:]

# URL for getting audio features
url = "https://api.spotify.com/v1/audio-features?ids="
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
    ###optumdata = str(data)

else:
    print(f"Request failed with status code {response.status_code}: {response.text}")


#data is json rn, rn I am segmenting the data into the reg set and the testing set in a 10% ratio
bigRap = data['audio_features'][:18]
smallRap = data['audio_features'][18:20]

bigRock = data['audio_features'][20:38]
smallRock = data['audio_features'][38:40]

bigPop = data['audio_features'][40:58]
smallPop = data['audio_features'][58:60]

#bigfile = data['audio_features'][:-3]
#smallfile = data['audio_features'][-3:]

#now replace with correct genres
bigRap = str(bigRap).replace('\'danceability\'', '\'genre\': \"Rap\", \'danceability\'').replace("\'", "\"")
smallRap = str(smallRap).replace('\'danceability\'', '\'genre\': \"Rap\", \'danceability\'').replace("\'", "\"")

bigRock = str(bigRock).replace('\'danceability\'', '\'genre\': \"Rock\", \'danceability\'').replace("\'", "\"")
smallRock = str(smallRock).replace('\'danceability\'', '\'genre\': \"Rock\", \'danceability\'').replace("\'", "\"")

bigPop = str(bigPop).replace('\'danceability\'', '\'genre\': \"Pop\", \'danceability\'').replace("\'", "\"")
smallPop = str(smallPop).replace('\'danceability\'', '\'genre\': \"Pop\", \'danceability\'').replace("\'", "\"")

#remake into JSON to put into file as a value 
bigRap = json.loads(bigRap)
smallRap = json.loads(smallRap)

bigRock = json.loads(bigRock)
smallRock = json.loads(smallRock)

bigPop = json.loads(bigPop)
smallPop = json.loads(smallPop)

lastBig = {'bruh': (bigRap+bigRock+bigPop)}
lastSmall = {'bruh': (smallRap+smallRock+smallPop)}

with open('bigfile.json', 'w') as f:
    json.dump(lastBig, f, ensure_ascii=False, indent=4)
    f.close()

with open('smallfile.json', 'w') as f:
    json.dump(lastSmall, f, ensure_ascii=False, indent=4)
    f.close()
'''
file = open("bigfile.json", "w")
json.dump({'bruh': bigRap}, file, ensure_ascii=False, indent=4)
file.close()

file = open("smallfile.json", "w")
json.dump({'bruh': smallRap}, file, ensure_ascii=False, indent=4)
file.close()
'''

