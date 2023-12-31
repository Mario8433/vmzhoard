# Generated by Django 4.2.7 on 2023-11-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("text", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="text",
            name="author",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="text",
            name="date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="text",
            name="entry",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="text",
            name="link",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="text",
            name="title",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="text",
            name="translator",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="text",
            name="text",
            field=models.TextField(null=True),
        ),
    ]
