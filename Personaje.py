class Personaje:
    def __init__(self, nombre, planeta, genero):
        self.nombre = nombre
        self.planeta = planeta
        self.genero = genero

    def __str__(self):
        return self.nombre  
    
def buscar_personaje(lista_personajes, cadena_busqueda):
    resultados = []
    for personaje in lista_personajes:
        if cadena_busqueda.lower() in personaje.nombre.lower():  
            resultados.append(personaje)
    return resultados
