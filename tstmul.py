#bruh machine
#electrician plumbing 
import requests
import json
import os, time

# Set up the API URL and parameters
url = "https://api.spotify.com/v1/audio-features?ids="
#track_id = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
rap = "17vJ4JDM5nsU4jxZgl1QSRspotify:track:3pzkWSjCdHKdzNEljKI4gzspotify:track:7i6jHKsAShYpPTN4kS4WBWspotify:track:1Bt9doNZTAw34cuW2FxaZWspotify:track:6BjmeqZw3N9etV8Oa2CkH1spotify:track:57wZV2CA5dbaJqyxxYUfK2spotify:track:5MuiMQ0ZTtGbVNRLBynOeEspotify:track:4QhPHgDgAFbbrWS7bcpEojspotify:track:3fYVwsvmV4QRhLVZcuL5yyspotify:track:3xls9xAVcGhHqc5B7e8Ywaspotify:track:755l4UkvolIqUBjlsv6uIDspotify:track:2liy0NM9d6CjAx3EwWksyNspotify:track:2mrwdu7Cdezo4xOGEni7Rvspotify:track:3elRCrT4kWcVyP2EjPc8cPspotify:track:1t7sVX8wCMVZHFSfYH2Y0yspotify:track:3xNTYCJki80XXOphZi7UKuspotify:track:5PNmwrKFzYrEv5jhgCjxhsspotify:track:3Kpsnwm3geSUFyQDBc7Rgwspotify:track:3ezhOp8Loy3SpY7mJqZuerspotify:track:4fFpJhPFy9Vmm8Oc4Ygams"
rap = rap.replace("spotify:track:", ",")
track_id = rap

# Add the track_id to the URL
full_url = url + track_id

# Set up the Bearer token
token = "BQD81fh5GHr4NQqwQCVIQtHAtfDAKCaFknuivHIuzI77hB7W_7o2TO1aEXEHWGhS8EhiNWY7_w9lsqOPc9yDa5lP9-gE2NAwAfvPKfzLPGfV-gmaX9G_yKo_FqrZxy14tFyaOFt9armJMcJ3RClH-B10DgKC-MiarIId7T8GrVn5FCocCPXJE44Y5pMKeFR9_VxKG24mEhqtWf0GgNns6x6pk_Dl1V2B4a-Q804RncRA3ngxVMeMX-mtQTh-mcrQ847gBneQcLjlH2UwqjqWi_q3cRKOQnQ93fbnCzWuZtSQFB5Kq4z1y1y4cwms6DfvIXC6dPVV9_eT-rtVs6lYFsjwNo1f4g"
#Bearer BQAUXQBvjeuUyDSSPOyi2uo2u7HEys31TfF6Aj7z9lzKNJ8EGpVLzXf32DxkhRdJ-XcA0cqFepSw9LaoDuYvsK2Mp27Xkx93m44CQ9fQDksFAdMWJhiIZqNaru4kJ815ua1saFf5MaGUmx1d7YHxIij3E-wGM8anVRk3yX5BfJK6RQWlZ8WnFkFP7_CYaVatm1g395St8sKlR8cxh3t8eBHEOu-CminVpfnyYSsH7FAGGLAs8CRur953fGPfFkLJRRKD2yhK0cACmmOwqCkAmwIoTzRXUOcmx4Ceglepykrcq3flLyF8gUnjm509SW3990qa4LMmS40i7YGGUxbeas-E_NPOFA
headers = {"Authorization": f"Bearer {token}"}

# Make the GET request
response = requests.get(full_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data
    data = json.loads(response.text)
    data = str(data)
    file = open("hermaniqua.txt", "a")

    #space the data 

    #this wipes file if u want
    #file.truncate(0)
    file.write(str(data)+'\n')

    # Parse and print the results
    print(json.dumps(data, indent=4))
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
