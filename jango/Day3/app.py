from flask import Flask, request , render_template
import requests
app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)





@app.route('/')
def index():
    #request.arg ->Dictionary(immutable)
    #클라이언트로 받은 파라미터를 저장 하고 있는 
    student = request.args.get("student")
    return {'hello' : student}

    #/?student=()


@app.route('/daum_webtoon')
def daum_toon_index():
    days = ["mon","tue","wed","thu","fri","sat","sun"] 
    return render_template('daum_webtoon_list.html',days=days )

@app.route('/daum_webtoon/<day>')
def daum_toon(day):
    
    url = f"http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}"
    data = request_data_from_url(url)
    return { day:parse_daum_webtoon_data(data)}



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
