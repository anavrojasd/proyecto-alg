class Especie:
    def __init__(self, nombre, altura, clasificacion, planeta, lengua, personajes, peliculas) -> None:
        self.nombre=nombre
        self.altura=altura
        self.clasificacion=clasificacion
        self.planeta=planeta
        self.lengua=lengua
        self.personajes=personajes
        self.peliculas=peliculas


    def mostrar_personajes(self):
        contador=1
        for personaje in self.personajes:
            print(f'{contador}-{personaje.nombre}')
            contador+=1

    def mostrar_episodios(self):
        contador=1
        for pelicula in self.peliculass:
            print(f'{contador}-{pelicula.titulo}')        

        