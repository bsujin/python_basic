import requests
 
 
def getLatLng(address):
    result = ""
 
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = 'e68603d86178518e0161a32013b7fe54'
    
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
    r = requests.get(url, headers=header)
 
    if r.status_code == 200:
        result_address = r.json()["documents"][0]["address"]
        
        result = result_address["y"], result_address["x"]
    else:
        
        result = "ERROR[" + str(r.status_code) + "]"
    
    return result
 
def getKakaoMapHtml(address_latlng):
    rest_api_key = 'e68603d86178518e0161a32013b7fe54'
    result = ""
    result = result + "<div id='map' style='width:1200px;height:1000px;display:inline-block;'></div>" + "\n"
    result = result + "<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + rest_api_key + "'></script>" + "\n"
    result = result + "<script>" + "\n"
    result = result + "    var container = document.getElementById('map'); " + "\n"
    result = result + "    var options = {" + "\n"
    result = result + "           center: new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ")," + "\n"
    result = result + "           level: 3" + "\n"
    result = result + "    }; " + "\n"
    result = result + "    var map = new kakao.maps.Map(container, options); " + "\n"
    
    result = result + "    var markerPosition  = new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ");  " + "\n"
    result = result + "    var marker = new kakao.maps.Marker({position: markerPosition}); " + "\n"
    result = result + "    var zoomControl = new kakao.maps.ZoomControl(); " + "\n"
    result = result + "    map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT); " + "\n"
    result = result + "    var mapTypeControl = new kakao.maps.MapTypeControl(); " + "\n"
    result = result + "    map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT); " + "\n"
    
    result = result + "    marker.setMap(map); " + "\n"
 
    result = result + "</script>" + "\n"
    
    #파일생성시 자동으로 - html 생성
    with open("C:/workspace_python/kakao/WebContent/maps.html","w") as html_file:
        html_file.write(result)
    return result
 
# main()
if __name__ == "__main__":
    address = "대전광역시 중구 대흥동 500-5"
    
    # 카카오 REST API로 좌표 구하기
    address_latlng = getLatLng(address)
 
    # 좌표로 지도 첨부 HTML 생성
    if str(address_latlng).find("ERROR") < 0:
        maphtml = getKakaoMapHtml(address_latlng)
        
        print(maphtml)
    else:
        print("[ERROR]getLatLng")
 


