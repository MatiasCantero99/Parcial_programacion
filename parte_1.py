import json

def leer_archivo(archivo_json:str) -> list:
    lista_nba = []
    with open(archivo_json,"r") as archivo:
        diccionario = json.load(archivo)
        lista_nba = diccionario["jugadores"]
    return lista_nba

ruta = r"C:\Users\User\Documents\1 Cuatrimestre UTN Programacion\J2TR4AQ3AFDEHIMSLSVWIZXH6Q.jpg"

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

muestra_estadistica_por_indice(1,lista_nba)

def crear_texto_por_indice(indice:int,lista:list,flag:bool):
    if flag:
        lista_valores = []
        claves = list(lista[indice].keys()) 
        claves.remove("estadisticas")
        claves.remove("logros")
        print(claves)
        clave_estadistica = list(lista[indice]["estadisticas"].keys())
        texto_valores = ""
        for clave,valor in lista[indice].items():
            if clave in claves:
                lista_valores.append(valor)
        
        for clave in clave_estadistica:
            claves.append(clave.replace("_"," "))
        texto_claves = ",".join(claves)
        print(texto_claves)
        return texto_claves + '\n' + texto_valores
    
texto = crear_texto_por_indice(0,lista_nba,True)
print(texto)

