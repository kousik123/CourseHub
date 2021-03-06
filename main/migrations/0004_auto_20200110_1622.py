# Generated by Django 2.2.5 on 2020-01-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecturevideo',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
