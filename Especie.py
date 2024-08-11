class Especie:
    def __init__(self, nombre_especie, altura_especie, clasificacion_especie, nombre_planeta_origen_especie, lengua_materna_especie, personajes, url):
        self.nombre_especie=nombre_especie
        self.altura_especie=altura_especie
        self.clasificacion_especie=clasificacion_especie
        self.nombre_planeta_origen_especie=nombre_planeta_origen_especie
        self.lengua_materna_especie=lengua_materna_especie
        self.personajes = personajes
        self.url = url

    def mostrar_especies(self, lista_peliculas, lista_personajes):

        listaNombres = []
        listaPeliculas = []
        
        for urlPersonaje in self.personajes:    
            for personaje in lista_personajes:
                if urlPersonaje == personaje.url:
                    listaNombres.append(personaje.nombre_personaje)
        for pelicula in lista_peliculas:
            for urlEspecie in pelicula.especies:
                if urlEspecie == self.url:
                    listaPeliculas.append(pelicula.titulo)
        
        print(f'''
        Datos de la especie:
        Nombre: {self.nombre_especie}
        Altura: {self.altura_especie}
        Clasificacion: {self.clasificacion_especie}
        Planeta de origen: {self.nombre_planeta_origen_especie}
        Lengua materna: {self.lengua_materna_especie}
        Nombre de los personajes que pertenecen a la especie:''')
        print(*listaNombres, sep = ",")
        print('''\tNombre de los episodios en los que aparecen:''')
        print(*listaPeliculas, sep = ",")
    
        
                
