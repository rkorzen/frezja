# Generated by Django 4.2.13 on 2024-06-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_alter_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="publication_date",
            field=models.DateTimeField(null=True),
        ),
    ]
