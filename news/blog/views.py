from django.shortcuts import render

# after creating model
from blog.models import Post, Comment

#after creating forms
from django.http import HttpResponseRedirect
from blog.forms import CommentForm

def blog_home(request):
    return render (request, "blog/homepage.html")

def gallery(request):
    return render(request, "blog/gallery.html")

def aboutus(request):
    return render(request, "blog/aboutus.html")

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
    #after form
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        

    comments = Comment.objects.filter(post=post)

    #before form
    context = {
        "post":post,
        "comments":comments,  
        #after form
        'form':CommentForm(),
    }
    return render(request, "blog/detail.html",context)

    '''
    The primary key (pk) is the unique identifier of a database entry. That means we are requesting a single post with the specific primary key that you provide. 
    '''

    #form
    '''
    In line 3, you import HttpResponseRedirect, which helps you redirect the request in line 22. You’ll have a closer look at line 22 in a moment. First, follow the request through the body of blog_detail().

    Regardless of your request type, you take CommentForm(), which you imported in line 6, and make an instance of it in line 12. That way, you ensure that there’s always an empty form present in your view.

    Then in line 13, you check if you’ve received a POST request. If so, you update form with the data of the POST request in line 14. That’s the data that the user entered into the form.

    After that, you validate the form using .is_valid() in line 15 to check that the user has entered all the fields correctly.

    If the form is valid, then you create a new instance of Comment in lines 16 to 20. You can access the data from the form using form.cleaned_data, which is a dictionary. Before passing in user-submitted data to your database queries, it’s good practice to clean up form data. That way, you make sure that any input is consistent and safe.

    The keys of form.cleaned_data correspond to the form fields, so you can access the author using form.cleaned_data["author"] in line 17 and the comment’s body with form.cleaned_data["body"] in line 18.

    To properly create a Comment object in your database, you must connect it to an existing Post in line 19. You grab the related post with the primary key of the view in line 11.

    Once you’ve created the comment from the form, you save it using .save() in line 21 and redirect the user to the URL that request.path_info contains in line 22. In your case, that’ll be the URL of a blog post.

    This means, in other words, that when you transmit a valid form to blog_detail() with a POST request, then Django will call blog_detail() again after saving your comment. This time, Django will call the view function with a GET request, and the blog post will load with an emptied form and your comment in the list of comments.

    For these GET requests or when the form isn’t valid, the rest of blog_detail() will do this:

    Line 24 queries the database for any existing comments on your post.
    Lines 25 to 29 create the context, including the data for the post, the filtered comments, and the form.
    Line 30 renders the detail.html template with context.
    '''