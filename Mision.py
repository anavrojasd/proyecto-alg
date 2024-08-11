import csv

def cargar_planetas(archivo):
    planetas = []

def cargar_naves(archivo):
    naves = []    



class Mision:
    def __init__(self, nombre, planeta_destino, nave, armas, integrantes):
        self.nombre=nombre
        self.planeta_destino=planeta_destino
        self.nave=nave
        self.armas=armas
        self.integrantes=integrantes


    def crear_mision(self):
        print('Ingrese los datos:')
        nombre=input('Nombre de la mision: ')
        print("Ingrese el planeta destino: ")
        contador=1

