import json
import re

def leer_archivo(archivo_json:str) -> list:
    lista_nba = []
    with open(archivo_json,"r") as archivo:
        diccionario = json.load(archivo)
        lista_nba = diccionario["jugadores"]
    return lista_nba

ruta = r"C:\Users\User\Documents\1 Cuatrimestre UTN Programacion\parcial\dt.json"

lista_nba = leer_archivo(ruta)

def muestra_jugador_posicion(lista:list) -> list:
    mensaje = ""
    contador = 0
    for jugador in lista:
        mensaje += "{0} {1} - {2}\n".format(contador,jugador["nombre"],jugador["posicion"])
        contador += 1
    print(mensaje)

#muestra_jugador_posicion(lista_nba)

def muestra_estadistica_por_indice(indice:int,lista:list) -> bool:
    flag = False
    mensaje = "{0}:\n".format(lista[indice]["nombre"])
    for clave,valor in lista[indice]["estadisticas"].items():
        mensaje += "{0}: {1}\n".format(clave.replace("_"," ").capitalize(),valor)
        flag = True
    if flag:
        print(mensaje)
        return flag

#muestra_estadistica_por_indice(1,lista_nba)

def guardar_csv(ruta:str,texto:str):
    flag_resultado = False
    with open(ruta,"w+") as archivo:
        byte = archivo.write(texto) 
        if byte != 0:
            flag_resultado = True
    if flag_resultado :
        print("Se creó el archivo: {0}".format(ruta))
    else:
        print("Error al crear el archivo: {0}".format(ruta))
    return flag_resultado

def crear_texto_por_indice(indice:int,lista:list,flag:bool):
    if flag:
        lista_valores = []
        claves = list(lista[indice].keys()) 
        claves.remove("estadisticas")
        claves.remove("logros")
        clave_estadistica = list(lista[indice]["estadisticas"].keys())
        texto_valores = ""
        for i in range(len(claves)):
            claves[i] = claves[i].capitalize()
        for clave,valor in lista[indice].items():
            if clave in claves:
                lista_valores.append(valor)
        for clave,valor in lista[indice]["estadisticas"].items():
            if clave in clave_estadistica:
                lista_valores.append(str(valor))
        texto_valores = ",".join(lista_valores)
        for clave in clave_estadistica:
            claves.append(clave.replace("_"," ").capitalize())
        texto_claves = ",".join(claves)
        texto_csv = texto_claves + '\n' + texto_valores
        ruta = "{0}.csv".format(lista[indice]["nombre"])
        flag = guardar_csv(ruta,texto_csv)
    else:
        print("No usaste punto 2")
    
#crear_texto_por_indice(0,lista_nba,True)


def muestra_logros_por_nombre(nombre:str,lista:list):
    patron = rf"{nombre}"
    mensaje = ""
    for jugador in lista:
        if re.search(patron,jugador["nombre"].lower()):
            mensaje = "{0}:\n".format(jugador["nombre"])
            for logro in jugador["logros"]:
                mensaje += "{0}\n".format(logro)
            print(mensaje)
#muestra_logros_por_nombre("john",lista_nba)

# def quick_sort_estadistica(lista:list,clave:str,flag:bool):
#     lista_de = []
#     lista_iz = []
#     if len(lista) <= 1:
#             return lista
#     else:
#         cantidad = len(lista)
#         pivot = lista[0]
#         for i in range(1,cantidad):
#             if flag == True and lista[i]["estadisticas"][clave] > pivot["estadisticas"][clave] or flag == False and lista[i]["estadisticas"][clave] < pivot["estadisticas"][clave]:
#                 lista_de.append(lista[i])
#             elif flag == True and lista[i]["estadisticas"][clave] <= pivot["estadisticas"][clave] or flag == False and lista[i]["estadisticas"][clave] > pivot["estadisticas"][clave]:
#                 lista_iz.append(lista[i])
#     lista_iz = quick_sort_estadistica(lista_iz,clave,flag)
#     lista_iz.append(pivot)
#     lista_de = quick_sort_estadistica(lista_de,clave,flag)
#     lista_iz.extend(lista_de)
#     return lista_iz

def quick_sort_(lista:list,clave:str,flag:bool):
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
            return lista
    else:
        cantidad = len(lista)
        pivot = lista[0]
        for i in range(1,cantidad):
            if flag == True and lista[i][clave] > pivot[clave] or flag == False and lista[i][clave] < pivot[clave]:
                lista_de.append(lista[i])
            elif flag == True and lista[i][clave] <= pivot[clave] or flag == False and lista[i][clave] > pivot[clave]:
                lista_iz.append(lista[i])
    lista_iz = quick_sort_(lista_iz,clave,flag)
    lista_iz.append(pivot)
    lista_de = quick_sort_(lista_de,clave,flag)
    lista_iz.extend(lista_de)
    return lista_iz

lista = quick_sort_(lista_nba,"nombre",True)
mensaje = ""
for jugador in lista:
    mensaje += "Nombre: {0} - puntos por partido: {1}\n".format(jugador["nombre"],jugador["estadisticas"]["promedio_puntos_por_partido"])
print(mensaje)

