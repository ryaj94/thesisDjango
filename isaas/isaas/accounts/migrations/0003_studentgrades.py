# Generated by Django 4.1.5 on 2023-01-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_users_studentprof'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentgrades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gned02', models.CharField(max_length=200, null=True)),
                ('gned05', models.CharField(max_length=200, null=True)),
                ('gned11', models.CharField(max_length=200, null=True)),
                ('cosc50', models.CharField(max_length=200, null=True)),
                ('dcit21', models.CharField(max_length=200, null=True)),
                ('dcit22', models.CharField(max_length=200, null=True)),
                ('fitt1', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
