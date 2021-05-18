# Generated by Django 3.1.2 on 2021-05-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('indexed_value', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
    ]
