# Generated by Django 4.1.1 on 2022-10-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('roll_number', models.CharField(max_length=200, null=True)),
                ('upload', models.ImageField(upload_to='image')),
            ],
        ),
    ]
