from django.contrib import admin
from pokemon_entities.models import Pokemon, PokemonEntity, Element
admin.site.register(Pokemon)
admin.site.register(PokemonEntity)
admin.site.register(Element)
