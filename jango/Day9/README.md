



- # Day 09

- 오늘이야기 : URL namespace 설정을 해보자 !!!!! django admin 만져보자

pip install pylint

pip install pylint django

컴퓨터 속성-고급시스템설정-고급-환경변수-PATH(python 녀석들만)복사

vs code ctl+p >user setting 의 python:python path에 붙여넣기

 \# CRUD 

​    \# C -> new, create

​    \# R -> index, show

​    \# U -> edit, update

​    \# D -> Delete

​    url namespace

​    \#각각의 url에 별명을 지어줘서 html 파일에서 사용하는 링크를 추가적으로 바꾸지 않고,url.py에서만 수정하면 html 파일에서도 링크 수정이 반영되게끔 함

urls.py

```python
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [

path('', views.index, name="index"),
    path('<int:id>/', views.show,name="show"),
    path('new/', views.new,name="new"),
    path('create/', views.create,name="create"),
    path('<int:id>/edit/', views.edit,name="edit"),
    path('<int:id>/update/', views.update,name="update"),
    path('<int:id>/delete/', views.delete,name="delete"),
    ]
```



index.html

```html
{% extends 'base.html' %}
{% block content %}
<div class="container">
    <table class="table text-center">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Title</th>
                <th scope="col">Creator</th>
                <th scope="col">Created At</th>
            </tr>
        </thead>
        <tbody>
            {% for article in articles%}
            <tr>
                <th scope="row">{{article.id}}</th>
                <td><a href="{% url 'articles:show' article.id %}">{{article.id}}</a></td>
                <td>{{article.creator}}</td>
                <td>{{article.datetime_to_string}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <a href="{% url 'articles:new' %}" class="btn btn-info">새글쓰기</a>
</div>
{% endblock %}
```

















# restful api 

| 역활   | Request-method | end-point             | views(function) |
| ------ | -------------- | --------------------- | --------------- |
| create | GET            | /articles/new         | new             |
| create | POST           | /articles/            | create          |
| read   | GET            | /articles/<id>        | show            |
| read   | GET            | /articles             | index           |
| update | GET            | /articles/<id>/edit   | edit            |
| update | POST           | /articles/<id>/update | update          |
| delete | POST(DELETE)   | /articles/<id>/delete | delete          |
|        |                |                       |                 |
|        |                |                       |                 |
|        |                |                       |                 |
|        |                |                       |                 |





GET - 조회 

POST - DB에 반영 ..!!





admin 사이트를 수정해보자 

```
*powershell 에서 
python manage.py createsuperuser
완성 
```

