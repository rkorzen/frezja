import random
from datetime import datetime

import pytz
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from posts.models import Post

fake = Faker("pl_PL")


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("date_str", type=str, default=timezone.now(), help="Date")

    def handle(self, *args, **options):
        date_str = options.get("date_str")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        tz = pytz.timezone("UTC")
        date = tz.localize(date)
        self.stdout.write("Setting date to posts...")

        posts = Post.objects.all()
        posts = random.choices(posts, k=10)
        for post in posts:
            post.is_published = True
            post.publication_date = date
            post.save()

        self.stdout.write("Done!")
