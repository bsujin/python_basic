import requests
import json

url = "https://dapi.kakao.com/v2/search/cafe"
queryString = {"query":"아이유"}
header = {'authorization':'KakaoAK e68603d86178518e0161a32013b7fe54'}
r = requests.get(url, headers=header, params=queryString)

jsob = json.loads(r.text)
doc = jsob.get("documents")

for i in doc:
    print("cafename : ",i.get("cafename"), end =" ")
    print("contents :",i.get("contents"), end =" ")
    print("datetime : ",i.get("datetime"), end =" ")

    print("thumbnail : ",i.get("thumbnail"), end =" ")
    print("title:",i.get("title"), end =" ")
    print("url : ",i.get("url"))
    
