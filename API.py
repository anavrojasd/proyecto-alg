import requests as rq

def cargar_API(link):
    info=rq.get(link)
    return info.json()

cargar_API("https://www.swapi.tech/api/")

