# Generated by Django 4.0.1 on 2022-02-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_blog_goal_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='goal_at',
            field=models.DateTimeField(default='0000-00-00T00:00:00.677268'),
        ),
    ]
