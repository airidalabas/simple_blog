# Generated by Django 4.1.7 on 2023-03-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Kavos maniakai', max_length=255),
        ),
    ]