# Generated by Django 5.0.3 on 2024-05-12 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='tags',
        ),
    ]
