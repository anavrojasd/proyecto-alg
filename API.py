import requests as rq

def cargar_API(link):
    info=rq.get(link).json()
    return info

cargar_API("https://www.swapi.tech/api/")

