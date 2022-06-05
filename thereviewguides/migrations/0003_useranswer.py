# Generated by Django 2.1.5 on 2022-05-17 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thereviewguides', '0002_userquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAnswer', to='thereviewguides.UserQuestion')),
            ],
        ),
    ]
