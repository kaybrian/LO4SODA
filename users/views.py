from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import random




def generate_username(username):
    names = []
    for i in range(3):
        rand_name = username+str(random.randint(1,10))
        names.append(rand_name)
    return names           

def create_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        confirm_password = request.POST["confirm_password"]
        password = request.POST["password"]

        if password != confirm_password:
            messages.info(
                request, 
                'Passwords dont Match, Please check your passwords and try again '
            )
            return render(request, "users/create.html")
        else:
            user = User.objects.filter(username=username).exists()
            if user:
                names = generate_username(username)
                
                messages.info(
                    request, 
                    f'Sorry User with this username - {username} already exits'
                )
                messages.info(
                    request,
                    f'please try to use any of these names {names}'
                )
                return render(request, "users/create.html")
            else:
                new_user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                new_user.set_password(password)
                new_user.save()
                return HttpResponse("New user was created ")
    
    else:
        return render(request, "users/create.html")



def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user_vai = User.objects.filter(username=username).exists()
        
        if user_vai:
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('books:books_index')
            else:
                messages.info(
                    request, 
                    f'Invalid Username or password '
                )
                return render(request, 'users/login.html')

        else:
           
            messages.info(
                request, 
                f'''
                    Sorry User with this username - {username} dont exits
                '''
            )
            
            return render(request, 'users/login.html')
        
    else:
        
        return render(request, 'users/login.html')
            
       
       
def logoutuser(request):
    logout(request)
    messages.success(
        request, 
        f'Logged out Successful '
    )
    return redirect('users:login')