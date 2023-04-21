import psutil
from datetime import datetime

def obtener_tiempo_uso_aplicaciones():
    """
    Obtiene el tiempo de uso de cada aplicación en la sesión actual.
    """
    # Obtener una lista de todos los procesos en ejecución
    procesos = psutil.process_iter(['pid', 'name', 'create_time'])

    # Crear un diccionario para almacenar la información del tiempo de uso
    tiempo_uso_aplicaciones = {}

    # Obtener la hora actual para calcular el tiempo de uso
    hora_actual = datetime.now()

    # Recorrer cada proceso y obtener su tiempo de uso
    for proceso in procesos:
        pid = proceso.info['pid']
        nombre = proceso.info['name']
        hora_creacion = datetime.fromtimestamp(proceso.info['create_time'])
        tiempo_uso = hora_actual - hora_creacion

        # Actualizar el diccionario con el tiempo de uso del proceso
        if nombre not in tiempo_uso_aplicaciones:
            tiempo_uso_aplicaciones[nombre] = tiempo_uso
        else:
            tiempo_uso_aplicaciones[nombre] += tiempo_uso

    return tiempo_uso_aplicaciones

# Obtener el tiempo de uso de las aplicaciones en la sesión actual
tiempo_uso_aplicaciones = obtener_tiempo_uso_aplicaciones()

# Imprimir el tiempo de uso de cada aplicación
for nombre, tiempo_uso in tiempo_uso_aplicaciones.items():
    print(f'Aplicación: {nombre} - Te pasas we, podrias hacer ejercicio: {tiempo_uso}')

//abril estuvo aqui