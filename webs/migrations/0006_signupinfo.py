# Generated by Django 5.0.1 on 2024-02-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0005_contactinfo_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='signupinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('umail', models.CharField(max_length=30)),
                ('pswd', models.IntegerField()),
                ('phn', models.IntegerField()),
                ('adrs', models.TextField()),
            ],
        ),
    ]
