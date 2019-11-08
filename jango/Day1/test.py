import requests
#1.요청을 보내기 위한 requests 모듈을 import 한다
#모듈이 없을 경우 'pip install requests'을 실행
url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/fri"
# 해당 url 에 요청을 보낸다
response = requests.get(url)
#해당 응답을 출력
print(response.text)


