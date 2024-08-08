class Pelicula:
    def __init__(self, titulo, episodio, fecha, opening, director) -> None:
        self.titulo=titulo
        self.episodio=episodio
        self.fecha=fecha
        self.opening=opening
        self.director=director

    def mostrar_peliculas(self):
        print(f'''
Datos de la pelicula:
Titulo: {self.titulo}
Numero de Episodio: {self.episodio}              
Fecha de Lanzamiento: {self.fecha}
Opening crawl: {self.opening}
Nombre del Director: {self.director} ''')


        