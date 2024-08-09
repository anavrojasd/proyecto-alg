class Personaje:
    def __init__(self, nombre_personaje, planeta_origen, genero, url):
        self.nombre_personaje = nombre_personaje
        self.planeta_origen = planeta_origen
        self.genero = genero
        self.url = url

    def __str__(self):
        return self.nombre_personaje  
    
def buscar_personaje(lista_personajes, cadena_busqueda):
        resultados = []
        for personaje in lista_personajes:
            if cadena_busqueda.lower() in personaje.nombre_personaje.lower():  
                resultados.append(personaje)
                return resultados

   
def mostrar_personaje(self):
        print(f'''
        Datos de los personajes:
        Nombre: {self.nombre_personaje}
        Planeta de origen: {self.planeta_origen}
        Genero: {self.genero}
        Especie: 
        Naves que utiliza: 
        Vehiculos que utiliza:
                        ''')

