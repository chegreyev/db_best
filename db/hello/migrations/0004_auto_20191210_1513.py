# Generated by Django 3.0 on 2019-12-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_tuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='tuser',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
