class Planeta:
    def __init__(self, nombre, orbita, rotacion, habitantes, clima, peliculas, personajes) -> None:
        self.nombre=nombre
        self.orbita=orbita
        self.rotacion=rotacion
        self.habitantes=habitantes
        self.clima=clima
        self.peliculas=peliculas
        self.personajes=personajes

    def mostrar_personajes(self):
        contador=1
        for personaje in self.personajes:
            print(f'{contador}-{personaje.nombre}')
            contador+=1

    def mostrar_episodios(self):
        contador=1
        for pelicula in self.peliculass:
            print(f'{contador}-{pelicula.titulo}')    
        