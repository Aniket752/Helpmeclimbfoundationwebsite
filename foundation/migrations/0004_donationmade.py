# Generated by Django 3.0.5 on 2020-09-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0003_auto_20200922_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='donationMade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pan_no', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.CharField(max_length=10)),
                ('amount', models.CharField(max_length=200)),
                ('t_id', models.CharField(max_length=100)),
            ],
        ),
    ]