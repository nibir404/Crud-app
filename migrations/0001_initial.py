# Generated by Django 3.1.4 on 2020-12-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('f_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
            ],
        ),
    ]
