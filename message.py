import pandas as pd
import pywhatkit as kit
from datetime import datetime, timedelta

# Ruta del archivo Excel
file_path = 'C:/Users/CGOROSTIAGA/Desktop/Carlos/Varios 1/script-python/datos.xlsx'

# Cargar el archivo Excel y leer los datos
df = pd.read_excel(file_path)

# Cálculo de la fecha del próximo domingo
hoy = datetime.now()
domingo_proximo = hoy + timedelta((6 - hoy.weekday()) % 7)  # Próximo domingo

# Filtrar el DataFrame para los discursos del próximo domingo
df_domingo = df[df['Fecha'].astype(str) == domingo_proximo.strftime("%Y-%m-%d")]

# Iterar sobre cada discurso y enviar los mensajes
for index, row in df_domingo.iterrows():
    nombre = row['Discursante']
    telefono = row['Telefono']
    congregacion = row['Congregacion']
    bosquejo = row['Bosquejo']
    titulo = row['Titulo']

    # Imprimir los datos antes de enviar los mensajes
    print(f"Enviando mensajes a: {nombre}, Teléfono: {telefono}, Congregación: {congregacion}, Bosquejo: {bosquejo}, Título: {titulo}")

    # Primer mensaje de confirmación
    mensaje1 = f"""
    Hola buenas , hermano {nombre}, soy Carlos Gorostiaga de la congregación San Sebastián de los Reyes Centro, espero que estés bien. Quería confirmar que el próximo domingo {domingo_proximo.strftime('%d/%m/%Y')} haces el discurso público en nuestra congregación.
    
    El bosquejo asignado es el: {bosquejo}
    
    Tema: {titulo}

    Si te es posible, necesitaría que me indicaras el número de canción y si deseas utilizar alguna imagen, la envíes al correo:
    sonido.sansecentro@gmail.com
    
    Muchas gracias de antemano.
    """
    
    # Segundo mensaje de recordatorio
    mensaje2 = """
    Recordarte que la reunión es el Domingo a las 10:00 y el Salón del Reino está en Avenida de la Dehesa n6, San Sebastián de los Reyes. CP 28702, Sala 1 (es la sala de la planta superior)
    Muchas gracias por adelantado.
    Saludos. 
    
    https://maps.app.goo.gl/39jQfhkQX7Kqzb4PA?g_st=iw
    """

    # Enviar el primer mensaje de WhatsApp de inmediato
    kit.sendwhatmsg_instantly(f"+34{telefono}", mensaje1)
    print(f"Primer mensaje enviado a {nombre} con número {telefono}")
    
    # Enviar el segundo mensaje de WhatsApp de inmediato
    kit.sendwhatmsg_instantly(f"+34{telefono}", mensaje2)
    print(f"Segundo mensaje enviado a {nombre} con número {telefono}")
