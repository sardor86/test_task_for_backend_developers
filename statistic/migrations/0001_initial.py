# Generated by Django 4.2.7 on 2023-11-22 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120, verbose_name='Полное имя клиента')),
                ('birthdate', models.DateField(verbose_name='День рождение клиента')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120, verbose_name='Полное имя клиента')),
                ('birthdate', models.DateField(verbose_name='День рождение сотрудника')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название продукта')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Время заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='statistic.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statistic.employee')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='statistic.product')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]