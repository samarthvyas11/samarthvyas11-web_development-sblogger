from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from home.models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    user = request.user
    context = {"user":user}
    return render(request,'home/home.html',context)

def about(request):
    return render(request,'home/about.html')


def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) <2 or len(email)< 3 or len(phone)<10 or len(content) <4:
            messages.error(request,"All Informations are not provided")
        else:    
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Information successfully recorded")
    return render(request,'home/contact.html')


def search(request):
    query=request.GET['search']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)      


def handlesignup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        # if len(username)>10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your sBlogger account has been successfully created")

    else:
        print("404- Not Found")    
    return redirect('home')    


def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]


        user = authenticate(username=loginusername, password = loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request,"Invalid Username or password !!!!! Try again")
            return redirect("home")

    return HttpResponse("404-Not found")   
    
def handlelogout(request):
    
        logout(request)
        messages.success(request,"Successfully Logged out")  
        return redirect("home")      


def createblog(request):
    return render(request,"blog/createblog.html")