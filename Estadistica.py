import pandas as pd
import matplotlib.pyplot as plt
import numpy as num

def csv_battles():
    # Specify the path to your Excel file
    file_path = './csv/battles.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

        # Display the first few rows of the DataFrame
    print(df.head())

def csv_characters():
    # Specify the path to your Excel file
    file_path = './csv/characters.csv'

    # Read the Excel file
    df = pd.read_csv(file_path)

    # Group by 'homeworld' and count the number of characters in each group
    cant_planetas= df.groupby('homeworld').size()

    # Convert the result to a dictionary
    diccionario_planeta = cant_planetas.to_dict()

    # Display the dictionary
    print(diccionario_planeta)

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
    fig, ax = plt.subplots()

    # Display the pie chart
    ax.pie(valor_longitud, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_longitud) * 100:.1f}%' for label, size in zip(claves_longitud, valor_longitud)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="upper center", bbox_to_anchor=(0.5,-0.05),ncol=1)
    plt.show()
   
   
   
def capacidad_de_nave(df):
    capacidad_nave= dict(zip(df['name'], df['cargo_capacity']))
    #Grafica para capacidad
    claves_capacidad = list(capacidad_nave.keys())
    valor_capacidad= list(capacidad_nave.values())
    fig, ax = plt.subplots()

    # Display the pie chart
    ax.pie(valor_capacidad, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_capacidad) * 100:.1f}%' for label, size in zip(claves_capacidad, valor_capacidad)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="upper center", bbox_to_anchor=(0.5,-0.05),ncol=1)
    plt.show() 

def hiperimpulso_de_nave(df):
    hiperimpulso_nave= dict(zip(df['name'], df['hyperdrive_rating']))
    claves_hiperimpulso = list(hiperimpulso_nave.keys())
    valor_hiperimpulso= list(hiperimpulso_nave.values())
    fig, ax = plt.subplots()

    # Display the pie chart
    ax.pie(valor_hiperimpulso, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_hiperimpulso) * 100:.1f}%' for label, size in zip(claves_hiperimpulso, valor_hiperimpulso)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="upper center", bbox_to_anchor=(0.5,-0.05),ncol=1)
    plt.show() 

def mglt_de_nave(df):
    mglt_nave= dict(zip(df['name'], df['MGLT']))
    claves_mglt = list(mglt_nave.keys())
    valor_mglt= list(mglt_nave.values())
    fig, ax = plt.subplots()

    # Display the pie chart
    ax.pie(valor_mglt, startangle=140)
    leyenda_titulos = [f'{label}: {size/ sum(valor_mglt) * 100:.1f}%' for label, size in zip(claves_mglt, valor_mglt)]

    # Add the legend below the pie chart
    ax.legend(leyenda_titulos, title="Naves", loc="upper center", bbox_to_anchor=(0.5,-0.05),ncol=1)
    plt.show() 



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


