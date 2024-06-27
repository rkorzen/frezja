import requests
from io import BytesIO
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker
from photos.models import Photo

fake = Faker("pl_PL")


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "n", type=int, default=10, help="Number of photos to generate"
        )

    def handle(self, *args, **options):

        n = options.get("n")
        statuses = ["published", "banned", "pending"]

        for _ in range(
            n
        ):  # Adjust the range for the number of photos you want to create
            title = fake.sentence()
            opis = fake.text()
            status = fake.random.choice(statuses)
            width = fake.random_int(min=200, max=800)
            height = fake.random_int(min=200, max=800)

            response = requests.get(
                f"https://picsum.photos/{width}/{height}", stream=True
            )
            response.raise_for_status()  # Ensure we notice bad responses

            photo = Photo(title=title, opis=opis, status=status)

            photo_filename = f"{fake.uuid4()}.jpg"
            photo.img.save(photo_filename, File(BytesIO(response.content)))
            photo.save()

            self.stdout.write(
                self.style.SUCCESS(f'Successfully created photo "{title}"')
            )
