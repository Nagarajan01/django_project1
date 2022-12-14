# Generated by Django 4.1.1 on 2022-10-10 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('mark', models.IntegerField()),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Modified_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=20, null=True)),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('roll_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student_detail')),
            ],
        ),
    ]
