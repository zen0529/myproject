from rest_framework import generics, permissions
from .models import CustomUser, SentimentAnalysis
from .serializers import SentimentAnalysisSerializer, UserSerializer
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    
class SentimentAnalysisListCreate(generics.ListCreateAPIView):
    serializer_class = SentimentAnalysisSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs['username']
        return SentimentAnalysis.objects.filter(user__username=username)

    def perform_create(self, serializer):
        username = self.kwargs['username']
        user = CustomUser.objects.get(username=username)
        serializer.save(user=user)