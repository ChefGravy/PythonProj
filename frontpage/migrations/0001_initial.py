# Generated by Django 3.0.3 on 2020-08-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField()),
            ],
        ),
    ]
