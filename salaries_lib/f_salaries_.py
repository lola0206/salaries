"""Función mayus:convierte los nombres de las columnas del dataset a mayúsculas"""
def mayus(salaries_df):
    salaries_df.columns = salaries_df.columns.str.upper()
    return(salaries_df)

"""Función download_data: Descarga el dataset salaries desde Github hasta la carpeta especificada por el usuario"""
import requests
import pathlib
def download_data(path_file):
    location = pathlib.Path(path_file)
    folder = location.parents
    pathlib.Path(folder).mkdir(exist_ok=True)
    url = "https://raw.githubusercontent.com/colombia-dev/data/master/salaries/2020/raw.csv"
    r = requests.get(url, allow_redirects= True)
    with open(location, "wb") as f:
        f.write(r.content)
    return str(path_file)

