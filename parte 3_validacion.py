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


def busca_y_muestra_por_nombre(nombre:str,lista:list,opcion:int):
    patron = rf"{nombre}"
    segundo_patron = r"^Miembro del Salon de la Fama del Baloncesto$"
    mensaje = ""
    for jugador in lista:
        if re.search(patron,jugador["nombre"].lower()):
            match opcion:
                case 4:
                    mensaje = "{0}:\n".format(jugador["nombre"])
                    for logro in jugador["logros"]:
                        mensaje += "{0}\n".format(logro)
                    print(mensaje)
                case 6:
                    for logro in jugador["logros"]:
                        if re.search(segundo_patron,logro):
                            mensaje = "El jugador {0} es HALL OF FAME".format(jugador["nombre"])
                    if mensaje == "":
                        mensaje = "El jugador {0} no es HALL OF FAME".format(jugador["nombre"])
                    print(mensaje)

#busca_y_muestra_por_nombre("laettner",lista_nba,6)

def quick_sort_estadistica(lista:list,clave:str,flag:bool):
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
            return lista
    else:
        cantidad = len(lista)
        pivot = lista[0]
        for i in range(1,cantidad):
            if flag == True and lista[i]["estadisticas"][clave] > pivot["estadisticas"][clave] or flag == False and lista[i]["estadisticas"][clave] < pivot["estadisticas"][clave]:
                lista_de.append(lista[i])
            elif flag == True and lista[i]["estadisticas"][clave] <= pivot["estadisticas"][clave] or flag == False and lista[i]["estadisticas"][clave] > pivot["estadisticas"][clave]:
                lista_iz.append(lista[i])
    lista_iz = quick_sort_estadistica(lista_iz,clave,flag)
    lista_iz.append(pivot)
    lista_de = quick_sort_estadistica(lista_de,clave,flag)
    lista_iz.extend(lista_de)
    return lista_iz
def suma(lista:list,clave:str) -> int|float:
    suma = 0
    for jugador in lista:
        suma += jugador["estadisticas"][clave]
    return suma

def quick_sort(lista:list,clave:str,flag:bool):
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
    lista_iz = quick_sort(lista_iz,clave,flag)
    lista_iz.append(pivot)
    lista_de = quick_sort(lista_de,clave,flag)
    lista_iz.extend(lista_de)
    return lista_iz

lista = quick_sort(lista_nba,"nombre",True)
# mensaje = ""
# for jugador in lista:
#     mensaje += "Nombre: {0} - puntos por partido: {1}\n".format(jugador["nombre"],jugador["estadisticas"]["promedio_puntos_por_partido"])
# print(mensaje)

lista = quick_sort_estadistica(lista_nba,"promedio_puntos_por_partido",False)
# suma_final = suma(lista,"asistencias_totales")
# mensaje = "La cantidad de rebotes_totales es de: {0} siendo {1} el jugador con la cantidad mas alta de: {2}".format(suma_final,lista[0]["nombre"],lista[0]["estadisticas"]["asistencias_totales"])
# print(mensaje)

def muestra_jugadores_mayor_que_valor_dado(valor:int,clave:str,lista:list):
    if valor < lista[0]["estadisticas"][clave]:
        mensaje = "Los jugadores que promedian mas que {0} son:\n".format(valor)
        for jugador in lista:
            if jugador["estadisticas"][clave] > valor:
                mensaje += "Nombre: {0} - {1}: {2}\n".format(jugador["nombre"],clave.replace("_"," ").capitalize(), jugador["estadisticas"][clave])
        print(mensaje)
    else:
        print("No hay jugadores que promediaron mas que {0}".format(valor))

muestra_jugadores_mayor_que_valor_dado(25,"promedio_puntos_por_partido",lista)

def imprimir_menu():
    print("Menú de opciones:")
    print("1. Recorrer la lista de heroes")  
    print("2. Mostrar el nombre de cada superheroe")
    print("3. Mostrar el nombre de cada superheroe con su altura")
    print("4. Determinar cuál es el superhéroe más alto")
    print("5. Determinar cuál es el superhéroe más bajo")
    print("6. Determinar la altura promedio de los superhéroes")
    print("7. Mostrar la identidad del superheroe con la altura mas alta y mas baja")
    print("8. Informar cual es el superhéroe más y menos pesado.")
    print("0. Salir del menu")

def validar_entero(numero:str) -> bool:
    patron = r"^(?:[0-9]|1[0-9]|2[0-3])$"
    if re.match(patron, str(numero)):
        return True
    else:
        return False

def nba_menu_principal():
    imprimir_menu()
    opcion = input("\nIngrese la opción deseada: ")
    booleano = validar_entero(opcion)
    if(booleano == True):
        opcion_int = int(opcion)
        return opcion_int
    else:
        return -1

def nba_app(lista_personajes:list):
    while(True):
        opcion_int = nba_menu_principal()
        if(type(opcion_int) == int):
            match opcion_int:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 23:
                    pass
                case 0:
                    break
                case _:
                    print("Opcion no valida,numeros del 0 al 23 sin el 21 o 22")
        else:
            print("Opcion no valida,numeros del 0 al 23 sin el 21 o 22")
        
nba_app(lista_nba)

