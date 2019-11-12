from django.shortcuts import render
import requests
# Create your views here.
def ascii(request): 
    #입력 하고자 하는 text를 받아야함
    #artii에서 제공하느 폰트중 선택
    
    url = 'http://artii.herokuapp.com/fonts_list'
    response = requests.get(url)
    fonts_list = response.text.split('\n')

    context = {
        'fonts': fonts_list
    }


    return render(request,'ascii.html',context)
def result(request):
    #ascii에서 입력한 텍스트와 폰트를
    #astii에 보내서 결과값을 받아서 보내줌
    font = request.GET['font']
    text = request.GET['text']

    url= f'http://artii.herokuapp.com/make?font={font}&text={text}'
    response = requests.get(url)
    context= {
        'result':response.text
    }
    return render(request,'result.html',context)