#bruh machine
#electrician plumbing 
import json, os, time, base64, math, requests


# This dict has the search url for each genre, the number will count the number of songs per genre returned
rapDict = {"url": "https://api.spotify.com/v1/search?q=genre%Rap&type=track", "num": 0}
rockDict = {"url": "https://api.spotify.com/v1/search?q=genre%Rock&type=track", "num": 0}
popDict = {"url": "https://api.spotify.com/v1/search?q=genre%Pop&type=track", "num": 0}

#Nori: This dict is almost identical to the one above, only using a getPlaylistItems call rather than using the Spotify search API
#Nori: Defined the limit to be 20 so as to not have to change the built-in offset code
rnbDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DX4SBhb3fqCJd/tracks?limit=50", "num": 0}
salsaDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DX4qKWGR9z0LI/tracks?limit=50", "num": 0}
reggaetonDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DWY7IeIP1cdjF/tracks?limit=50", "num": 0}
metalDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DWTcqUzwhNmKv/tracks?limit=50", "num": 0}
countryDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DX1lVhptIYRda/tracks?limit=50", "num": 0}
rapDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DX0XUsuxWHRQd/tracks?limit=50", "num": 0}
classicalDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DWWEJlAGA9gs0/tracks?limit=50", "num": 0}
rockDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DXcF6B6QPhFDv/tracks?limit=50", "num": 0}
phonkDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DWWY64wDtewQt/tracks?limit=50", "num": 0}
jazzDict = {"url": "https://api.spotify.com/v1/playlists/37i9dQZF1DX7YCknf2jT6s/tracks?limit=50", "num": 0}
#add the dictionaries to a list of dicts called fullGenreList
#Nori: add the Playlist-derived dictionaries to fullGenreListPlaylist
fullGenreList = [rapDict, rockDict, popDict]
fullGenreListPlaylist = [rnbDict, salsaDict, reggaetonDict, metalDict, countryDict, rapDict, classicalDict, rockDict, phonkDict, jazzDict]

#************************AUTHORIZATION****************************************************************************************************************
#opens the file with the secrets and reads them 
file = open(".secret", "r", encoding="utf-8")
shword = file.readlines()
client_id = shword[0].strip("\n")
client_secret = shword[1]

#The secret is supposed to be hidden but idc, this should work on anyone's machine, NO AUTH TOKEN REQUIRED YAY LFGO


#client_id = "38102a72830649e8bffa570c0e40a0b8"
#client_secret = "28ba3a3963bc48309ca17c177a742e84"
#file.close()
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


#the first loop goes through each of the genre urls
#the inner loop (offset) will send multiple requests to a single genre url,
#^it increases the offset each time to get more songs
for genre in fullGenreListPlaylist:
    for offset in range(0,1,1):
        tempurl = genre['url']#appends the offset parameter to the url
        #important debugging
        #print("\n")
        #print(str(asdf))
        #print("ZURL: " + tempurl)
        #asdf+= 1

        #make the request with the augmented offset and auth token
        response = requests.get(tempurl, headers=headers, stream=False)
        if response.status_code == 200:

            #read in response as a json object
            data_in= json.loads(response.text)

            #instantiate holder string to append to 
            holder = ""
            #keep for debugginprint("URL: " + tempurl + " number: " + str(len(data_in['tracks']['items'])))

            #take note of the number of songs returned for each genre
            #VERY VERY important for later 
            #FUN FACT spotify will return UNPREDICTABLE numbers of songs so we can't hardcode these numbers
            #tough
            genre['num'] += len(data_in['items'])
            bruh = len(data_in['items'])

            #the json has a LOT LOT LOT of data; this line gets just the song id from the whole returned json object
            for i in range(0, len(data_in['items']), 1):
                holder += data_in['items'][i]['track']['uri']

            data += holder #append all the song ids to a list, this is okay because we keep note of the order and number

            time.sleep(.1) #I'm brazy but i stg this makes it work better its just a bit
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")


