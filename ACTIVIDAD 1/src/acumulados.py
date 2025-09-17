#Contiene funciones para inicializar y actualizar los acumulados por equipo.

def inicializar_acumulados(equipos: list[str]) #--> dict

#Crea un diccionario base con los campos:
#{"innovacion": 0, "presentacion": 0, "errores": 0, "mejores": 0, "total": 0}.

def actualizar_acumulados(acum: dict, ronda: dict, mejor: str) #--> dict

#Suma innovacion,presentacion,errores,totales.
#Incrementa el contador de mejores equipos si corresponde
#O sea, en una sola pasada tiene que tocar todos los campos del acumulado.