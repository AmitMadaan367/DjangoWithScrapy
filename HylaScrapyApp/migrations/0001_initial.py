# Generated by Django 4.0.5 on 2022-06-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('url', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