#make data into a LIST and clean it up
data = data.replace("spotify:track:", ",")[1:]
olddata = data.split(',') #note this is called OLDDATA
#stuff for api call 
featureUrl = "https://api.spotify.com/v1/audio-features?ids=" #universal url for song lookup by id
headers = {"Authorization": f"Bearer {token}"} #give auth token

#get the total number of songs by looping through each genre's num of songs

#Since I capped the songs at 50, we just make it 50 songs per genre
#The following code makes it easy to add genres as long as you use a playlist with at least 50 songs
totalSongs = len(fullGenreListPlaylist) * 50
#for i in fullGenreListPlaylist:
#    totalSongs += i['num']

#get the many chunks of songs, and then the remainder
iterationDict = {'reg': math.floor(totalSongs/5), 'xtra':(totalSongs%5) }
#the remainder is because its a slightly different loop
#I arbitrarily say that we should segment the call into 5, (maybe 6) segments for explained below


#AT THIS POINT, THERE ARE THE CORRECT NUMBER OF SONGS IN THIS LIST, COMMA SEPARATED

#**********************GET ATTRIBUTES OF A SONG BY LOOKING UP THE SPECIFIC SONG ID*******************************************************************************************************
######################*****WE'RE DOING THIS SEGMENT MESS TO NOT MAKE THE URL TOO LONG NO MATTER HOW MANY SONGS WE HAVE YAY****************************
counter = 0
print("OLD DATA LEN:",len(olddata))
for i in range(0,5,1): #loop through each main segment 
    full_url = featureUrl #start the url string w the universal lookup api url

    #get the segement to send
    for j in range(0,100,1):


        full_url += olddata[counter]+"," 
        counter += 1
        #^^goal is to add the 5th of song ids to the lookup url
        #i counts to 5
        #j counts to the segment size

    #send get request w full segmented URL
    response = requests.get(full_url, headers=headers, stream=False)
    #print("FULL URL: " + full_url + "\n")
    #COFFEE
    #The URLs are correct; they are unique and there are the right number of them.

    if response.status_code == 200:
        #first case establishes the structure - must keep
        if (i==0):
            #print("FIRSTFIRST")
            firstjson = json.loads(response.text) #take in the json response
            data = firstjson #set data to this, we need to do it this way 

            #to get the append structure!
        else:
            tmpdata = json.loads(response.text) # Load the JSON data
            data['audio_features'] = data['audio_features']+tmpdata['audio_features'] #append to our building json object

        
    #LAST ONE TO GET REMAINDER this one is really really strange but whatev will TODO later
    if(iterationDict['xtra'] > 0):
        if(i == 4):
            #get the last few songs
            full_url = featureUrl
            #weird case idky it shouldn't have to be this way??
            if(iterationDict["xtra"]==1):
                full_url += olddata[(iterationDict["reg"]*5)]
            else:
                for k in range(0, iterationDict['xtra'],1):
                    full_url += olddata[(iterationDict["reg"]*5)+k]+","
                    #SHWHAT
                    # print(str(olddata[(iterationDict["reg"]*5)+k])) #TODO WHY NO WORK
            
            #print("LAST")
            #print(full_url)
            response = requests.get(full_url, headers=headers)
            holder = ""
            if response.status_code == 200:
                data['audio_feature'] = data['audio_features']+tmpdata['audio_features']
            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")

    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")


#KEEP FOR DEBUGGING
#print(data)
#print("\n")
#print(data['audio_features'])
print("total songs: " + str(totalSongs))
#UNCOMMENT THIS: print(fullGenreListPlaylist)


dataList = data['audio_features']
#^this creates a list of the data to segment it by genre - v important!

#******************************************CLEAN UP DATA BY PUTTING EACH INTO A STRING SEGMENTED BY GENRE*********************************************************************


#I promise you ik how to program, I am doing this rawdog because we will add more genres in the future but I promise you ik this is slow but it is readable

bigRnb = ""
bigSalsa = ""
bigReggaeton = ""
bigMetal = ""
bigCountry = ""
bigRap = ""
bigClassical = ""
bigRock = ""
bigPhonk = ""
bigJazz = ""

