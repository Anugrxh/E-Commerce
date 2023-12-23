# Generated by Django 4.2.4 on 2023-10-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_signupdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]