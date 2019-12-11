# Generated by Django 3.0 on 2019-12-11 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
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
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('university_code', models.IntegerField(blank=True, null=True)),
                ('university_category', models.CharField(default='State', max_length=255, null=True)),
                ('university_type', models.CharField(default='University', max_length=255, null=True)),
                ('university_email', models.CharField(max_length=100, null=True)),
                ('university_site', models.CharField(max_length=100, null=True)),
                ('military_dep', models.CharField(default='No', max_length=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='rus.City')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_title', models.CharField(max_length=255)),
                ('first_lesson', models.CharField(max_length=100)),
                ('second_lesson', models.CharField(max_length=100)),
                ('total_grant', models.IntegerField(null=True)),
                ('full_kz', models.IntegerField(null=True)),
                ('full_ru', models.IntegerField(null=True)),
                ('full_en', models.IntegerField(null=True)),
                ('shortened_kz', models.IntegerField(null=True)),
                ('shortened_ru', models.IntegerField(null=True)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professions', to='rus.University')),
            ],
        ),
    ]
