# Generated by Django 3.0.3 on 2020-04-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_arm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('cash', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Arm',
        ),
    ]
