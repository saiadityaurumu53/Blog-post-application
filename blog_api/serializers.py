"""
Define what kind of data we want to serialize, what data we want to get from the DB, saveinto DB and reyturn it into JSON
"""

from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #Define what model we want
        #then define what kind of data we want to manage within the POST
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')

    