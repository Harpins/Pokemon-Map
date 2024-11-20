from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    title_ru = models.CharField(
        max_length=50, default='MissingNo', verbose_name='Название покемона (рус.)')
    title_en = models.CharField(
        max_length=50, blank=True, verbose_name='Название покемона (анг.)')
    title_jp = models.CharField(
        max_length=50, blank=True, verbose_name='Название покемона (яп.)')
    description = models.TextField(
        blank=True, verbose_name='Описание покемона')
    img_url = models.ImageField(blank=True,
                                null=True,
                                upload_to='media/',
                                verbose_name='Ссылка на изображение покемона',
                                )
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='pokemon_pre_evo', verbose_name='Предыдущая стадия развития покемона')
    next_evolutions = models.ManyToManyField('self', symmetrical=False, blank=True,
                                             related_name='pokemon_next_evo', verbose_name='Следующие стадии развития покемона')
    element_types = models.ManyToManyField(
        'Element', symmetrical=False, blank=True, related_name='elements', verbose_name='Тип покемона')

    def __str__(self):
        return f'{self.title_ru}:{self.id}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, blank=False, related_name='pokemon_type', verbose_name='Вид покемона')
    latitude = models.FloatField(
        blank=True, null=True, verbose_name='Координаты: широта')
    longitude = models.FloatField(
        blank=True, null=True, verbose_name='Координаты: долгота')
    appeared_at = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата появления')
    disappeared_at = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата исчезновения')
    level = models.IntegerField(
        blank=True, null=True, verbose_name='Уровень покемона')
    health = models.IntegerField(
        blank=True, null=True, verbose_name='Здоровье покемона')
    attack = models.IntegerField(
        blank=True, null=True, verbose_name='Атака покемона')
    defence = models.IntegerField(
        blank=True, null=True, verbose_name='Защита покемона')
    special = models.IntegerField(
        blank=True, null=True, verbose_name='Спецхарактеристика покемона')
    speed = models.IntegerField(
        blank=True, null=True, verbose_name='Скорость покемона')

    def __str__(self):
        return f'{self.pokemon.title_ru}:{self.pokemon.id}'


class Element(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название типа')
    img = models.ImageField(blank=True,
                            null=True,
                            upload_to='media/',
                            verbose_name='Иконка типа покемона')
    strong_against = models.TextField(blank=True, verbose_name='Описание типа')

    def __str__(self):
        return self.title
