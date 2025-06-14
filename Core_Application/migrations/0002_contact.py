# Generated by Django 5.0.4 on 2025-02-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core_Application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date', '-time'],
            },
        ),
    ]
