from flask import Flask, escape, request
import requests
app = Flask(__name__)
if __name__=='__main__':
    app.run(debug=True)
    #서버를 재시작 할때 새로고침만 해도 갱신이 된다.
@app.route('/')
def index():
    daily_toon_data = {}
    dd='mon'
    url = f"http://webtoon.daum.net/data/pc/webtoon/list_serialized/{dd}"
    data = request_data_from_url(url)
    daily_toon_data[dd]=parse_daum_webtoon_data(data)
    
    return daily_toon_data

    


def request_data_from_url(url):
    # 해당 url 에 요청을 보낸다
    response = requests.get(url)    
    #해당 응답을 출력
    #print(response.text)

    data = response.json()
    return data



def parse_daum_webtoon_data(data):
    toons = []
    for toon in data["data"]:
        #제목의 key는 title
        title = toon["title"]
        #설명의 key는 introduction
        desc = toon['introduction']
        #장르의 위치는 'cartoon' 안에 'genre'라는 리스트 안에 'name'이라는key
        genres = []
        for genre in toon["cartoon"]['genres']:
            genres.append(genre["name"])
            
        #print(genres)
        artists = []
        for artist in toon['cartoon']["artists"]:
            artists.append(artist["name"])
        #썸네일 이미지    
        img_url = toon["pcThumbnailImage"]["url"]
        tmp = {
            title : {
                "desc" : desc,
                "writer" : artists,
                "img_url": img_url
            }
        }
        toons.append(tmp)
    return toons