listingholders = [bigRnb,bigSalsa,bigReggaeton,bigMetal,bigCountry,bigRap,bigClassical,bigRock,bigPhonk,bigJazz]

iterator = 0
genreIterator = 0
for genre in listingholders:
    listingholders[genreIterator] = dataList[iterator:iterator+fullGenreListPlaylist[genreIterator]['num']]
    iterator += fullGenreListPlaylist[genreIterator]['num']
    genreIterator += 1


bigRnb = listingholders[0]
bigSalsa = listingholders[1]
bigReggaeton = listingholders[2]
bigMetal = listingholders[3]
bigCountry = listingholders[4]
bigRap = listingholders[5]
bigClassical = listingholders[6]
bigRock = listingholders[7]
bigPhonk = listingholders[8]
bigJazz = listingholders[9]



#OK NOW we have the rap, rock, pop, etc songs sorted into a straight string, 
#(I mean its a string rn but we can convert back to a dict)

#now replace with correct genres
bigRnb = str(bigRnb).replace('\'danceability\'', '\'genre\': \"Rnb\", \'danceability\'').replace("\'", "\"")

bigSalsa = str(bigSalsa).replace('\'danceability\'', '\'genre\': \"Salsa\", \'danceability\'').replace("\'", "\"")

bigReggaeton = str(bigReggaeton).replace('\'danceability\'', '\'genre\': \"Reggaeton\", \'danceability\'').replace("\'", "\"")

bigMetal = str(bigMetal).replace('\'danceability\'', '\'genre\': \"Metal\", \'danceability\'').replace("\'", "\"")

bigCountry = str(bigCountry).replace('\'danceability\'', '\'genre\': \"Country\", \'danceability\'').replace("\'", "\"")

bigRap = str(bigRap).replace('\'danceability\'', '\'genre\': \"Rap\", \'danceability\'').replace("\'", "\"")


bigClassical = str(bigClassical).replace('\'danceability\'', '\'genre\': \"Classical\", \'danceability\'').replace("\'", "\"")


bigRock = str(bigRock).replace('\'danceability\'', '\'genre\': \"Rock\", \'danceability\'').replace("\'", "\"")


bigPhonk = str(bigPhonk).replace('\'danceability\'', '\'genre\': \"Phonk\", \'danceability\'').replace("\'", "\"")


bigJazz = str(bigJazz).replace('\'danceability\'', '\'genre\': \"Jazz\", \'danceability\'').replace("\'", "\"")



#remake into JSON to put into file as a value that can be easily read by ML libraries 
bigRnb = json.loads(bigRnb)
bigSalsa = json.loads(bigSalsa)
bigReggaeton = json.loads(bigReggaeton)
bigMetal = json.loads(bigMetal)
bigCountry = json.loads(bigCountry)
bigRap = json.loads(bigRap)
bigClassical = json.loads(bigClassical)
bigRock = json.loads(bigRock)
bigPhonk = json.loads(bigPhonk)
bigJazz = json.loads(bigJazz)

#bigPop = json.loads(bigPop)
#smallPop = json.loads(smallPop)


#OK SO THIS IS IMPORTANT********************************************
#lastBig is now a dict, of a single key-val pair.  The key is 'bruh',
#and the value is a LIST of DICTS - everything we need
#this is werid asf to me, but apparently this is how a ton of stuff is done
#so this is the right way.
#Metal, Salsa, Jazz, Country, and Reggaeton
lastBig = {'bruh': ( bigMetal + bigJazz + bigReggaeton + bigSalsa + bigCountry)}

#[rnbDict, salsaDict, reggaetonDict, metalDict, countryDict, rapDict, classicalDict, rockDict, phonkDict, jazzDict]
#WRITE TO FILE
with open('funbigfile.json', 'w') as f: #btw the 'w' parameter here clears whatev is in the file
    json.dump(lastBig, f, ensure_ascii=False, indent=4)
    f.close()

