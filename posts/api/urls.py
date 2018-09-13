from django.conf.urls import url
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^(?P<pk>[\d]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
]
