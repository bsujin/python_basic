import requests

url = "https://dapi.kakao.com/v2/search/cafe"   #찾을 사이트- 검색 영역
header = {'Authorization' : 'KakaoAK ' + "e68603d86178518e0161a32013b7fe54"}   #api키
queryString = {'query': "아이유"}    # 검색 키워드 
#                                     키 : 키값              권한  
r = requests.get(url, headers=header, params=queryString)

for i in r.json()["documents"] :
    print (i["title"] ) 
    print (i["url"])
    print (i["datetime"])
    print (i["contents"])


