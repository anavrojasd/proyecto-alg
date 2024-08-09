import requests as rq
from Pelicula import Pelicula
from Planeta import Planeta
from Personaje import Personaje
from Especie import Especie
from Nave import Nave

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

def cargar_especie():
    lista_especies=[]
    especiesAPI= cargar_API("https://www.swapi.tech/api/species?page=1&limit=40")

    for results in especiesAPI["results"]:
        url_especie=cargar_API(results["url"])
        nombre_especie=url_especie["result"]['properties']["name"]
        altura_especie=url_especie["result"]['properties']["average_height"]
        clasificacion_especie=url_especie["result"]['properties']["classification"]
        nombre_planeta_origen_especie=url_especie["result"]['properties']["homeworld"]
        lengua_materna_especie=url_especie["result"]['properties']["language"]

        especies=Especie(nombre_especie,altura_especie,clasificacion_especie,nombre_planeta_origen_especie,lengua_materna_especie)
        lista_especies.append(especies)
    return lista_especies

def cargar_nave():
    lista_naves=[]
    navesAPI=cargar_API("https://www.swapi.tech/api/starships?page=1&limit=40")
    for results in navesAPI["results"]:
        url_nave=cargar_API(results["url"])
        nombre_nave=url_nave["result"]['properties']["name"]
        piloto=url_nave["result"]['properties']["pilots"]

        nave=Nave(nombre_nave,piloto)
        lista_naves.append(nave)
    return lista_naves



    

