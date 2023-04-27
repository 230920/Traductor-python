import google.auth # Importamos librerias
from google.cloud import translate_v2 as translate
#Definimos una función llamada traducir que acepta tres parámetros: texto, idioma_origen e idioma_destino.
def traducir(texto, idioma_origen, idioma_destino):
    credenciales, proyecto = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    traductor = translate.Client(credentials=credenciales)
#utilizamos la función translate() del cliente de la API de traducción para enviar una solicitud de traducción.
    resultado = traductor.translate(texto, source_language=idioma_origen, target_language=idioma_destino)

    return resultado["translatedText"]

idioma_origen = input("Ingrese el idioma de origen: ")
idioma_destino = input("Ingrese el idioma de destino: ")
texto = input("Ingrese el texto a traducir: ")

texto_traducido = traducir(texto, idioma_origen, idioma_destino)

print("El texto traducido es:", texto_traducido)