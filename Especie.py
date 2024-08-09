class Especie:
    def __init__(self, nombre_especie, altura_especie, clasificacion_especie, nombre_planeta_origen_especie, lengua_materna_especie):
        self.nombre_especie=nombre_especie
        self.altura_especie=altura_especie
        self.clasificacion_especie=clasificacion_especie
        self.nombre_planeta_origen_especie=nombre_planeta_origen_especie
        self.lengua_materna_especie=lengua_materna_especie
                
        # def mostrar_personajes(self):
    #     contador=1
    #     for personaje in self.personajes:
    #         print(f'{contador}-{personaje.nombre}')
    #         contador+=1

    # def mostrar_episodios(self):
    #     contador=1
    #     for pelicula in self.peliculass:
    #         print(f'{contador}-{pelicula.titulo}')        

        

    def mostrar_especies(self):
        print(f'''
        Datos de la especie:
        Nombre: {self.nombre_especie}
        Altura: {self.altura_especie}
        Clasificacion: {self.clasificacion_especie}
        Planeta de origen: {self.nombre_planeta_origen_especie}
        Lengua materna: {self.lengua_materna_especie}
        Nombre de los personajes que pertenecen a la especie:
        Nombre de los episodios en los que aparecen:         
                        ''')







            
