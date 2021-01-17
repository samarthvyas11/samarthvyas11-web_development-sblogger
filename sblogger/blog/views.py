from django.shortcuts import render,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
def bloghome(request):
    allpost = Post.objects.all()
    context = {"allposts":allpost}
    print(allpost)


    return render(request,"blog/bloghome.html",context)
def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    # replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    # replyDict={}
    # for reply in replies:
    #     if reply.parent.sno not in replyDict.keys():
    #         replyDict[reply.parent.sno]=[reply]
    #     else:
    #         replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user}
    #  'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        # post = request.POST.get( Post.sno == postSno)
        post = Post.objects.filter(sno = postSno)[0]
        slug1 =  post.slug 
        # post = post[0]
        # post = Post.objects.filter(sno=postSno


        comment = BlogComment(comment=comment,user=user,post = post)
        comment.save()
        messages.success(request,"Comment added successfully")
    return redirect(f"/blog/{ slug1 }")



def uploadblog(request):
    if request.method == "POST":
        title = request.POST.get("blogtitle")
        content = request.POST.get("contentblog")
        name =  request.POST.get("blogauthor")
        email = request.POST.get("blogemail")
        slug = title
        post = Post(title=title,author=name,email=email,content=content,slug = slug)
        post.save()
    return redirect("/")    




   
# Create your views here.
