# Generated by Django 2.1.5 on 2022-05-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thereviewguides', '0004_useranswers'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=5000)),
                ('answer', models.CharField(max_length=5000)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]
