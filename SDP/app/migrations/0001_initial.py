# Generated by Django 3.1.6 on 2021-05-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('restaurant_id', models.IntegerField(unique=True)),
                ('area', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]
