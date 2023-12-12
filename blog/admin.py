from django.contrib import admin
from blog.models import Category, Comment, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

'''
For the purposes of this tutorial, we don’t need to add any attributes or methods to these classes. Their purpose is to customize what the admin pages show. For this tutorial, the default configuration is enough.
'''