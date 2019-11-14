# DAY07

- 네이버 api를 이용하자. 	

USE_TZ : ORM 이 기본적으로 UTC로 한다 , 

언어 세팅

- I18 N = I랑 N 은 18개 있다 . 국제화  
- ㅣ10 N :  지역화 설정 

## NAVER API

요청 URL

ㅣhttps://openapi.naver.com/v1/datalab/search 

프로토콜

HTTPS 

#### HTTP 메서드 

POST

#### 파라미터 

파라미터를 JSON 형식으로 전달합니다.



|        파라미터         |     타입      | 필수 여부 |                             설명                             |
| :---------------------: | :-----------: | :-------: | :----------------------------------------------------------: |
|        startDate        |    string     |     Y     | 조회 기간 시작 날짜(`yyyy-mm-dd` 형식). 2016년 1월 1일부터 조회할 수 있습니다. |
|         endDate         |    string     |     Y     |            조회 기간 종료 날짜(`yyyy-mm-dd` 형식)            |
|        timeUnit         |    string     |     Y     |   구간 단위 - `date`: 일간 - `week`: 주간 - `month`: 월간    |
|      keywordGroups      |  array(JSON)  |     Y     | 주제어와 주제어에 해당하는 검색어 묶음 쌍의 배열. 최대 5개의 쌍을 배열로 설정할 수 있습니다. |
| keywordGroups.groupName |    string     |     Y     |          주제어. 검색어 묶음을 대표하는 이름입니다.          |
| keywordGroups.keywords  | array(string) |     Y     | 주제어에 해당하는 검색어. 최대 20개의 검색어를 배열로 설정할 수 있습니다. |
|         device          |    string     |     N     | 범위. 검색 환경에 따른 조건입니다. - 설정 안 함: 모든 환경 - `pc`: PC에서 검색 추이 - `mo`: 모바일에서 검색 추이 |
|         gender          |    string     |     N     | 성별. 검색 사용자의 성별에 따른 조건입니다. - 설정 안 함: 모든 성별 - `m`: 남성 - `f`: 여성 |
|          ages           | array(string) |     N     | 연령. 검색 사용자의 연령에 따른 조건입니다. - 설정 안 함: 모든 연령 - `1`: 0∼12세 - `2`: 13∼18세 - `3`: 19∼24세 - `4`: 25∼29세 - `5`: 30∼34세 - `6`: 35∼39세 - `7`: 40∼44세 - `8`: 45∼49세 - `9`: 50∼54세 - `10`: 55∼59세 - `11`: 60세 이상 |



#### 참고 사항 

API를 요청할 때 다음 예와 같이 HTTP 요청 헤더에 [클라이언트 아이디와 클라이언트 시크릿](https://developers.naver.com/docs/common/openapiguide/appregister.md#클라이언트-아이디와-클라이언트-시크릿-확인)을 추가해야 합니다.

```sh
> POST /v1/datalab/search HTTP/1.1
> Host: openapi.naver.com
> User-Agent: curl/7.49.1
> Accept: */*
> Content-Type: application/x-www-form-urlencoded; charset=UTF-8
> X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 클라이언트 아이디 값}
> X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 클라이언트 시크릿 값}
> Content-Length: 360
```



naver api 

````python

from django.shortcuts import render
import requests
import json
# Create your views here.
def search(request):
    #검색어를 입력 하는곳 

    return render(request,'search.html')

def result(request):
    #검색어에 대한 검색 트렌드를 받아 보는 곳 
    
    start_date = request.GET['search_start_date']
    end_date = request.GET['search_end_date']
    time_unit = request.GET['search_time_unit']
    group_name = request.GET['search_group_name']
    keywords = request.GET['search_keywords'].split(',')
    query = {
            "startDate": start_date,
            "endDate": end_date,
            "timeUnit": time_unit,
            "keywordGroups": [
            {
            "groupName": group_name,
            "keywords": keywords
            }
        ]
  
        }
    url = 'https://openapi.naver.com/v1/datalab/search'
    client_id ='#'
    clirnt_secret='#'
    headers={
         'X-Naver-Client-Id' : client_id,
         'X-Naver-Client-Secret':clirnt_secret
    }
    
    params=json.dumps(query)

    response = requests.post(url,data=params,headers=headers)    

    result=response.text

    context= {
       
        'result':result
         }

  
    
    return render(request,'result.html',context)
````



serch.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

    <h1>검색어를 입력 하세요 . </h1>
    <form action="/search/result">
        <label>기간 시작날짜</label>
        <input type="date" name="search_start_date"><br/>
        <label>기간 종료날짜</label>
        <input type="date" name="search_end_date"><br/>
        <label>주간날짜</label>
        <select name="search_time_unit">
            <option value="date">일간</option>
            <option value="week">주간</option>
            <option value="month">월간</option>
        </select>
        </br>
        <label>검색어 그룹명</label>
        <input type="text" name="search_group_name">
        </br>
        <label>크렌드를 볼 검색어 목록(여러개의 검색어 의 경우 ','로 구분된다.</label>
        </br>
        <input type="text" name="search_keywords">
        </br>
        <input type="submit" value="검색">
    </form>
</body>
</html>
```

result.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {{result}}
</body>
</html>
```

# class

person  - 테이블 



# ORM

DB 에  SQL 문을 쉽게 넣을수 있게 해주는 녀석입니다. 

ORM 약속을 잘 지키면 됩니다. 

python manage.py    migraton - 파이선 파일로 DB 구조로 만들 준비 

python manage.py    migrate (명령어)  db에 반영 

shell에서 파이썬 하기 

```
shell 에서 명령어
python manage.py shell
b1=Board()
*insert
b1.title ="내용"
*save 전까지 db에 입력이 안된다. 
b1.save()
*저장된 오브젝트 모두 부른다.select all 
board.obeject.all() 
b2 = Board.objects.filter(title='제목').first()
#원하는 row 검색, 배열로 리턴 한다. 
```

























