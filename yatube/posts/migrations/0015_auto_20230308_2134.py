# Generated by Django 2.2.16 on 2023-03-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20230308_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('created',)},
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique follow',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('author', 'user'), name='unique_follow'),
        ),
        migrations.AlterModelTable(
            name='follow',
            table=None,
        ),
    ]