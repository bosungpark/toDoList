# Generated by Django 4.0.1 on 2022-02-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_blog_goal_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='tag',
            name='background_color',
            field=models.CharField(default='red', max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text_color',
            field=models.CharField(default='red', max_length=100),
        ),
    ]
