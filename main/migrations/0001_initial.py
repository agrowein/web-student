# Generated by Django 3.2.7 on 2021-10-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('patronymic', models.CharField(max_length=40)),
                ('is_teacher', models.BooleanField(default=False)),
                ('student_code', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Детальная информация',
                'verbose_name_plural': 'Детальная информация',
            },
        ),
    ]