from django.urls import path
from . import views as account_views
app_name='accounts'

urlpatterns = [
path('login/', account_views.login,name="login"),
path('logout/', account_views.logout,name="logout"),
path('signup/', account_views.signup,name="signup")
]