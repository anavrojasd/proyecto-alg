import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def csv_battles():
    # Specify the path to your Excel file
    file_path = './csv/battles.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

        # Display the first few rows of the DataFrame
    print(df.head())

###################### Número 5 del menú ####################################

def csv_characters():
    # Specify the path to your Excel file
    file_path = './csv/characters.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)
    return df

def nombre_planeta(df):

    # Group by 'homeworld' and count the number of characters in each group
    cant_planetas= df.groupby('homeworld').size()

    # Convert the result to a dictionary
    diccionario_planeta = cant_planetas.to_dict()

    nombre_planeta = list(diccionario_planeta.keys())
    cantidad_nacidos = list(diccionario_planeta.values())
    fig, ax = plt.subplots(figsize=(10,7))

    # Display the pie chart
    ax.pie(cantidad_nacidos, startangle=140)
    leyenda_titulos = [f'{label}: {sum(cantidad_nacidos)}' for label, size in zip(nombre_planeta, cantidad_nacidos)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Cantidad de Personajes Nacidos en cada Planeta", loc='center left', bbox_to_anchor=(1,0.5),fontsize='small')
    plt.show()

#######################################################################################

def csv_cities():
    # Specify the path to your Excel file
    file_path = './csv/cities.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_droids():
    # Specify the path to your Excel file
    file_path = './csv/droids.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_events():
    # Specify the path to your Excel file
    file_path = './csv/events.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_films():
    # Specify the path to your Excel file
    file_path = './csv/films.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_music():
    # Specify the path to your Excel file
    file_path = './csv/music.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_organizations():
    # Specify the path to your Excel file
    file_path = './csv/organizations.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_planets():
    # Specify the path to your Excel file
    file_path = './csv/planets.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_quotes():
    # Specify the path to your Excel file
    file_path = './csv/quotes.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_species():
    # Specify the path to your Excel file
    file_path = './csv/species.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

################################ Número 6 del Menú #############################

def csv_starships():
    # Specify the path to your Excel file
    file_path = './csv/starships.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)
    return df
    
def longitud_de_nave(df):
    longitud_nave= dict(zip(df['name'], df['length']))
    #Grafica para longitud
    claves_longitud = list(longitud_nave.keys())
    valor_longitud = list(longitud_nave.values())
    fig, ax = plt.subplots(figsize=(10,7))

    # Display the pie chart
    ax.pie(valor_longitud, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_longitud) * 100:.1f}%' for label, size in zip(claves_longitud, valor_longitud)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="center left", bbox_to_anchor=(1,0.5),fontsize='small')
    plt.show()
   
   
   
def capacidad_de_nave(df):
    capacidad_nave= dict(zip(df['name'], df['cargo_capacity']))
    
    #Grafica para capacidad
    claves_capacidad = list(capacidad_nave.keys())
    valor_capacidad = list(capacidad_nave.values())
    valor_capacidad = [0 if np.isnan(x) else x for x in valor_capacidad]
    fig, ax = plt.subplots(figsize=(10,7))

    # Display the pie chart
    ax.pie(valor_capacidad, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_capacidad) * 100:.1f}%' for label, size in zip(claves_capacidad, valor_capacidad)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="center left", bbox_to_anchor=(1,0.5),fontsize='small')
    plt.show() 

def hiperimpulso_de_nave(df):
    hiperimpulso_nave= dict(zip(df['name'], df['hyperdrive_rating']))
    claves_hiperimpulso = list(hiperimpulso_nave.keys())
    valor_hiperimpulso= list(hiperimpulso_nave.values())
    valor_hiperimpulso = [0 if np.isnan(x) else x for x in valor_hiperimpulso]
    fig, ax = plt.subplots(figsize=(10,7))

    # Display the pie chart
    ax.pie(valor_hiperimpulso, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_hiperimpulso) * 100:.1f}%' for label, size in zip(claves_hiperimpulso, valor_hiperimpulso)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="center left", bbox_to_anchor=(1,0.5),fontsize='small')
    plt.show() 

