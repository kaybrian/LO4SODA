from django.urls import path 
from .views import * 


urlpatterns = [
    path('', IndexView.as_view(), name="books_index"),
    path('<int:id>/', GetBookDetails.as_view(),name="books_detail"),
    path('about/', about, name="about"),
    path('create/', Create.as_view(), name="create_book")
]


app_name ="books"