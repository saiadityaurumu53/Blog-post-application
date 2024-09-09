from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

"""
Here, 
1. the post is associated with the User and hence we are going to use the User model
2. Also, when we make a post we also need to timestamp it and hence import timezone
3. Now, we are going to make a category for this as each post is going to be a part of the category
"""

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published' , 'Published'),
    )

    #used to flash out different items here
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,  #if we delete a category then we will delete all the posts in a category
        default=1
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published') #utilize this to identify each post 
    #instead of using the ID for each post we are gonna use the slug 
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )  #either it can be draft or published

    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager


    class Meta:
        #by default we wanna display the data in either ascending or descending 
        ordering = ('-published', )

    def __str__(self) -> str:
        return self.title
