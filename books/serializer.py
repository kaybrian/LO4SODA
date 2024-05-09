from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    
    class Meta: 
        model = Book
        fields = '__all__'