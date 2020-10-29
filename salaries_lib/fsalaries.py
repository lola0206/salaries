import requests
import pathlib
 


def mayus(salaries_df):
    #Convierte los nombres de las columnas del dataset a mayúsculas
    
    #Parametros: 
    # salaries_df (dataframe): el data frame para el cual se necesita modificar los nombres de las columnas 
    
    #Regresa:
    # salaries_df (dataframe): el dataframe modificado

    salaries_df.columns = salaries_df.columns.str.upper()
    return(salaries_df)



def download_data(path_file):
    #Descarga el dataset salaries desde Github hasta la carpeta especificada por el usuario

    #Parametros:
    #path_file (str): ruta de almacenamiento del archivo, junto con su nombre
    
    #Regresa:
    #path_file (str): la ruta donde fue almacenado con éxito el archivo junto con el nombre dle mismo

    location = pathlib.Path(path_file)
    folder = location.parent
    pathlib.Path(folder).mkdir(exist_ok=True)
    url = "https://raw.githubusercontent.com/colombia-dev/data/master/salaries/2020/raw.csv"
    r = requests.get(url, allow_redirects= True)
    with open(location, "wb") as f:
        f.write(r.content)
    return str(path_file)



def sel(salaries_df):
    #Crea  un dataframe con las columnas necesarias para comenzar la limpieza

    #Parametros: 
    #salaries_df (dataframe)

    #Regresa: 
    #salaries_df (dataframe): dataframe con las columnas seleccionadas 

    salaries_df = salaries_df[["¿A usted le pagan en pesos colombianos (COP) o dólares (USD)?",
                                    "¿Usando la moneda de la respuesta anterior, cuánto es su remuneración ANUAL base?  eg 36,000,000 si es pesos o 3,600 si es dólares"]]
    return(salaries_df)



def divide(salaries_df):
    #Crea  dos data frame separados para analizar quienen ganan en pesos y dólares


    #Parametros: 
    #salaries_df (dataframe)

    #Regresa: 
    #salaries_df_pesos (dataframe): dataframe con valores en peso
    #salaries_df_dolar (dataframe): dataframe con valores en peso

    salaries_df_pesos =  salaries_df.loc[salaries_df["¿A USTED LE PAGAN EN PESOS COLOMBIANOS (COP) O DÓLARES (USD)?"]== "pesos",:]
    salaries_df_dolar =  salaries_df.loc[salaries_df["¿A USTED LE PAGAN EN PESOS COLOMBIANOS (COP) O DÓLARES (USD)?"]== "dólares",:]

    return(salaries_df_pesos,salaries_df_dolar)
