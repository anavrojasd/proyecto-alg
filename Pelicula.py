class Pelicula:
    def __init__(self, titulo, numero_del_episodio, fecha_de_lanzamiento, opening_crawl, director, productores, planetas, aeronaves, vehiculos, especies, personajes):
        self.titulo = titulo
        self.numero_del_episodio = numero_del_episodio
        self.fecha_de_lanzamiento = fecha_de_lanzamiento
        self.opening_crawl = opening_crawl
        self.director = director
        self.productores = productores
        self.planetas = planetas
        self.aeronaves = aeronaves
        self.vehiculos = vehiculos
        self.especies = especies
        self.personajes = personajes

    def mostrar_peliculas(self, mostrar_personajes=False):
        print(f'''
                Datos de la película:
                Título: {self.titulo}
                Número de Episodio: {self.numero_del_episodio}
                Fecha de Lanzamiento: {self.fecha_de_lanzamiento}
                Opening crawl: {self.opening_crawl}
                Nombre del Director: {self.director}
                        ''')
        if mostrar_personajes:
            print("Personajes:")
            for personaje in self.personajes:
                print(f"- {personaje[1]}")
