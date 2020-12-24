from django.db import models
from django.conf import settings 
from django.utils import timezone
"""
In the below class named post is our model.Model.models says that this is a Post model
Think the class Post as database table:
Author :This is a link to another model.it is the foreign key  will allow us to link our table to another table in the database
Also on delete cascade means when you delete this author.You will have to delete the related info also
title :type is charfield with max 200 characters
text:type is textField. This is for long text without a limit.
date :current date created object from timezone
published date:The date that you publish your post on blog
publish function:Returns the time posted your blog will be saved
In this scenario, when we call __str__() we will get a text (string) with a Post title.
"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

