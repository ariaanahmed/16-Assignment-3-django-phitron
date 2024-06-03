# Generated by Django 5.0.6 on 2024-06-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_categories'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='add_a_category',
        ),
        migrations.AddField(
            model_name='task',
            name='add_a_category',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]
