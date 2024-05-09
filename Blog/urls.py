from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administrators-wmhs/', admin.site.urls),
    path('', include('books.urls')),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    
    path('api-auth/', include('rest_framework.urls'))
]


# WMHS@2024

#  nbvcxzwe are going to try to build a simple api to 
# show all the books in our project 