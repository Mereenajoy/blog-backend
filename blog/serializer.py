from rest_framework import serializers
from blog.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields =(
            'userid',
            'title',
            'message'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel

        fields =(
            'name',
            'profile',
            'email',
            'password'
        )