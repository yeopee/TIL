from django.urls import path
from .import views as boards_views
urlpatterns = [
    #게시판의 메인페이지 , 전체 리스트 페이지 
    path('',boards_views.index),
    #게시판에 새 글을 작성 하는 페이지
    path('create',boards_views.create),
    path('new/',boards_views.new),
    #게시판 상세 페이지 
    path('<int:id>/',boards_views.show),
    path('<int:id>/edit/',boards_views.edit),
    path('<int:id>/update/',boards_views.update),   
    path('<int:id>/delete/',boards_views.delete)

    
]

