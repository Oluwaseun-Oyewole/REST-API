from django.urls import path, include
from . import views
from rest_tutorial.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('', views.index, name='index'),
    # path('detail/<int:pk>/', views.detail, name='detail'),
    # path('', views.ArticleApiView.as_view(), name='Articleapiview'),
    # path('detail/<int:article_id>/', views.ArticleDetailView.as_view(), name='Articledetailview'),
    # path('generic/article/<int:id>/', views.GenericApiView.as_view(), name='generic'),
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]