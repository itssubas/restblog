from rest_framework import generics
from .serializers import BlogPostSerializer
from .models import BlogPost

class CreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new blogpost."""
		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This handles GET, PUT, DELETE requests"""
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer