from . import views 
from django.urls import path


urlpatterns = [
    path('create/', views.create_user, name="create_user"),
    path('login/', views.Userlogin, name="login"),
    path('logout/', views.logoutuser, name="logout"),
]

app_name = "users"