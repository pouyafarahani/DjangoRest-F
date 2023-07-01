from django.urls import path

from .views import BlogAPIView


urlpatterns = [
    path('', BlogAPIView.as_view(), name='api_blog'),
]
