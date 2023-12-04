from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

    '''
    For created_on, the DateTimeField takes the argument auto_now_add=True. This assigns the current date and time to this field whenever you create an instance of this class.
    '''
    '''
    For last_modified, the DateTimeField takes the argument auto_now=True. This assigns the current date and time to this field whenever an instance of this class is saved. That means whenever you edit an instance of this class, date_modified is updated.
    '''
    
    '''
    Here we link your models for categories and posts in such a way that you can assign many categories to many posts. Django provides a ManytoManyField field type for this kind of relationship.
    '''


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

   
    '''
    we use another relational field, the ForeignKey field. This is similar to the ManyToManyField but instead defines a many-to-one relationship. The reasoning behind this is that many comments can be assigned to one post. But we can’t have a comment that corresponds to many posts.
    '''

    '''
    The ForeignKey field takes two arguments. The first is the other model in the relationship—in this case, Post. The second tells Django what to do when a post is deleted. If a post is deleted, then we don’t want the comments related to it hanging around. Instead, we delete the comments as well. That’s what on_delete=models.CASCADE is for.
    '''


    # we face some prblm after adding our post and category from django admin site. so add some code in models so that it fixes all

    '''
    Just like with common Python classes, you can add a .__str()__ method to model classes to provide a better string representation of your objects. For categories, you want to display the name. For posts, you want the title. For comments, show the name of the commenter and the post that they’re commenting on.

    To fix the incorrect plural form of your Category class, you add a Meta class to control the plural name of the class. By default, Django just adds a lowercase s at the end of a model name. For the plural of post, this works perfectly. For categories, you need to explicitly define verbose_name_plural with the correct spelling.
    '''
