# Generated by Django 3.1.4 on 2021-05-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_formback_topback'),
    ]

    operations = [
        migrations.AddField(
            model_name='topback',
            name='place',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Место работы'),
        ),
        migrations.AlterField(
            model_name='topback',
            name='adres',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Юридический адрес'),
        ),
        migrations.AlterField(
            model_name='topback',
            name='description',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='topback',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='topback',
            name='iin',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='ИИН'),
        ),
        migrations.AlterField(
            model_name='topback',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Номер телефона'),
        ),
    ]
