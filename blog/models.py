from django.db import models
# import the following
from django.utils import timezone
from django.urls import reverse
from django.urls   import reverse_lazy
# from django.core.urlresolvers import reverse

# Create your models here.
# the following model is a database that's going to hold post's on the blog and only the user will have power to approve & delete the post
class Post(models.Model):
    # the 'auth.User' is a super user of django admin interface
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    # the title of the post
    title = models.CharField(max_length=200)
    # the actual post 'text information'
    text = models.TextField()
    # each post have time when it is created therefore i am going to create one here
    created_date = models.DateTimeField(default=timezone.now())
    # the published date is set to be blank up until it is aproved
    published_date = models.DateTimeField(blank=True,null=True)

    # the followingmethod is here to set the date of when the post has been published
    def publish(self):
        self.published_date= timezone.now()
        self.save()
# this method will be linked with a button to approve the users comment
    def approved_comments(self):
        return self.comment.filter(approved_comment=True)

# after the user's comment have been approved , the user willbe then redirected into another page
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()
# this method will redirect a user to the main page after pasting a comment

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
