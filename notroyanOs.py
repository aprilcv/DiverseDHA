import os

def analizar_archivo(archivo):
    # Lista de palabras clave asociadas a troyanos
    palabras_clave = ['malware', 'troyano', 'backdoor', 'keylogger', 'spyware', 'rootkit']

    # Leer el contenido del archivo en modo binario
    with open(archivo, 'rb') as f:
        contenido = f.read()

    # Verificar si alguna palabra clave está presente en el contenido del archivo
    for palabra in palabras_clave:
        if palabra.encode() in contenido:
            print(f'Cuidadito eee, esto esta peligrosho: {archivo} - Palabra clave encontrada: {palabra}')
            return True
//abrilestuvoaquiholi//
    return False

def explorar_directorio(directorio):
    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(directorio)

    # Analizar cada archivo en el directorio
    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_archivo):
            analizar_archivo(ruta_archivo)
        elif os.path.isdir(ruta_archivo):
            explorar_directorio(ruta_archivo)

# Directorio a explorar
directorio_inicial = '/ruta/del/directorio/a/explorar'

# Iniciar la exploración del directorio
explorar_directorio(directorio_inicial)
