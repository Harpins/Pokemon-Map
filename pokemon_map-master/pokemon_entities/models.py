import uuid
from django.db import models


class Pokemon(models.Model):
    pokemon_id = models.AutoField(primary_key=True, verbose_name='ID Покемона')
    title_ru = models.CharField(
        max_length=20, blank=False, verbose_name='Название покемона (рус.)')
    title_en = models.CharField(
        max_length=20, blank=True, verbose_name='Название покемона (анг.)')
    title_jp = models.CharField(
        max_length=20, blank=True, verbose_name='Название покемона (яп.)')
    description = models.TextField(
        blank=True, verbose_name='Описание покемона')
    img_url = models.ImageField(blank=True,
                                null=True,
                                height_field='image_height',
                                width_field='image_width',
                                upload_to='sprites/pokemon/',
                                default='sprites/pokemon/missingno.png',
                                verbose_name='Ссылка на изображение покемона',
                                )
    image_height = models.IntegerField(
        blank=True, null=True, verbose_name='Высота изображения')
    image_width = models.IntegerField(
        blank=True, null=True, verbose_name='Ширина изображения')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='post_evolution', verbose_name='Предыдущая стадия развития покемона')
    next_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='pre_evolution', verbose_name='Следующая стадия развития покемона')
    element_type = models.ForeignKey('Element', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип покемона')
    def __str__(self):
        return f'{self.title_ru}'


class PokemonEntity(models.Model):
    entity_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False, verbose_name='Уникальный идентификатор покемона')
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, blank=False, verbose_name='Вид покемона')
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
    defense = models.IntegerField(
        blank=True, null=True, verbose_name='Защита покемона')
    special = models.IntegerField(
        blank=True, null=True, verbose_name='Спецхарактеристика покемона')
    speed = models.IntegerField(
        blank=True, null=True, verbose_name='Скорость покемона')

    def __str__(self):
        return f'{self.pokemon.title_ru}:{self.entity_id}'

class Element(models.Model):
    title = models.CharField(max_length=20, blank=False, verbose_name='Название типа')
    img = models.ImageField(blank=True,
                            null=True,
                            upload_to='sprites/pokemontypes/',
                            default='sprites/pokemontypes/curse.png',
                            verbose_name='Иконка типа покемона')
    strong_against = models.TextField(blank=True, verbose_name='Описание типа')

    def __str__(self):
        return self.title