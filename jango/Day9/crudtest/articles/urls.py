from django.contrib import admin
from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    # CRUD 
    # C -> new, create
    # R -> index, show
    # U -> edit, update
    # D -> Delete
    #url namespace
    #각각의 url에 별명을 지어줘서 html 파일에서 사용하는 링크를 추가적으로 바꾸지 않고,url.py에서만 수정하면 html 파일에서도 링크 수정이 반영되게끔 함
    path('', views.index, name="index"),
    path('<int:id>/', views.show,name="show"),
    path('new/', views.new,name="new"),
    path('create/', views.create,name="create"),
    path('<int:id>/edit/', views.edit,name="edit"),
    path('<int:id>/update/', views.update,name="update"),
    path('<int:id>/delete/', views.delete,name="delete"),
]