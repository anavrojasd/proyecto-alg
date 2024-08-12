import os
from Usuario import Usuario
from Mision import Mision
from Estadistica import csv_planets, csv_characters, csv_weapons, csv_starships, nombres_personajes, nombres_planetas, nombres_naves, nombres_armas
import re

class Algo:
    usuarios_obj=[]
    misiones_obj=[]        

def agregar_usuario(cedula, nombre, apellido):    
    nuevo_usuario=Usuario(cedula, nombre, apellido)
    with open(f'misiones/{nuevo_usuario.cedula}.txt', "w") as file:
        file.write(f'Cedula - {nuevo_usuario.cedula}' + '\n')
        file.write(f'Nombre - {nuevo_usuario.nombre}' + '\n')
        file.write(f'Apellido - {nuevo_usuario.apellido}' + '\n')
        file.write('\n')
        file.write('\n')

def buscar_usuario_lineal(cedula):
    if os.path.exists(f'./misiones/{cedula}.txt'):
        return True
    return False

# Para validar que el usuario solo pueda crear 5 misiones maximo
def validacion_maximo_misiones(cedula):
    with open(f'misiones/{cedula}.txt', "r", encoding='utf-8') as file:
        contenido = file.read()
    contenido = contenido.lower()
    palabra = 'Mision'
    palabra_a_contar = palabra.lower()
    contador = contenido.count(palabra_a_contar)

    if contador > 5:
        return True
    return False

