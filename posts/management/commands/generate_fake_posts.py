from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from faker import Faker
fake = Faker("pl_PL")

from posts.models import Post


class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument("n", type=int, default=10, help="Number of posts to generate")

    def handle(self, *args, **options):
        User = get_user_model()

        u = User.objects.first()
        if not u:
            raise CommandError("No user found - probably there is no one in the database")

        n = options.get("n")
        self.stdout.write(f"Generating fake {n} posts...")

        for _ in range(options.get("n")):
            Post.objects.create(
                title=fake.sentence(nb_words=5),
                content=fake.text(500),
                author=u,
            )

        self.stdout.write("Done!")