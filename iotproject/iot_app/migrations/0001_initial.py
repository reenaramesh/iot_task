# Generated by Django 4.0 on 2024-05-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(default='', max_length=70)),
                ('device_type', models.CharField(default='', max_length=200)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('data', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
