# Generated by Django 3.0 on 2019-12-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_auto_20191211_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TUserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('profession', models.CharField(max_length=255)),
                ('university_name', models.CharField(max_length=255)),
                ('university_rating', models.IntegerField()),
            ],
        ),
    ]