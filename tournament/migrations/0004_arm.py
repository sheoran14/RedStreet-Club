# Generated by Django 3.0.3 on 2020-04-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20200305_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
    ]