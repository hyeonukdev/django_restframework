# Generated by Django 3.2.4 on 2021-06-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_regNo', models.TextField(unique=True)),
                ('student_name', models.TextField()),
                ('student_email', models.TextField()),
                ('student_mobile', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
