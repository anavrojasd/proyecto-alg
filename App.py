from API import cargar_peliculas, cargar_planetas, cargar_especie, cargar_personaje
from Pelicula import Pelicula
from Planeta import Planeta
from Personaje import buscar_personaje, mostrar_personaje

class App:
    def start(self):
        peliculas = cargar_peliculas()
        planetas = cargar_planetas()
        especies= cargar_especie()
        personajes = cargar_personaje()

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

            elif menu == '2':
                for especie in especies:
                    especie.mostrar_especies(peliculas, personajes)
                
            elif menu == '3':
                for planeta in planetas:
                    planeta.mostrar_planetas()

            elif menu == '4': 
                cadena_busqueda = input("Ingrese parte del nombre del personaje a buscar: ")
                resultados = buscar_personaje(personajes, cadena_busqueda)
                if resultados:
                    print("Personajes encontrados:")
                    for personaje in resultados:
                        mostrar_personaje(personaje) 
                else:
                    print("No se encontraron personajes con ese nombre.")
            elif menu == '13':
                break

    
app = App()
app.start()
