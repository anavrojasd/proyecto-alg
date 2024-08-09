class Planeta:
    def __init__(self, nombre_planeta, periodo_orbita, periodo_rotacion, cantidad_habitantes, tipo_clima, personajes,url):
        self.nombre_planeta = nombre_planeta
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_habitantes = cantidad_habitantes
        self.tipo_clima = tipo_clima
        self.personajes = personajes
        self.url = url

    def mostrar_planetas(self, lista_peliculas, lista_personajes):
        
        listaNombres = []
        listaPeliculas = []
            
        for urlPlaneta in self.personajes:    
            for personaje in lista_personajes:  
                if urlPlaneta == personaje.url:
                    listaNombres.append(personaje.nombre_personaje)
        for pelicula in lista_peliculas:
            for urlPlaneta in pelicula.planetas:
                if urlPlaneta == self.url:
                    listaPeliculas.append(pelicula.titulo)    

        print(f'''
        Datos del planeta:
        Nombre: {self.nombre_planeta}
        Período de órbita: {self.periodo_orbita}
        Período de rotación: {self.periodo_rotacion}
        Cantidad de habitantes: {self.cantidad_habitantes}
        Tipo de clima: {self.tipo_clima}
        Lista de episodios en los que aparece el planeta:''')
        print(*listaPeliculas, sep = ", ")
        print('''\tLista de personajes originarios del planeta:''')
        print(*listaNombres, sep = ", ")


