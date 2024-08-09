class Personaje:
    def __init__(self, nombre_personaje, planeta_origen, genero, especie_personaje, url):
        self.nombre_personaje = nombre_personaje
        self.planeta_origen = planeta_origen
        self.genero = genero
        self.especie_personaje = especie_personaje
        self.url = url

    def __str__(self):
        return self.nombre_personaje 

    def buscar_personaje(lista_personajes, cadena_busqueda):
        resultados=[]
        contador=1
        for personaje in lista_personajes:
            if cadena_busqueda.lower() in personaje.nombre_personaje.lower():  
                print(f'{contador}-{personaje.nombre_personaje}')
                contador+=1


    def mostrar_personaje(self, lista_naves, lista_vehiculos):
        listaNaves=[]
        listaVehiculos=[]

        for urlNaves in self.nave:    
            for nave in lista_naves:
                if urlNaves == nave.url:
                    listaNaves.append(nave.nombre_nave)
        for vehiculo in lista_vehiculos:
            for urlPersonaje in vehiculo.personajes:
                if urlPersonaje == self.url:
                    listaVehiculos.append(vehiculo.nombre_vehiculo)            

        print(f'''
        Datos de los personajes:
        Nombre: {self.nombre_personaje}
        Planeta de origen: {self.planeta_origen}
        Genero: {self.genero}
        Especie: {self.especie_personaje}''') 
        print('\tNaves que utiliza: ')
        print(*listaNaves, sep = ",")  
        print('\tVehiculos que utiliza: ')
        print(*listaVehiculos, sep = ",")








