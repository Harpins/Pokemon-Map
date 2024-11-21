import folium
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from pokemon_entities.models import Pokemon, PokemonEntity
import django.utils.timezone as get_time

USE_TZ = True

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    time_now = get_time.now()
    
    current_entities = PokemonEntity.objects.filter(
        appeared_at__lte=time_now, disappeared_at__gt=time_now)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    
    for pokemon_entity in current_entities:
        if pokemon_entity.pokemon.img_url:
            add_pokemon(
                folium_map, pokemon_entity.latitude,
                pokemon_entity.longitude,
                pokemon_entity.pokemon.img_url.url[1::],
            )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.img_url.url:
            pokemons_on_page.append({
                'id': pokemon.id,
                'img_url': pokemon.img_url.url[1::],
                'title_ru': pokemon.title_ru,
            })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    time_now = get_time.now()

    requested_pokemon = get_object_or_404(Pokemon.objects.all(), id=pokemon_id)
    requested_evolutions = requested_pokemon.next_evolutions.all()
    requested_types = requested_pokemon.element_types.all()

    requested_pokemon_entities = PokemonEntity.objects.filter(
        pokemon=requested_pokemon, appeared_at__lte=time_now, disappeared_at__gt=time_now)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon_entities:
        if pokemon_entity.pokemon.img_url:
            add_pokemon(
                folium_map, pokemon_entity.latitude,
                pokemon_entity.longitude,
                pokemon_entity.pokemon.img_url.url[1::],
            )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 
        'pokemon': requested_pokemon, 
        'requested_evolutions': requested_evolutions, 
        'requested_types': requested_types,
    })
