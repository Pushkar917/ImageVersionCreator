# Generated by Django 3.2.4 on 2023-02-27 14:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalContactModel',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=24, verbose_name='name')),
                ('phone_number', models.CharField(blank=True, max_length=18, verbose_name='phone_number')),
                ('is_spam', models.BooleanField(default=False, help_text='Is this a spam number?', verbose_name='SPAM')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
