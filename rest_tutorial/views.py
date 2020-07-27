from .models import Article
from django.http import HttpResponse
from rest_tutorial.serializers import ArticleSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_tutorial.serializers import ArticleSerializers
from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication,
                                            TokenAuthentication
                                           )
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


#  Generic Viewsets and mixins
# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializers
#     queryset = Article.objects.all()



# Model Viewsets and mixins
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()




    # viewsets in django rest api views
    # """
    # A simple ViewSet for listing or retrieving users.
    # """
    # def list(self, request):
    #     article = Article.objects.all()
    #     serializer = ArticleSerializers(article, many=True)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     serializer = ArticleSerializers(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset, pk=pk)
    #     serializer = ArticleSerializers(article)
    #     return Response(serializer.data)
    #
    # def update(self, request, pk=None):
    #     article = Article.objects.get(pk=pk)
    #     serializer = ArticleSerializers(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Generic api views and authentications
# class GenericApiView(generics.GenericAPIView,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializers
#     queryset = Article.objects.all()
#
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     lookup_field = 'id'
#
#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     def put(self, request, id=None):
#         return self.update(request, id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)

# Class based django rest api views
# class ArticleApiView(APIView):
#     def get(self, request):
#             articles = Article.objects.all()
#             serializer = ArticleSerializers(articles, many=True)
#             return Response(serializer.data)
#
#     def post(self, request):
#             serializer = ArticleSerializers(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetailView(APIView):
#     def get_object(self, request, article_pk):
#         try:
#             return Article.objects.get(pk=article_pk)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, article_id):
#         article = Article.objects.get(id=article_id)
#         serializer = ArticleSerializers(article)
#         return Response(serializer.data)
#
#     def put(self, request, article_id):
#                 article = Article.objects.get(id=article_id)
#                 serializer = ArticleSerializers(article, data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, article_id):
#             article = self.get_object(article_id)
#             article.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)





# Function based django rest api views

# @api_view(['GET', 'POST'])
# def index(request):
#
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializers(articles, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ArticleSerializers(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def detail(request, pk):
#         """
#         Retrieve, update or delete a code snippet.
#         """
#         try:
#             snippet = Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#         if request.method == 'GET':
#             serializer = ArticleSerializers(snippet)
#             return Response(serializer.data)
#
#         elif request.method == 'PUT':
#             serializer = ArticleSerializers(snippet, data=request.data)
#
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
#                             )
#         elif request.method == 'DELETE':
#             snippet.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
