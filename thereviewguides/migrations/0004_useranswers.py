# Generated by Django 2.1.5 on 2022-05-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thereviewguides', '0003_useranswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=5000)),
                ('answer', models.CharField(max_length=5000)),
            ],
        ),
    ]