def mglt_de_nave(df):
    mglt_nave= dict(zip(df['name'], df['MGLT']))
    claves_mglt = list(mglt_nave.keys())
    valor_mglt= list(mglt_nave.values())
    valor_mglt = [0 if np.isnan(x) else x for x in valor_mglt]

    fig, ax = plt.subplots(figsize=(10,7))

    # Display the pie chart
    ax.pie(valor_mglt, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_mglt) * 100:.1f}%' for label, size in zip(claves_mglt, valor_mglt)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="center left", bbox_to_anchor=(1,0.5),fontsize='small')
    plt.show() 

##########################################################################################################

def csv_timeline():
    # Specify the path to your Excel file
    file_path = './csv/timeline.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_vehicles():
    # Specify the path to your Excel file
    file_path = './csv/vehicles.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

def csv_weapons():
    # Specify the path to your Excel file
    file_path = './csv/weapons.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

################################ Número 7 del Menú ############################## 

def estadisticas_aeronaves():
    # Specify the path to your CSV file
    file_path = './csv/starships.csv'

    # Read the CSV file
    df = pd.read_csv(file_path)

    #Trae los estadisticos basicos de hiperimpulso
    minimo_hiperimpulsor= pd.Series(df.hyperdrive_rating.values).min()
    maximo_hiperimpulsor= pd.Series(df.hyperdrive_rating.values).max()
    promedio_hiperimpulsor= pd.Series(df.hyperdrive_rating.values).mean()
    moda_hiperimpulsor= pd.Series(df.hyperdrive_rating.values.flatten()).mode().iloc[0]


    #Trae los estadisticos basicos de costo
    minimo_costos= pd.Series(df.cost_in_credits.values).min()
    maximo_costos= pd.Series(df.cost_in_credits.values).max()
    promedio_costos= pd.Series(df.cost_in_credits.values).mean()
    moda_costos= pd.Series(df.cost_in_credits.values.flatten()).mode().iloc[0]


    #Trae los estadisticos basicos de MGLT
    minimo_mglt= pd.Series(df.MGLT.values).min()
    maximo_mglt= pd.Series(df.MGLT.values).max()
    promedio_mglt= pd.Series(df.MGLT.values).mean()
    moda_mglt= pd.Series(df.hyperdrive_rating.values.flatten()).mode().iloc[0]


    #Trae los estadisticos basicos de velocidad max
    minimo_velocidad_max= pd.Series(df.max_atmosphering_speed.values).min()
    maximo_velocidad_max= pd.Series(df.max_atmosphering_speed.values).max()
    promedio_velocidad_max= pd.Series(df.max_atmosphering_speed.values).mean()
    moda_velocidad_max= pd.Series(df.max_atmosphering_speed.values.flatten()).mode().iloc[0]

    info=pd.DataFrame(columns=['Aspectos','Minimo','Maximo','Promedio','Moda'])
    caracteristicas= ['Hiperimpulsor', 'Costos', 'MGLT','Velocidad Max']
    info['Aspectos']=np.array(caracteristicas)

    minimo_lista = [minimo_hiperimpulsor, minimo_costos, minimo_mglt, minimo_velocidad_max]
    maximo_lista = [maximo_hiperimpulsor, maximo_costos, maximo_mglt, maximo_velocidad_max]
    promedio_lista = [promedio_hiperimpulsor, promedio_costos, promedio_mglt, promedio_velocidad_max]
    moda_lista = [moda_hiperimpulsor, moda_costos, moda_mglt, moda_velocidad_max]
    
    info["Aspectos"] = np.array(caracteristicas)
    info["Minimo"] = np.array(minimo_lista)
    info["Maximo"] = np.array(maximo_lista)
    info["Promedio"] = np.array(promedio_lista)
    info["Moda"] = np.array(moda_lista)
    
    
    
    print(info)
