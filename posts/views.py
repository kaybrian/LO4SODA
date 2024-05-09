from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("You are connected to the server")


def create_post(request):
    return HttpResponse("You are going to create a post")