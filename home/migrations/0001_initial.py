# Generated by Django 5.1.1 on 2024-09-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=15)),
                ('about_text', models.TextField(max_length=500)),
                ('projects_title', models.CharField(blank=True, max_length=15, null=True)),
                ('projects_text', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]