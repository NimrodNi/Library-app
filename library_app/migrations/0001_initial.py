# Generated by Django 5.1.3 on 2024-12-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='films/', verbose_name='Загрузите фото книги')),
                ('title', models.CharField(max_length=100, verbose_name='укажите название книги')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание')),
                ('price', models.FloatField(default=10, verbose_name='укажите цену на книгу')),
                ('published_at', models.IntegerField(verbose_name='Укажите дату выпуска: ')),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Комедия', 'Комедия'), ('Романы', 'Романы')], default='Роман', max_length=100)),
                ('page_amount', models.IntegerField(blank=True, verbose_name='Укажите количество страниц')),
                ('author', models.CharField(default='Райан Гослинг', max_length=100, verbose_name='Укажите автора')),
                ('audio_version', models.URLField(null=True, verbose_name='Укажите ссылку на аудио версию книги')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]
