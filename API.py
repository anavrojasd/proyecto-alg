import requests as rq
from Pelicula import Pelicula


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
        url= results['properties']['url']
        planetas= results['properties']['planets']
        aeronaves= results['properties']['starships']
        vehiculos= results['properties']['vehicles']
        especies= results['properties']['species']

        pelicula = Pelicula(titulo, personajes,numero_del_episodio,fecha_de_lanzamiento, opening_crawl, director, productores, url, planetas, aeronaves, vehiculos, especies)
        lista_peliculas.append(pelicula)
    return lista_peliculas
cargar_peliculas()
