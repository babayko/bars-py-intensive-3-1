# Generated by Django 3.2.12 on 2022-03-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_and_inheritance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
        migrations.DeleteModel(
            name='OrderedWorker',
        ),
        migrations.CreateModel(
            name='OrderedWorker',
            fields=[
            ],
            options={
                'ordering': ('last_name', 'startwork_date'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('meta_and_inheritance.worker',),
        ),
    ]
