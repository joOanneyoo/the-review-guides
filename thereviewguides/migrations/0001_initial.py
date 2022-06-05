# Generated by Django 2.1.5 on 2022-04-30 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('author', models.CharField(max_length=50)),
                ('yearReleased', models.IntegerField()),
                ('description', models.CharField(max_length=10000)),
                ('img_url', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='booklist',
            name='genre_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Booklist', to='thereviewguides.Genre'),
        ),
    ]
