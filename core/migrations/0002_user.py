# Generated by Django 4.2 on 2023-04-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='banners/', verbose_name='Image')),
                ('username', models.CharField(max_length=300, null=True, verbose_name='Username')),
                ('followers', models.IntegerField(blank=True, default=0, null=True)),
                ('following', models.IntegerField(blank=True, default=0, null=True)),
                ('password', models.IntegerField(blank=True, default=0, null=True)),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
                ('bio', models.CharField(max_length=300, null=True, verbose_name='Bio')),
                ('name', models.CharField(max_length=300, null=True, verbose_name='Name')),
            ],
        ),
    ]
