# Generated by Django 2.1.5 on 2022-05-16 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thereviewguides', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('question', models.CharField(max_length=5000)),
            ],
        ),
    ]
