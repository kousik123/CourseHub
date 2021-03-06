# Generated by Django 2.2.5 on 2020-01-01 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200101_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('lecturename', models.TextField(max_length=200)),
                ('lecturedate', models.DateField(default=datetime.date.today)),
                ('lecturevideo', models.FileField(upload_to='')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Course')),
            ],
            options={
                'db_table': 'Lecture',
            },
        ),
    ]
