# Generated by Django 3.0.7 on 2020-06-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_yml', '0003_incoming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='file',
            field=models.BinaryField(),
        ),
    ]
