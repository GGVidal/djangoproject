from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
]