def crear_mision():
    print('Ingrese sus datos: ')
    cedula=int(input("\tCedula: "))
    usuario_seleccionado = buscar_usuario_lineal(cedula)
    
    if not usuario_seleccionado:
        nombre=input("\tNombre: ")
        apellido=input("\tApellido: ")
        agregar_usuario(cedula, nombre, apellido)

    if validacion_maximo_misiones(cedula):
        print('Ya no puedes agregar mas misiones')
        return 
    
    print("Puede empezar a crear su mision")
    nombre_mision=input("Nombre de la mision: ")
    print(f'Nombre de la mision: {nombre_mision}')

    planeta = elegir_planeta()
    nave = elegir_nave()
    armas = elegir_armas()
    integrantes = elegir_integrantes()

    mision = Mision(nombre_mision, planeta, nave, armas, integrantes)

    # Guardar la mision que se crea
    with open(f'misiones/{cedula}.txt', "a") as file:
        file.write(f'Mision - {mision.nombre}' + '\n')
        file.write(f'En el planeta: - {mision.planeta_destino}' + '\n')
        file.write(f'Con la nave - {mision.nave}' + '\n')
        armas_elegidas = ','.join(map(str, armas))
        file.write(f'Con las armas - {armas_elegidas}' + '\n')
        integrantes_elegidos = ','.join(map(str, integrantes))
        file.write(f'Con los integrantes - {integrantes_elegidos}' + '\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
       
def elegir_planeta():
    planetas = csv_planets()
    nombres_planetas_lista = nombres_planetas(planetas)

    print("Seleccione un planeta: ")
    contador=1
    for planeta in nombres_planetas_lista:
        print(f'{contador}-{planeta}')
        contador+=1
    planeta_elegido=int(input("-->"))
    planeta=nombres_planetas_lista[planeta_elegido-1]
    print(f'Planeta destino: {planeta}')
    return planeta
    
def elegir_nave():
    naves = csv_starships()
    nombres_naves_lista = nombres_naves(naves) 
    print("Seleccione una nave: ")
    contador=1
    for nave in nombres_naves_lista:
        print(f'{contador}-{nave}')
        contador+=1
    nave_elegida=int(input("-->"))
    nave=nombres_naves_lista[nave_elegida-1]
    print(f'Nave: {nave}')
    return nave

def elegir_armas():
    armas_elegidas=[]
    armas = csv_weapons()
    nombres_armas_lista = nombres_armas(armas)
    index = 0
    print(f'Seleccione las armas: ')
    contador=1
    for arma in nombres_armas_lista:
        print(f'{contador}-{arma}')
        contador+=1
    numeros=input('Escriba los numeros de las armas que desee (separados con coma): ').split(",")
    if(len(numeros) > 7 ):
        print('No se puede seleccionar mas de 7 armas.')
        elegir_armas()
    for numero in numeros:
        armas_elegidas.append(nombres_armas_lista[int(numero)-1])
    
    print(f'Armas: {armas_elegidas}')
    return armas_elegidas

def elegir_integrantes():
    integrantes_elegidos=[]
    personajes = csv_characters()
    nombres_personajes_lista = nombres_personajes(personajes) 
    index=0
    print(f'Seleccione los integrantes: ')
    contador=1
    for integrante in nombres_personajes_lista:
        print(f'{contador}-{integrante}')
        contador+=1
    numeros=input('Escriba los numeros de los integrantes que desee (separados con coma): ').split(",")
    if(len(numeros) > 7):
        print('No se pueden seleccionar mas de 7 integrantes.')
        elegir_integrantes()
    for numero in numeros:
        integrantes_elegidos.append(nombres_personajes_lista[int(numero)-1])
    print(f'Integrantes: {integrantes_elegidos}')
    return integrantes_elegidos



# Para modificar misiones guardadas
def parsear_archivo(cedula):
    with open(f'./misiones/{cedula}.txt', 'r', encoding='utf-8') as file:
        contenido = file.read()

    
    partes = re.split(r'\n\s*\n', contenido, maxsplit=1)
    no_mision = partes[0]
    parte_mision = partes[1] if len(partes) > 1 else ""

    misiones = []
    bloques_misiones = re.split(r'\n\s*\n', parte_mision.strip())

    for bloque in bloques_misiones:
        lineas = bloque.splitlines()
        mision = {}
        for linea in lineas:
            if linea.startswith("Mision -"):
                mision["Mision"] = linea.split(" - ")[1]
            elif linea.startswith("En el planeta:"):
                mision["En el planeta"] = linea.split(" - ")[1]
            elif linea.startswith("Con la nave"):
                mision["Con la nave"] = linea.split(" - ")[1]
            elif linea.startswith("Con las armas"):
                mision["Con las armas"] = linea.split(" - ")[1].split(',')
            elif linea.startswith("Con los integrantes"):
                mision["Con los integrantes"] = linea.split(" - ")[1].split(',')
        misiones.append(mision)

    return no_mision, misiones

def salvar_archivo(cedula, no_mision, misiones):
    with open(f'./misiones/{cedula}.txt', 'w', encoding='utf-8') as file:
        # Escribir la no mision
        file.write(no_mision.strip() + "\n\n")
        
        # Escribir cada mision al archivo
        for mision in misiones:
            file.write(f"Mision - {mision['Mision']}\n")
            file.write(f"En el planeta: - {mision['En el planeta']}\n")
            file.write(f"Con la nave - {mision['Con la nave']}\n")
            file.write(f"Con las armas - {','.join(mision['Con las armas'])}\n")
            file.write(f"Con los integrantes - {','.join(mision['Con los integrantes'])}\n\n")

def modificar_mision(misiones):
    # Para ver las misiones disponibles
    print("\nMisiones disponibles: ")
    for i, mision in enumerate(misiones, start=1):
        print(f"{i}. {mision['Mision']}")

    # Para elegir que mision modificar
    eleccion = int(input("\nEscriba el numero de la mision que desea modificar: ")) - 1

    # Para elegir que modificar
    print("\n¿Que desea modificar?")
    print("1. El planeta destino")
    print("2. La nave")
    print("3. Las armas")
    print("4. Los integrantes")
    modificacion_elegida = int(input("-->"))


    # Para modificar lo elegido
    if modificacion_elegida == 1:
        nuevo_planeta = elegir_planeta()
        misiones[eleccion]['En el planeta'] = nuevo_planeta
    elif modificacion_elegida == 2:
        nueva_nave = elegir_nave()
        misiones[eleccion]['Con la nave'] = nueva_nave
    elif modificacion_elegida == 3:
        nuevas_armas = elegir_armas()
        misiones[eleccion]['Con las armas'] = [arma.strip() for arma in nuevas_armas]
    elif modificacion_elegida == 4:
        nuevos_integrantes = elegir_integrantes()
        misiones[eleccion]['Con los integrantes'] = [integrante.strip() for integrante in nuevos_integrantes]
    else:
        print('Ingrese una opcion valida.')    

    print("\nMision actualizada")

       

def gestionar_mision(self):
        while len(self.misiones_obj) < 5:
            continuar = input("¿Desea crear una nueva misión? (si/no): ").lower()
            if continuar != 'si':
                break
            crear_mision()

def acceder_mision(self):
        misiones_usuarios=[]
        cedula = int(input("Ingrese su cédula para acceder a sus misiones: "))
        if cedula in misiones_usuarios:
            misiones = misiones_usuarios[cedula]
            print("\nMisiones disponibles:")
            contador = 1
            for mision in misiones:
                print(f'\t{contador}-{mision["nombre_mision"]}')
                contador += 1
            mision_seleccionada = int(input("Ingrese el número de la misión para ver los detalles--> "))
            if mision_seleccionada > 0 and mision_seleccionada <= len(misiones):
                mision = misiones[mision_seleccionada - 1]
                print("\nDetalles de la Misión:")
                print(f"Nombre de la misión: {mision['nombre_mision']}")
                print(f"Planeta destino: {mision['planeta'].nombre}")
                print(f"Nave a utilizar: {mision['nave'].nombre}")
                print("Armas a utilizar:")
                for arma in mision['armas']:
                    print(f"- {arma.nombre}")
                print("Integrantes de la misión:")
                for integrante in mision['integrantes']:
                    print(f"- {integrante.nombre}")
            else:
                print("\nIngrese solo números válidos.")
                return acceder_mision()
        else:
            print("No se encontraron misiones para esta cédula.")
            return acceder_mision(self)

# Ver las misiones de cada usuario a partir de su cedula
def visualizar_mision(cedula):
    with open(f'misiones/{cedula}.txt', "r", encoding='utf-8') as file:
        contenido = file.read()
    print(contenido)


def seleccionar_y_ver_mision(misiones):
    print("\nMisiones disponibles:")
    for i, mision in enumerate(misiones, start=1):
        print(f"{i}. {mision['Mision']}")

    # Para elegir que mision ver
    eleccion = int(input("\nEscriba el numero de la mision que desea visualizar: ")) - 1

    # Visualizar la mision elegida
    print(f"Mision - {mision['Mision']}")
    print(f"En el planeta: - {mision['En el planeta']}")
    print(f"Con la nave - {mision['Con la nave']}")
    print(f"Con las armas - {', '.join(mision['Con las armas'])}")
    print(f"Con los integrantes - {', '.join(mision['Con los integrantes'])}")
     



        












             