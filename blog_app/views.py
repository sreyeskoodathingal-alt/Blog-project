from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Blog , Command
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
# Create your views here.


def greetings(request):
    return HttpResponse("hello and welcome to my blog page")

def basic(request):

    data_set = [{'name':'john','place':'manjeri','age':33},
                {'name':'mohan','place':'calicut','age':43},
                {'name':'manu','place':'wandoor','age':26}]

    mark = 30
    
    username = 'john'
    
    context = {'data':data_set,'username':username,'mark':mark}
    
    return render(request,'basic.html',context)

def home(request):

    blog = Blog.objects.all()
    context = {'blog':blog}
    return render(request,'home.html',context)

def create_blog(request):

    if request.method == 'POST':
        title_data  = request.POST.get('title')
        content_data = request.POST.get('content')
        year_data = request.POST.get('year')
        image_data = request.FILES.get('image')

        blog = Blog.objects.create(title = title_data, content = content_data, year = year_data , image=image_data)
        blog.save()
        return redirect('home')

    return render(request, 'create_blog.html')

def update_blog(request,blog_id): 

    blog = Blog.objects.get(id = blog_id)
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        year = request.POST.get('year')
        image = request.FILES.get('image')

        blog.title = title
        blog.content = content
        blog.year = year
        blog.image = image

        blog.save()
        return redirect('home')
    
    context = {'blog':blog}
    return render(request, 'update_blog.html',context)


def delete_blog(request, blog_id):

    blog = Blog.objects.get(id = blog_id)
    blog.delete()
    return redirect('home')


def detail_blog(request, blog_id):

    blog = Blog.objects.get(id = blog_id)
    command_list = Command.objects.filter(blog = blog)
    if request.method== 'POST':

        command= request.POST.get('command')
        name=request.POST.get('name')

        command_data = Command.objects.create(name= name , command = command , blog= blog)
        command_data.save()

    
    context = {'blog':blog, 'command': command_list}
    return render(request, 'detail_blog.html', context)


def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{
                "error":'username already exist'
            })
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('login')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password

        )

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            return render(request, 'login.html',{
                'error': 'Invalid username or password'
            })
        


    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

    