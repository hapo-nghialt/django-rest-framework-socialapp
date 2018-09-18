from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            'content',
            'slug'
        ]


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
