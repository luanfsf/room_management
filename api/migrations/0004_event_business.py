# Generated by Django 4.1.3 on 2022-11-01 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.business'),
        ),
    ]
