from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:room_id>/exit/',views.exit,name="exit"),
    path('<int:room_id>/', views.show, name="room"),
    path('<int:room_id>/messsage',views.chat,name="chat"),
]