# Generated by Django 3.1.4 on 2021-05-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210511_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='formback',
            name='bank',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Банковские реквизиты'),
        ),
        migrations.AddField(
            model_name='formback',
            name='fio',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='ФИО Первого руководителя'),
        ),
        migrations.AddField(
            model_name='formback',
            name='first',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Должность первого руководителя'),
        ),
        migrations.AlterField(
            model_name='formback',
            name='adres',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Юридический адрес'),
        ),
        migrations.AlterField(
            model_name='formback',
            name='child',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='formback',
            name='description',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Направление деятельности'),
        ),
        migrations.AlterField(
            model_name='formback',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='formback',
            name='iin',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='БИН/ИИН'),
        ),
        migrations.AlterField(
            model_name='formback',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Полное наименование организации'),
        ),
        migrations.AlterField(
            model_name='formback',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Номер телефона'),
        ),
    ]
