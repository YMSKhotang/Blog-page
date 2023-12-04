from django.shortcuts import render

# Create your views here.

from blog.models import Post, Comment

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
    '''
    The minus sign (-) tells Django to start with the largest value rather than the smallest. That way, you get the recently created posts first.
    '''

def blog_category(request,category):
    posts = Post.objects.filter(categories__name__contains = category).order_by("-created_on")
    context = {
        "category":category,
        "posts":posts,
    }
    return render(request, "blog/category.html", context)

    '''
    We use a Django Queryset filter. The argument of the filter tells Django what conditions need to be true to retrieve an object. In this case, you only want posts whose categories contain the category with the name corresponding to what’s given in the argument of the view function.
    '''

def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments":comments,  
    }
    return render(request, "blog/detail.html",context)

    '''
    The primary key (pk) is the unique identifier of a database entry. That means we are requesting a single post with the specific primary key that you provide. 
    '''