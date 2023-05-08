#bruh machine
#electrician plumbing 
import requests, json, os, time, base64, math


# This dict has the search url for each genre, the number will count the number of songs per genre returned
classicpianoDict = {"url": "https://api.spotify.com/v1/search?q=genre%Classical-Piano&type=track", "num": 0}
rockDict = {"url": "https://api.spotify.com/v1/search?q=genre%Rock&type=track", "num": 0}
popDict = {"url": "https://api.spotify.com/v1/search?q=genre%Anime&type=track", "num": 0}

#add the dictionaries to a list of dicts called fullGenreList
fullGenreList = [classicpianoDict, rockDict, popDict]


#************************AUTHORIZATION****************************************************************************************************************
#opens the file with the secrets and reads them 
file = open(".secret", "r", encoding="utf-8")
shword = file.readlines()
#client_id = shword[0].strip("\n")
#client_secret = shword[1]

#The secret is supposed to be hidden but idc, this should work on anyone's machine, NO AUTH TOKEN REQUIRED YAY LFGO


client_id = "38102a72830649e8bffa570c0e40a0b8"
client_secret = "28ba3a3963bc48309ca17c177a742e84"
file.close()
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
    for offset in range(0, 200, 20):
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
            #FUN FACT spotify will return UNPREDICTABLE numbers of songs so we can't hardcode these numbers
            #tough
            genre['num'] += len(data_in['tracks']['items'])

            #the json has a LOT LOT LOT of data; this line gets just the song id from the whole returned json object
            for i in range(0, len(data_in['tracks']['items']), 1):
                holder += data_in['tracks']['items'][i]['uri']    
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
#print(olddata)#print(iterationDict)
#print("\n")
#COFFEE
#AT THIS POINT, THERE ARE THE CORRECT NUMBER OF SONGS IN THIS LIST, COMMA SEPARATED

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
print(fullGenreList)


dataList = data['audio_features']
#^this creates a list of the data to segment it by genre - v important!

#******************************************CLEAN UP DATA BY PUTTING EACH INTO A STRING SEGMENTED BY GENRE*********************************************************************


#I promise you ik how to program, I am doing this rawdog because we will add more genres in the future but I promise you ik this is slow but it is readable

#**The idea here is to segment 90% of the data into the training data, and like 10% into test data
#training data is one file, test data is the other file
#we need to make it a string to clean it up
#spotify api is [INCONSISTENT] at best, so we don't actually know how many songs we're going to get
#that's why we need to do it this way ugh


bigclassicpiano = dataList[:fullGenreList[0]['num']]
print("type of bigclassicalpiano" + str(type(bigclassicpiano)))
print("\n")
print(bigclassicpiano)
iterator = fullGenreList[0]['num']
#the idea is to get the first 0 to [number of classicpiano songs - 3] as the first var
#and the last 3 classicpiano songs as the 2nd var
#each var (rn is just a string) will be cleaned up later
#and then appended to the appropriate file

#smallclassicpiano = dataList[iterator:iterator + 3]
#iterator = fullGenreList[0]['num']
#the iterator is necessary ish to keep our place in the list
#^the point is we traverse the list to find songs of the right genre
#and then assign those songs the genre by search num
#ik this is a weird way to do it, but spotify api 
#doesn't give us the genre so we kinda have to retroactively do it ourselves 


#we have to stair step this by only making rock songs in bigRock by basing off where we were
bigRock = dataList[iterator:iterator+fullGenreList[1]['num']]
iterator += fullGenreList[1]['num']

#smallRock = dataList[iterator:iterator+3]
#iterator += 3

bigPop = dataList[iterator:iterator+fullGenreList[2]['num']]
iterator += fullGenreList[2]['num']

#smallPop = dataList[iterator:iterator+3]
#keep below line for future work
#iterator += 3

#TODO COFFEE add more genres here, 


#OK NOW we have the classicpiano, rock, pop, etc songs sorted into a straight string, 
#(I mean its a string rn but we can convert back to a dict)

#now replace with correct genres
bigclassicpiano = str(bigclassicpiano).replace('\'danceability\'', '\'genre\': \"classicpiano\", \'danceability\'').replace("\'", "\"")
#smallclassicpiano = str(smallclassicpiano).replace('\'danceability\'', '\'genre\': \"classicpiano\", \'danceability\'').replace("\'", "\"")

bigRock = str(bigRock).replace('\'danceability\'', '\'genre\': \"Rock\", \'danceability\'').replace("\'", "\"")
#smallRock = str(smallRock).replace('\'danceability\'', '\'genre\': \"Rock\", \'danceability\'').replace("\'", "\"")

bigPop = str(bigPop).replace('\'danceability\'', '\'genre\': \"Pop\", \'danceability\'').replace("\'", "\"")
#smallPop = str(smallPop).replace('\'danceability\'', '\'genre\': \"Pop\", \'danceability\'').replace("\'", "\"")


#remake into JSON to put into file as a value that can be easily read by ML libraries 
bigclassicpiano = json.loads(bigclassicpiano)
#smallclassicpiano = json.loads(smallclassicpiano)

bigRock = json.loads(bigRock)
#smallRock = json.loads(smallRock)

bigPop = json.loads(bigPop)
#smallPop = json.loads(smallPop)


#OK SO THIS IS IMPORTANT********************************************
#lastBig is now a dict, of a single key-val pair.  The key is 'bruh',
#and the value is a LIST of DICTS - everything we need
#this is werid asf to me, but apparently this is how a ton of stuff is done
#so this is the right way.
lastBig = {'bruh': (bigclassicpiano+bigRock+bigPop)}
#lastSmall = {'bruh': (smallclassicpiano+smallRock+smallPop)}

#WRITE TO FILE
with open('funbigfile.json', 'w') as f: #btw the 'w' parameter here clears whatev is in the file
    json.dump(lastBig, f, ensure_ascii=False, indent=4)
    f.close()

#with open('funsmallfile.json', 'w') as f:
#    json.dump(lastSmall, f, ensure_ascii=False, indent=4)
#    f.close()


#TODO 
#next steps:
#- refine search to only do most popular songs maybe
#- add more genres 
#- ......?
#- profit