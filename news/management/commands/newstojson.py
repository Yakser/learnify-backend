import json

from django.core.management.base import BaseCommand, CommandError

from news.models import News
from news.serializers import NewsListSerializer


class Command(BaseCommand):
    help = "Shows specified news titles"

    def add_arguments(self, parser):
        parser.add_argument("news_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        news_json = []
        for news_id in options["news_ids"]:
            try:
                news = News.objects.get(pk=news_id)
                news_json += [NewsListSerializer(news).data]
            except News.DoesNotExist:
                raise CommandError(f"News with id {news_id} does not exist!")
        self.stdout.write(self.style.SUCCESS(json.dumps(news_json)))
