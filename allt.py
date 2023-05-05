#bruh machine
#electrician plumbing 
import requests, json, os, time, base64, math


# This dict has the search url for each genre, the number will count the number of songs per genre returned
rapDict = {"url": "https://api.spotify.com/v1/search?q=genre%Rap&type=track", "num": 0}
rockDict = {"url": "https://api.spotify.com/v1/search?q=genre%Rock&type=track", "num": 0}
popDict = {"url": "https://api.spotify.com/v1/search?q=genre%Pop&type=track", "num": 0}

#add the dictionaries to a list of dicts called fullGenreList
fullGenreList = [rapDict, rockDict, popDict]


#************************AUTHORIZATION****************************************************************************************************************
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

#yay now we have the authorization token


#**********************************GET SONG IDS BY GENRE*********************************************************************************************************

#give headers the auth token
headers = {"Authorization": f"Bearer {token}"}
#instantiate data as a string to append to
data = ""


#debug: asdf = 1

#the first loop goes through each of the genre urls
#the inner loop (offset) will send multiple requests to a single genre url,
#^it increases the offset each time to get more songs
for genre in fullGenreList:
    for offset in range(0, 40, 20):
        tempurl = genre['url']+"&offset="+str(offset)  #appends the offset parameter to the url
        #important debugging
        #print("\n")
        #print(str(asdf))
        #print("ZURL: " + tempurl)
        #asdf+= 1

        #make the request with the augmented offset and auth token
        response = requests.get(tempurl, headers=headers)
        if response.status_code == 200:

            #read in response as a json object
            data_in= json.loads(response.text)

            #instantiate holder string to append to 
            holder = ""
            #keep for debugginprint("URL: " + tempurl + " number: " + str(len(data_in['tracks']['items'])))

            #take note of the number of songs returned for each genre
            #VERY VERY important for later 
            genre['num'] += len(data_in['tracks']['items'])

            #the json has a LOT LOT LOT of data; this line gets just the song id from the whole returned json object
            for i in range(0, len(data_in['tracks']['items']), 1):
                holder += data_in['tracks']['items'][i]['uri']    
            data += holder #append all the song ids to a list, this is okay because we keep note of the order and number
            time.sleep(.25) #I'm brazy but i stg this makes it work better its just a bit
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")



#make data into a LIST and clean it up
data = data.replace("spotify:track:", ",")[1:]
olddata = data.split(',') #note this is called OLDDATA

#stuff for api call 
featureUrl = "https://api.spotify.com/v1/audio-features?ids=" #universal url for song lookup by id
headers = {"Authorization": f"Bearer {token}"} #give auth token

#get the total number of songs by looping through each genre's num of songs
totalSongs = 0
for i in fullGenreList:
    totalSongs += i['num']

#get the many chunks of songs, and then the remainder
iterationDict = {'reg': math.floor(totalSongs/5), 'xtra':(totalSongs%5) }
#the remainder is because its a slightly different loop
#I arbitrarily say that we should segment the call into 5, (maybe 6) segments

#IMPORTANT DEBUGGING STUFF PLS KEEP
#print("TESTING ELEMENT")
#print(olddata[5])
#print("total songs: " + str(totalSongs))
#print(iterationDict)
#print("\n")


#**********************GET ATTRIBUTES OF A SONG BY LOOKING UP THE SPECIFIC SONG ID*******************************************************************************************************
for i in range(0,5,1): #loop through each main segment 
    full_url = featureUrl #start the url string w the universal lookup api url

    #get the segement to send
    for j in range(0,iterationDict['reg'],1):
        #print("I: "+str(i)+ " J: " + str(j) + " i*5: " + str(i*5) + " index: " + str(((i*5)+j-1)))
        #print('index: ' + str(((i*iterationDict['reg'])+j)))
        full_url += olddata[(i*iterationDict['reg'])+j]+"," 
        #^^goal is to add the 5th of song ids to the lookup url
        #i counts to 5
        #j counts to the segment size

    #send get request w full segmented URL
    response = requests.get(full_url, headers=headers)

    if response.status_code == 200:
        #first case establishes the structure - must keep
        if (i==0):
            print("FIRSTFIRST")
            firstjson = json.loads(response.text) #take in the json response
            data = firstjson #set data to this, we need to do it this way 
            #to get the append structure!
        else:
            tmpdata = json.loads(response.text) # Load the JSON data
            data['audio_features'].append(tmpdata) #append to our building json object
        
    #LAST ONE TO GET REMAINDER this one is really really strange but whatev will TODO later
    if(iterationDict['xtra'] > 0):
        if(i == 4):
            #get the last few songs
            full_url = featureUrl
            #weird case idky it shouldn't have to be this way??
            if(iterationDict["xtra"]==1):
                full_url += olddata[(iterationDict["reg"]*5)]
            else:
                for k in range(0, iterationDict['xtra']-1,1):
                    full_url += olddata[(iterationDict["reg"]*5)+k]+","
                    #SHWHAT
                    # print(str(olddata[(iterationDict["reg"]*5)+k])) #TODO WHY NO WORK
            
            #print("LAST")
            #print(full_url)
            response = requests.get(full_url, headers=headers)
            holder = ""
            if response.status_code == 200:
                data['audio_features'].append(tmpdata)
            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")

    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")



#iterationNum = floor()
print("\nHEREHERHEREHRHERHERHERH\n")
print(type(data))
print(data)





#rn, data is a string, we must change it to a list and segment it 
# URL for getting audio features
####url = "https://api.spotify.com/v1/audio-features?ids="


'''

full_url = url + data

# Set up the Bearer token
headers = {"Authorization": f"Bearer {token}"}

# we must make multipe requests 
response = requests.get(full_url, headers=headers)

# Check if the request was successful
holder = ""
if response.status_code == 200:
    # Load the JSON data
    data = json.loads(response.text)
    ###optumdata = str(data)

else:
    print(f"Request failed with status code {response.status_code}: {response.text}")

'''
#data is json rn, rn I am segmenting the data into the reg set and the testing set in a 10% ratio
#TODO make this dynamic
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

