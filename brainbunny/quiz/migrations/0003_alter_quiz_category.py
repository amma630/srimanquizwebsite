# Generated by Django 5.0.7 on 2024-09-05 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_category_options_alter_quiz_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.category'),
        ),
    ]
