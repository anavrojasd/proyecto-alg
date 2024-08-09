import requests as rq
from Pelicula import Pelicula
from Planeta import Planeta
from Personaje import Personaje
def cargar_API(link):
    info=rq.get(link).json()
    return info

def cargar_peliculas():
    lista_peliculas = []
    peliculasAPI = cargar_API("https://www.swapi.tech/api/films")
    
    for results in peliculasAPI['result']:
        titulo = results['properties']['title']
        personajes = results['properties']['characters']
        numero_del_episodio= results['properties']['episode_id']
        fecha_de_lanzamiento= results['properties']['release_date']
        opening_crawl= results['properties']['opening_crawl']
        director= results['properties']['director']
        productores= results['properties']['producer']
        planetas= results['properties']['planets']
        aeronaves= results['properties']['starships']
        vehiculos= results['properties']['vehicles']
        especies= results['properties']['species']
        pelicula = Pelicula(titulo, personajes,numero_del_episodio,fecha_de_lanzamiento, opening_crawl, director, productores, planetas, aeronaves, vehiculos, especies)
        pelicula.mostrar_peliculas()
        lista_peliculas.append(pelicula)
    return lista_peliculas


def cargar_planetas():
    lista_planetas= []
    planetasAPI= cargar_API("https://www.swapi.tech/api/planets?page=1&limit=75")

    for results in planetasAPI["results"]:
        url_planeta=cargar_API(results["url"])
        nombre_planeta = url_planeta['result']['properties']['name']
        periodo_orbita=url_planeta['result']['properties']['orbital_period']
        periodo_rotacion=url_planeta['result']['properties']['rotation_period']
        cantidad_habitantes=url_planeta['result']['properties']['population']
        tipo_clima=url_planeta['result']['properties']['name']

        planeta= Planeta(nombre_planeta, periodo_orbita, periodo_rotacion, cantidad_habitantes, tipo_clima)
        lista_planetas.append(planeta)
    return lista_planetas


def cargar_personaje():
    lista_personajes=[]
    personajesAPI= cargar_API("https://www.swapi.tech/api/people?page=1&limit=95")

    for results in personajesAPI["results"]:
        url_personaje=cargar_API(results["url"])
        nombre_personaje=url_personaje["result"]['properties']["name"]
        planeta_origen=url_personaje["result"]['properties']["homeworld"]
        genero=url_personaje["result"]['properties']["gender"]

        personaje=Personaje(nombre_personaje, planeta_origen,genero)
        lista_personajes.append(personaje)
    return lista_personajes

        