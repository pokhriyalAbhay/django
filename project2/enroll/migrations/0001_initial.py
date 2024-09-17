# Generated by Django 5.0.2 on 2024-03-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=50)),
                ('stuemail', models.EmailField(max_length=254)),
                ('stupass', models.CharField(max_length=50)),
                ('comment', models.CharField(default='not aviable', max_length=50)),
            ],
        ),
    ]
