# Generated by Django 4.2.4 on 2023-09-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drafts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('recipient', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
