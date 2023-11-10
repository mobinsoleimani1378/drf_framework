from rest_framework import serializers
from .models import Article

class ArticleSer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=150)
    status = serializers.BooleanField(required=False)
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)