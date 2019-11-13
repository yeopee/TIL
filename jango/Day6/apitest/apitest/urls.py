"""apitest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kakao_api import views as kakao_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #주소 검색하는 페이지 
    path('kakao/',kakao_views.main),
    #주소 검색 결과 + 키워드 입력 
    path('kakao/address/',kakao_views.find_address),
    #키워드 검색 결과 
    path('kakao/result/',kakao_views.keyword_result)
]
