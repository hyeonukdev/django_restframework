# Generated by Django 3.2.4 on 2021-06-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emplyee_regNo', models.TextField(unique=True)),
                ('emplyee_name', models.TextField()),
                ('employee_email', models.TextField()),
                ('employee_mobile', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
