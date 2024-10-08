import requests as rq
from API import cargar_peliculas, cargar_planetas, cargar_especie, cargar_personaje, cargar_nave, cargar_vehiculo
from Pelicula import Pelicula
from Planeta import Planeta
from Especie import Especie
from Personaje import buscar_personaje, Personaje
from Nave import Nave
from Vehiculo import Vehiculo
from Mision import Mision
from misionesApp import (
    crear_mision, 
    modificar_mision, 
    acceder_mision, 
    gestionar_mision, 
    visualizar_mision, 
    parsear_archivo, 
    salvar_archivo,
    seleccionar_y_ver_mision
)
from Estadistica import csv_characters, nombre_planeta, csv_starships, longitud_de_nave, capacidad_de_nave, hiperimpulso_de_nave, mglt_de_nave, estadisticas_aeronaves

class App:
    def start(self):
        planetas =cargar_planetas()
        especies= cargar_especie()
        lista_personajes =cargar_personaje()
        lista_naves = cargar_nave()
        lista_vehiculos = cargar_vehiculo()
        lista_peliculas = cargar_peliculas()

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
                11- Cargar misiones                 
                12- Salir                                                                                                                              
            --> ''')

            if menu == '1':
                for pelicula in lista_peliculas:
                    pelicula.mostrar_peliculas()
                None

            elif menu == '2':
                for especie in especies:
                    especie.mostrar_especies(lista_peliculas, lista_personajes)

            elif menu == '3':
                for planeta in planetas:
                    planeta.mostrar_planetas(lista_peliculas, lista_personajes)

            elif menu == '4':
                
                resultados = buscar_personaje(lista_personajes)
                especie_del_personaje = ""
                if len(resultados) > 0:
                    for personaje in resultados:
                        listaNaves=[]
                        listaVehiculos=[]
                        listaPeliculas=[]
                        eleccion=int(input('Seleccione un personaje: '))
                        print()
                        if 1 <= eleccion <= len(resultados):
                            personaje=resultados[eleccion-1]
                            
                            for especie in especies:                                
                                for p in especie.personajes:
                                    if p == personaje.url:
                                        especie_del_personaje = especie.nombre_especie
                            
                            for pelicula in lista_peliculas:
                                for urlPersonaje in pelicula.personajes:
                                    if personaje.url == urlPersonaje:
                                        listaPeliculas.append(pelicula.titulo)

                            for nave in lista_naves:
                                for urlPersonaje in nave.piloto:                                    
                                    if personaje.url == urlPersonaje:
                                        listaNaves.append(nave.nombre_nave)

                            for vehiculo in lista_vehiculos:
                                for urlPersonaje in vehiculo.piloto:
                                    if personaje.url == urlPersonaje:
                                        listaVehiculos.append(vehiculo.nombre_vehiculo)

                            personaje.show(especie_del_personaje, listaPeliculas, listaNaves, listaVehiculos)
                        else:
                            print('Seleccion invalida. Elija un numero en la lista')                            
                else:
                    print('No se encontraron personajes.')                                            
                
            elif menu == '5':
                personajes = csv_characters()
                nombre_planeta(personajes)

            elif menu == '6':
                while True:
                    submenu=input('''
Ingrese una de las opciones:
        1- Longitud de la nave.
        2- Capacidad de carga.
        3- Clasificación de hiperimpulsor.
        4- MGLT (Modern Galactic Light Time)
        5- Salir.
 ''')
                    if submenu=='1':
                        graficos_longitudes= csv_starships()
                        longitud_de_nave(graficos_longitudes)

                    elif submenu=='2':
                        graficos_capacidad= csv_starships()
                        capacidad_de_nave(graficos_capacidad)
                    
                    elif submenu== '3':
                        graficos_hiperimpulso= csv_starships()
                        hiperimpulso_de_nave(graficos_hiperimpulso)
                    
                    elif submenu== '4':
                        graficos_mglt= csv_starships()
                        mglt_de_nave(graficos_mglt)
                    
                    elif submenu=='5':
                        break
                    
            elif menu == '7':
                estadisticas_aeronaves()   

            elif menu == '8':
                crear_mision() 

            elif menu == '9':
                cedula=int(input('Por favor dame la cedula para buscar tus misiones: '))               
                no_mision, misiones = parsear_archivo(cedula)
                modificar_mision(misiones)
                salvar_archivo(cedula, no_mision, misiones)

            elif menu == '10':
                cedula=int(input('Por favor dame la cedula para buscar tus misiones: '))
                no_mision, misiones = parsear_archivo(cedula)
                seleccionar_y_ver_mision(misiones)

            elif menu == '11':
                cedula=int(input('Por favor dame la cedula para buscar tus misiones: '))
                print('\n\n')
                visualizar_mision(cedula)             

            elif menu == '12':
                break

            else:
                print('Ingrese una opcion valida.')
