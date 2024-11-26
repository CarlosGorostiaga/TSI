import pandas as pd 
import requests
import os
from datetime import datetime

# Rutas de los archivos 
excel_path = r"C:\Users\CGOROSTIAGA\Desktop\Carlos\coordenadas.xlsx"
resultados = r"C:\Users\CGOROSTIAGA\Desktop\Carlos\resultadosCoord.xlsx"
log_path = r"C:\Users\CGOROSTIAGA\Desktop\Carlos\log-direcciones.txt"

# Clave de la API de Google Maps
api_key = "AIzaSyCIto10Nr6YkkQUi3izyHH27kDtQgwYIHw"

# Eliminar el archivo si esta duplicado
if os.path.exists(log_path): 
    os.remove(log_path)

# Crear archivo de log
with open(log_path, "w") as log_file:
    log_file.write("Inicio del procesamiento de datos: {datetime.now()}\n") 

# Leer datos del archivo Excel original 
data = pd.read_excel(excel_path)

# Registrar informacion inicial en el log
with open(log_path, "a") as log_file:
    log_file.write(f"Encabezados detectados en el Excel: {', '.join(data.columns)}\n")

# Crear una lista para almacenar los resultados
resultados = []

# Procesamiento de Datos de cada fila del archivo original : 
for index, row in data.iterrows():
    ref_obra = row.get("REF OBRA", "")
    signo = row.get("Signo")
    direccion = row.get("Dirección")
    poblacion = row.get("Población")
    provincia = row.get("Provincia")
    cp = row.get("CP", "")

    # Concatenar la dirección completa de forma segura
    direccion_completa = f"{signo} {direccion}, {poblacion}, {provincia}, {cp}".strip(",")

    # Registrar la direccion concatenada en log 
    with open(log_path, "a") as log_file: 
        log_file.write(f"Dirección concatenada: {direccion_completa}\n")

    # Llamar a API de Google Maps 
    latitud, longitud = "", ""
    if direccion_completa.strip() != "": 
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={requests.utils.quote(direccion_completa)}&key={api_key}"
        try: 
            response = requests.get(url)
            response_data = response.json()

            if response_data["status"] == "OK": 
                location = response_data["results"][0]["geometry"]["location"]
                latitud = location["lat"]
                longitud = location["lng"]

            else: 
                