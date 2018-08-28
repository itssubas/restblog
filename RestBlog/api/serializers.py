from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
	"""To map model instance into JSON format"""
	class Meta:
		model = BlogPost
		fields = ('id', 'title', 'posted_on', 'edited_on', 'content', 'tags')
		read_only_fields = ('posted_on', 'edited_on')