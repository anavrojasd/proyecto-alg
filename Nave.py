class Nave:
    def __init__(self,nave, piloto):
        self.piloto=piloto
        self.nave=nave
        

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
        Nombre: {self.nombre}
        Altura: {self.altura}
        Clasificacion: {self.clasificacion}
        Planeta de origen: {self.planeta}
        Lengua materna: {self.opening_crawl}                
                        ''')