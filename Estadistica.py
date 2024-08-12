import pandas as pd

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

    return df

def nombres_personajes(df):
    nombres = df['name'].tolist()
    return nombres

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
    return df

def nombres_planetas(df):
    nombres = df['name'].tolist()
    return nombres

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

    # Display the first few rows of the DataFrame
    
    return df

def nombres_naves(df):
    nombres = df['name'].tolist()
    return nombres

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
    
    return df

def nombres_armas(df):
    nombres = df['name'].tolist()
    return nombres



