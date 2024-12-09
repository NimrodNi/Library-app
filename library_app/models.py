from django.db import models

class BookModel(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Романы', 'Романы')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото книги')
    title = models.CharField(max_length=100, verbose_name='укажите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='укажите цену на книгу', default=10)
    published_at = models.DateField("Укажите дату выпуска: ")
    genre = models.CharField(max_length=100, choices=GENRE, default='Роман')
    page_amount = models.IntegerField(verbose_name='Укажите количество страниц', blank=True)
    author = models.CharField(max_length=100, verbose_name='Укажите автора', default='Райан Гослинг')
    audio_version = models.URLField(verbose_name='Укажите ссылку на аудио версию книги', null=True)

#Если вы указываете новое поле то обязательно используйте атрибут null=True и занового проводите миграции
#Еще используете null True когда меняете поле
#После прописания всех полей проводим миграции 1ая команда python manage.py makemigrations 2ая python manage.py migrate
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title

