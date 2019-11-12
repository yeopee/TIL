from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
def opgg(request):
    #소환사명을 입력할 입력창을 만듣다. 


    return render(request,'opgg.html')

def result(request):
    #op.gg 를 크롤링해서 입력된 소환사에 대한 전적 정보를 가져온다 
    
    name = request.GET['nickname']
    url =f'https://www.op.gg/summoner/userName={name}'
  
    response = requests.get(url)
    html= BeautifulSoup(response.text,'html.parser')
    if html.select_one('span.WinLose .wins') is None:
        result ={
            'msg':'소환사가 없거나 언랭입니다.'
        }

    else:
        result = {
            'name':name,
            'win':html.select_one('span.WinLose .wins').text,
            'lose':html.select_one('span.WinLose .losses').text,
            'ratio':html.select_one('span.WinLose .winratio').text
        }
    
    return render(request,'ratio.html',result)