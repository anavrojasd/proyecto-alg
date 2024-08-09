from API import cargar_peliculas, cargar_planetas
from Pelicula import Pelicula

class App:
    def start(self):
        peliculas = cargar_peliculas()
        print('Bienvenido')

        while True:
            menu = input('''
Ingrese una opción del menú:
    1- Lista de películas de la saga
    2- Lista de las especies de seres vivos de la saga   
    3- Lista de planetas 
    4- Buscar un personaje                                                   
    5- Gráfico de cantidad de personajes nacidos en cada planeta
    6- Gráficos de características de naves
    7- Estadísticas sobre naves
    8- Construir misión
    9- Modificar misión
    10- Visualizar misión
    11- Guardar misiones
    12- Cargar misiones                  
    13- Salir                                                                                                                              
--> ''')

            if menu == '1':
                for pelicula in peliculas:
                    pelicula.mostrar_peliculas()

                    

# Crear una instancia de la aplicación y comenzar
app = App()
app.start()
