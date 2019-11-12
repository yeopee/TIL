from django.shortcuts import render

# Create your views here.
def pubgopgg(request):

    return render(request,'pubgopgg.html')

def result(request):

    return render(request,'pubgratio.html')