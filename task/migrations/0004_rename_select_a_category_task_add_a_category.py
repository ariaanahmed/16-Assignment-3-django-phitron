# Generated by Django 5.0.6 on 2024-06-03 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_rename_add_a_category_task_select_a_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='select_a_category',
            new_name='add_a_category',
        ),
    ]
