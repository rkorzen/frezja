# Generated by Django 4.2.13 on 2024-06-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0002_alter_tag_slug"),
        ("posts", "0006_post_publication_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="publication_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="tags.tag"
            ),
        ),
    ]
