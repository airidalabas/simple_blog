# Generated by Django 4.1.7 on 2023-03-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Puodelis po puodelio', max_length=255),
        ),
    ]
