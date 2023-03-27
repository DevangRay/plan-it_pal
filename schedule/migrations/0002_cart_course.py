# Generated by Django 4.1.7 on 2023-03-27 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_nbr', models.IntegerField()),
                ('subject', models.CharField(max_length=10)),
                ('catalog_nbr', models.CharField(max_length=10)),
                ('instructor_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.cart')),
            ],
        ),
    ]
