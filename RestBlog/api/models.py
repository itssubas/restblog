from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length=250, blank=False, unique=True)
	posted_on = models.DateTimeField(auto_now_add=True)
	edited_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	tags = models.CharField(max_length=20, blank=False)