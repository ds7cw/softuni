# Generated by Django 5.0.1 on 2024-02-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('personal_photo', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
