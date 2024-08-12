from estadistica import csv_planets, csv_starships, csv_weapons, csv_characters
from Usuario import Usuario
class Mision:

    usuario_obj=[]

    def __init__(self, nombre, planeta_destino, nave, armas, integrantes):
        self.nombre=nombre
        self.planeta_destino=planeta_destino
        self.nave=nave
        self.armas=armas
        self.integrantes=integrantes


def crear_mision(self):
    print('Ingrese sus datos: ')
    cedula=int(input("\tCedula: "))
    usuario_seleccionado=self.buscar_usuario_lineal(cedula)
    if not usuario_seleccionado:
        nombre=input("\tNombre: ")
        apellido=input("\tApellido: ")
    else:
        nombre=usuario_seleccionado.nombre
        apellido=usuario_seleccionado.apellido
        print("Puede empezar a crear su mision")
        nombre_mision=input("Nombre de la mision: ")


def buscar_usuario_lineal(self, cedula):
        for usuario in self.usuario_obj:
            if usuario.cedula==cedula:
                return usuario
        return None  

def elegir_planeta(self):
    lista_planetas=[]
    

def elegir_nave(self):
    lista_naves=[]

def elegir_armas(self):
    lista_armas=[] 

def elegir_integrantes(self):
    lista_personajes=[]       

        
