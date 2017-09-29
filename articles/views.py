# Create your views here.
from articles.models import Articles
from articles.serializers import ArticlesSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes  = (IsAuthenticated,)
    