from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from news.models import News
from news.serializers import NewsDetailSerializer, NewsListSerializer


class NewsList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
