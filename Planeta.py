class Planeta:
    def __init__(self, nombre_planeta, periodo_orbita, periodo_rotacion, cantidad_habitantes, tipo_clima):
        self.nombre_planeta = nombre_planeta
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_habitantes = cantidad_habitantes
        self.tipo_clima = tipo_clima

    def mostrar_planetas(self):
        print(f'''
        Datos del planeta:
        Nombre: {self.nombre_planeta}
        Período de órbita: {self.periodo_orbita}
        Período de rotación: {self.periodo_rotacion}
        Cantidad de habitantes: {self.cantidad_habitantes}
        Tipo de clima: {self.tipo_clima}
        Lista de episodios en los que aparece: 
        Lista de los personajes originarios del planeta: 
                        ''')
