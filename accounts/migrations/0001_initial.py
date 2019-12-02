# Generated by Django 2.2.7 on 2019-12-01 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('status', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
