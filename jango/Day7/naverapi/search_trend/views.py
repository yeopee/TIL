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