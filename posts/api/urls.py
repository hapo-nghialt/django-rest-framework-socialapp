from django.conf.urls import url
from .views import (
    PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView
)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\d]+)/$', PostDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\d]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
]
