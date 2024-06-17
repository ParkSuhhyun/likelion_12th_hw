# Generated by Django 5.0.3 on 2024-05-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_comment_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='comments', to='main.tag'),
        ),
    ]
