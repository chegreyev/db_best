# Generated by Django 3.0 on 2019-12-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_delete_tuser'),
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
    ]
