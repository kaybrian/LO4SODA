
from .views import * 
from django.urls import path 

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_post, name="create"),
    path('add-post/', create_post, name="add-post")
]

# google.com/posts/create
# google.com/posts/add-post