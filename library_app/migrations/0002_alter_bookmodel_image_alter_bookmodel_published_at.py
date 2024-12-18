# Generated by Django 5.1.3 on 2024-12-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='image',
            field=models.ImageField(upload_to='books/', verbose_name='Загрузите фото книги'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='published_at',
            field=models.DateField(verbose_name='Укажите дату выпуска: '),
        ),
    ]
