# Generated by Django 2.0.9 on 2018-11-18 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('decription', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='')),
                ('total_events', models.IntegerField(default=40)),
                ('points_events', models.IntegerField(default=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]