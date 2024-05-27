from django.urls import path
from .views import UserCreate, UserDetail, SentimentAnalysisListCreate

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('<str:username>/', UserDetail.as_view(), name='user_detail'),
     path('<str:username>/sentimentanalysis/', SentimentAnalysisListCreate.as_view(), name='sentiment_analysis'),
]
