from rest_framework.generics import ListAPIView

from blog.models import BlogModel
from .serializers import BlogSerializers


class BlogAPIView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
