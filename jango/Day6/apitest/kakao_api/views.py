from django.shortcuts import render
import requests
import json
# Create your views here.

def main(request):
    #주소를 검색 하는 페이지

    return render(request,'kakao_main.html')

def find_address(request):
    #main에 검색한 검색어를 카카오 로컬 검색으로 결과를 보여주는 페이지 +키워드를 입력하는 페이지 
    url =f'https://dapi.kakao.com/v2/local/search/address.json'
    key ='4874c8c3ccc19478badf6e9070a52f64'
    q = request.GET['address']
    params={
        'query':q,
        'size':16,

    }
    headers= {
        'Authorization' : f'KakaoAK {key}'
    }

    response = requests.get(url, params=params,headers=headers)



    address_data = json.loads(response.text)
    context= {
        "result":address_data["documents"]
    }

    return render(request,'kakao_address.html',context)

def keyword_result(request):
    #키워드를 입력하는 곳에서 입력한 키워드가 position(위,경도) 좌표를 추출해서 kakao api에 요청을 보낸다.
    keyword = request.GET['keyword']
    position= request.GET['position']
    gps_x = position.split(',')[0]
    gps_y = position.split(',')[1]
    url ='https://dapi.kakao.com/v2/local/search/keyword.json'
    key = '4874c8c3ccc19478badf6e9070a52f64'
    params={
        'query': keyword,
        'x':gps_x,
        'y':gps_y,

    }
    headers={
        'Authorization' : f'KakaoAK {key}'
    }
    response= requests.get(url, params=params,headers=headers)
    context = {
        'result':json.loads(response.text)["documents"]
    }
    return render(request,'keyword_result.html',context)