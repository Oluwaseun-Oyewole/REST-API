from rest_framework import serializers
from django.utils import timezone
from .models import Article


# class ArticleSerializers(serializers.Serializer):
#     author = serializers.CharField(max_length=100)
#     title =serializers.CharField(max_length=100)
#     email = serializers.CharField(max_length=100)
#     date = serializers.DateTimeField(default=timezone.now)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
# #         instance.save()
#         return instance


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
