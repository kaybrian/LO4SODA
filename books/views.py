from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .models import Book
from .serializer import BookSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class IndexView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = Book.objects.all()
    
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        # try:
        #     books = Book.objects.all()
        #     serializer = BookSerializer(books, many=True)
        #     return Response(serializer.data)
        # except:
        #     return Response({"Message": "Yoooo man we crushed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    



@login_required(login_url='users:login')
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)
    
   
class GetBookDetails(APIView):
    serializer_class =BookSerializer
    queryset = Book.objects.all()
    
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Message": "Yoooo man we crushed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

            

@login_required(login_url='users:login')
def about(request):
    return HttpResponse("This is the about us page")

class Create(APIView):
    serializer_class =BookSerializer
    queryset = Book.objects.all()

    def post(self, request, format=None):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Message": "Yoooo man we crushed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
