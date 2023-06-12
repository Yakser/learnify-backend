from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from news.models import News
from news.serializers import NewsDetailSerializer, NewsListSerializer


class NewsList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetail(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
