# Generated by Django 2.2.16 on 2023-03-09 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20230309_2213'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('author', 'user'), name='unique_follow'),
        ),
    ]
