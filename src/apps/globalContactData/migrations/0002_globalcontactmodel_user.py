# Generated by Django 3.2.4 on 2023-02-27 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globalContactData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalcontactmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_contact_database', to=settings.AUTH_USER_MODEL),
        ),
    ]
