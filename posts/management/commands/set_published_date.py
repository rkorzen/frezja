from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
import random
import pytz
from faker import Faker
fake = Faker("pl_PL")

from posts.models import Post


class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument("date_str", type=str, default=timezone.now(), help="Date")

    def handle(self, *args, **options):

        date_str = options.get("date_str")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        tz = pytz.timezone("UTC")
        date = tz.localize(date)
        self.stdout.write(f"Setting date to posts...")

        posts = Post.objects.all()
        posts = random.choices(posts, k=10)
        for post in posts:
            post.is_published = True
            post.publication_date = date
            post.save()

        self.stdout.write("Done!")