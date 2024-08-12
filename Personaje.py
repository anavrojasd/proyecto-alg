class Personaje:
    def __init__(self, nombre_personaje, planeta_origen, genero, url):
        self.nombre_personaje = nombre_personaje
        self.planeta_origen = planeta_origen
        self.genero = genero
        self.url = url

    def show(self, nombre_especie, listaPeliculas, listaNaves, listaVehiculos ):
        print(f'Datos de los personajes:')
        print(f'Nombre: {self.nombre_personaje}')
        print(f'Planeta de origen: {self.planeta_origen}')  
        print(f'Episodios en los que interviene: ')  
        print(*listaPeliculas, sep = ',')
        print(f'Genero: {self.genero}')
        print(f'Especie: {nombre_especie}') 
        print('Naves que utiliza: ')
        print(*listaNaves, sep = ",")  
        print('Vehiculos que utiliza: ')
        print(*listaVehiculos, sep = ",")

    
                               

    def __str__(self):
        return self.nombre_personaje 

def buscar_personaje(lista_personajes):
    resultados = []
    contador=1
    cadena_busqueda=input('Introduce el nombre del personaje a buscar: ')

    for personaje in lista_personajes:
        if cadena_busqueda.lower() in personaje.nombre_personaje.lower():
            print(f'{contador}-{personaje.nombre_personaje}')
            resultados.append(personaje)
            contador+=1  
    return resultados    

   
                   
    



