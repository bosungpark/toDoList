# Generated by Django 4.0.1 on 2022-02-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_blog_goal_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='goal_at',
            field=models.CharField(default='목표날짜를 정해놓고 하는 것은 아님.', max_length=100),
        ),
    ]
