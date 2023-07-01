from rest_framework import serializers

from blog.models import BlogModel


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'
