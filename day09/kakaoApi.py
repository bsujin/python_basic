import json,requests
import sys
url = "https://dapi.kakao.com/v2/search/cafe"
apikey = "e68603d86178518e0161a32013b7fe54"
subj = "아이유"
#                                     키 : 키값              권한  
r = requests.get( url, params = {'query':subj}, headers={'Authorization' : 'KakaoAK ' + apikey } )
js = json.JSONEncoder().encode(r.json())

for i in r.json()["documents"] :
    print (i["title"] ) 
    print (i["url"])
    print (i["datetime"])
    print (i["contents"])


