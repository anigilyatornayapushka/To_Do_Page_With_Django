# Generated by Django 4.1.7 on 2023-03-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_tasks_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
    ]
