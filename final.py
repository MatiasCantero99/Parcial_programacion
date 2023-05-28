import json
import re

def leer_archivo(archivo_json:str) -> list:
    """
    Lee un archivo json
    recive el archivo json por parametro 
    devuelve una lista con jugadores nba
    """
    lista_nba = []
    with open(archivo_json,"r") as archivo:
        diccionario = json.load(archivo)
        lista_nba = diccionario["jugadores"]
    return lista_nba

ruta = r"C:\Users\User\Documents\1 Cuatrimestre UTN Programacion\parcial\dt.json"

lista_nba = leer_archivo(ruta)

def muestra_jugador_posicion(lista:list):
    """
    muestra el nombre del jugador y su posicion en la cancha
    recive una lista por parametro
    no devuelve nada
    """
    mensaje = ""
    contador = 0
    for jugador in lista:
        mensaje += "{0} {1} - {2}\n".format(contador,jugador["nombre"],jugador["posicion"])
        contador += 1
    print(mensaje)

def muestra_estadistica_por_indice(indice:int,lista:list) -> bool:
    """
    muestra las estadisticas de un jugador por su indice
    recive un indice y una lista por parametro
    devuelve un bool True o False
    """
    flag = False
    mensaje = "{0}:\n".format(lista[indice]["nombre"])
    for clave,valor in lista[indice]["estadisticas"].items():
        mensaje += "{0}: {1}\n".format(clave.replace("_"," ").capitalize(),valor)
        flag = True
    if flag:
        print(mensaje)
        return flag

def guardar_csv(ruta:str,texto:str):
    """
    Guarda en un archivo csv
    recive una ruta donde se alojara el archivo y un texto que estara dentro por parametro
    no retorna nada
    """
    flag_resultado = False
    with open(ruta,"w+") as archivo:
        byte = archivo.write(texto) 
        if byte != 0:
            flag_resultado = True
    if flag_resultado :
        print("Se creó el archivo: {0}".format(ruta))
    else:
        print("Error al crear el archivo: {0}".format(ruta))

def crear_texto_por_indice(indice:int,lista:list,flag:bool):
    """
    Crea un texto en formato csv para despues guardarlo siempre y cuando usaste el punto 2
    recive un indice, una lista y un flag por parametro
    No retorna nada sino que manda el archivo a guardar_csv
    """
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
        guardar_csv(ruta,texto_csv)
    else:
        print("No usaste punto 2")

def calcular_max(lista:list,clave:str) -> list:
    """
    Calcula el max de una lista
    Recibe una lista y una clave por parametro
    devuelve una lista con el nombre y el valor maximo de la clave que buscaste
    """
    lista_maximos = []
    maximo = None
    jugador_max = ""
    for jugador in lista:
        if maximo == None or jugador["estadisticas"][clave] > maximo:
            maximo = jugador["estadisticas"][clave]
            jugador_max = jugador["nombre"]
    lista_maximos.append(maximo)
    lista_maximos.append(jugador_max)
    return lista_maximos

def calcular_min(lista:list,clave:str) -> list:
    """
    Calcula el min de una lista
    Recibe una lista y una clave por parametro
    devuelve una lista con el nombre y el valor minimo de la clave que buscaste
    """
    lista_minimos = []
    min = None
    jugador_min = ""
    for jugador in lista:
        if(min == None or jugador["estadisticas"][clave] < min):
            min = jugador[clave]
            jugador_min = jugador["nombre"]
    lista_minimos.append(min)
    lista_minimos.append(jugador_min)
    return jugador_min

def calcular_max_min_dato(lista:list,calculo_a_realizar:str,dato:str) -> list:
    """
    Calcular max o min dependiendo lo que pediste y lo envia a otra funcion
    Recibe una lista, el calculo que queres realizar y un dato por parametro
    Devuelve una lista proporcionada por calcular_min o calcular_max
    """
    if calculo_a_realizar == "maximo":
        pedido = calcular_max(lista,dato)
    else:
        pedido = calcular_min(lista,dato)
    return pedido

    
def busca_y_muestra_por_nombre(nombre:str,lista:list,opcion:int):
    """
    Busca por el nombre del jugador
    Recibe una lista, el nombre a buscar y la opcion por parametro
    No devuelve nada
    """
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

def quick_sort_estadistica(lista:list,clave:str,flag:bool) -> list:
    """
    Es un algoritmo de ordenamiento basado en las estadisticas
    Recibe una lista, clave y el flag para asc o desc por parametro
    Retorna una lista ordenada de forma asc o desc
    """
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
    """
    Suma valores de las estadisticas
    Recibe una lista y una clave por parametro
    Retorna la suma en int o float dependiendo sus valores
    """
    suma = 0
    for jugador in lista:
        suma += jugador["estadisticas"][clave]
    return suma

def suma_logros(lista:list,clave:str) -> int:
    """
    Suma los logros de los jugadores
    Recibe una lista y una clave por parametro
    Retorna la suma en int
    """
    suma = 0
    for jugador in lista:
        suma += len(jugador[clave])
    return suma

def sacar_promedio(suma:int,lista:list) -> float:
    """
    Saca el promedio
    Recibe una suma echa y una lista por parametro
    Retorna el promedio echo
    """
    cantida_lista = len(lista)
    promedio = suma / cantida_lista
    return promedio

def quick_sort(lista:list,clave:str,flag:bool):
    """
    Es un algoritmo de ordenamiento de forma asc o desc
    Recibe una lista, una clave y un flag por parametro
    No retorna nada
    """
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
            return lista
    else:
        cantidad = len(lista)
        pivot = lista[0]
        for i in range(1,cantidad):
            if type(lista[i][clave]) == list:
                if flag == True and len(lista[i][clave]) > len(pivot[clave]) or flag == False and len(lista[i][clave]) < len(pivot[clave]):
                    lista_de.append(lista[i])
                elif flag == True and len(lista[i][clave]) <= len(pivot[clave]) or flag == False and len(lista[i][clave]) >= len(pivot[clave]):
                    lista_iz.append(lista[i])
            else:
                if flag == True and lista[i][clave] > pivot[clave] or flag == False and lista[i][clave] < pivot[clave]:
                    lista_de.append(lista[i])
                elif flag == True and lista[i][clave] <= pivot[clave] or flag == False and lista[i][clave] >= pivot[clave]:
                    lista_iz.append(lista[i])
    lista_iz = quick_sort(lista_iz,clave,flag)
    lista_iz.append(pivot)
    lista_de = quick_sort(lista_de,clave,flag)
    lista_iz.extend(lista_de)
    return lista_iz

def muestra_jugadores_mayor_que_valor_dado(valor:int,clave:str,lista:list):
    """
    Muestra los jugadores que superen cierto valor
    Recibe un valor, una clave y una lista por parametro
    No retorna nada
    """
    lista_maximos = calcular_max_min_dato(lista,"maximo",clave)
    if valor < lista_maximos[0]:
        mensaje = "Los jugadores que promedian mas que {0} son:\n".format(valor)
        for jugador in lista:
            if jugador["estadisticas"][clave] > valor:
                mensaje += "Nombre: {0} - {1}: {2}\n".format(jugador["nombre"],clave.replace("_"," ").capitalize(), jugador["estadisticas"][clave])
        print(mensaje)
    else:
        print("No hay jugadores que promediaron mas que {0}".format(valor))

def muestra_jugador_por_posicion(lista:list,clave:str,lista_posicion:list,valor:int):
    """
    Muestra los jugadores que superen cierto valor pero por posicion
    Recibe una lista, una clave, otra lista pero de posicion y un valor por parametro
    No retorna nada
    """
    lista_maximos = calcular_max_min_dato(lista,"maximo",clave)
    if valor < lista_maximos[0]:
        contador = 0
        mensaje = "Los jugadores que promedian mas que {0} son:\n".format(valor)
        for posicion in lista_posicion:
            mensaje += "{0}:\n".format(posicion)
            for jugador in lista:
                if posicion == jugador["posicion"]:
                    if jugador["estadisticas"][clave] > valor:
                        mensaje += "Nombre: {0} - {1}: {2}\n".format(jugador["nombre"],clave.replace("_"," ").capitalize(), jugador["estadisticas"][clave])
        print(mensaje)
    else:
        print("No hay jugadores que promediaron mas que {0}".format(valor))

def crea_ranking_dream_team(lista:list,lista_titulo:list):
    """
    Crea un texto del ranking del dream team para mandar a guardar a csv
    Recibe una lista de los jugadores y una lista con el titulo del archivo por parametro
    No retorna nada
    """
    lista_puntos = quick_sort_estadistica(lista,"puntos_totales",False)
    lista_asistencia = quick_sort_estadistica(lista,"asistencias_totales",False)
    lista_rebotes = quick_sort_estadistica(lista,"rebotes_totales",False)
    lista_robos = quick_sort_estadistica(lista,"robos_totales",False)
    titulo = ",".join(lista_titulo)
    mensaje = ""
    for jugador in lista:
        for i in range(len(lista_puntos)):
            if re.match(jugador["nombre"], lista_puntos[i]["nombre"]):
                indice_puntos = i + 1
                break

        for i in range(len(lista_rebotes)):
            if re.match(jugador["nombre"], lista_rebotes[i]["nombre"]):
                indice_rebotes = i + 1
                break

        for i in range(len(lista_asistencia)):
            if re.match(jugador["nombre"], lista_asistencia[i]["nombre"]):
                indice_asistencias = i + 1
                break

        for i in range(len(lista_robos)):
            if re.match(jugador["nombre"], lista_robos[i]["nombre"]):
                indice_robos = i + 1
                break
        mensaje += "{0},{1},{2},{3},{4}\n".format(jugador["nombre"], indice_puntos, indice_rebotes, indice_asistencias, indice_robos)
    texto_csv = titulo + "\n" + mensaje
    guardar_csv("Ranking_DreamTeam.csv",texto_csv)
                    
def imprimir_menu():
    """
    Imprime el menu
    No recibe nada
    No retorna nada
    """
    print("Menú de opciones:")
    print("1. Muestra nombre y posicin del Dream Team")  
    print("2. Selecciona un jugador por indice y muestra sus estadisticas")
    print("3. Guardar las estadisticas del punto 2 en un csv")
    print("4. Ingresa el nombre de un jugador y muestra sus logros")
    print("5. Muestra puntos por partido por nombre de manera ascendente")
    print("6. Ingresa el nombre de un jugador y muestra si es Hall of fame o no")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo")
    print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales")
    print("10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor")
    print("11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor")
    print("12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor")
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales")
    print("15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor")
    print("23. Ingresar un valor y mostrar los")
    print("0. Salir del menu")

def validar_entero(numero:str) -> bool:
    """
    Valida un numero entero para el menu
    Recibe un numero entero
    Retorna un bool True o False
    """
    patron = r"^(?:[0-9]|1[0-9]|2[0-3])$"
    if re.match(patron, str(numero)):
        return True
    else:
        return False

def nba_menu_principal() -> int:
    """
    Manda a imprimir el menu principal y pide la opcion que quieras
    No recibe nada
    Retorna la opcion casteada a int o -1
    """
    imprimir_menu()
    opcion = input("\nIngrese la opción deseada: ")
    booleano = validar_entero(opcion)
    if(booleano == True):
        opcion_int = int(opcion)
        return opcion_int
    else:
        return -1

def nba_app(lista_jugadores:list):
    """
    Corre la app haciendo lo que pediste por el menu
    Recibe una lista por parametro
    No retorna nada
    """
    flag_case_2 = False
    while(True):
        opcion_int = nba_menu_principal()
        if(type(opcion_int) == int):
            match opcion_int:
                case 1:
                    muestra_jugador_posicion(lista_jugadores)
                case 2:
                    muestra_jugador_posicion(lista_jugadores)
                    numero = input("Ingrese el numero del jugador para ver sus estadisticas: ")
                    if re.search(r"^(?:[0-9]|1[0-1])$",numero):
                        if int(numero) < len(lista_jugadores):
                            flag_case_2 = muestra_estadistica_por_indice(int(numero),lista_jugadores)
                    else:
                        print("error")
                case 3:
                    if flag_case_2:
                        crear_texto_por_indice(int(numero),lista_jugadores,flag_case_2)
                    else:
                        print("No usaste punto 2")
                case 4:
                    nombre = input("Ingresa el nombre a buscar: ")
                    busca_y_muestra_por_nombre(nombre.lower(),lista_jugadores,4)
                case 5:
                    lista = quick_sort(lista_jugadores,"nombre",True)
                    mensaje = ""
                    for jugador in lista:
                        mensaje += "Nombre: {0} - puntos por partido: {1}\n".format(jugador["nombre"],jugador["estadisticas"]["promedio_puntos_por_partido"])
                    print(mensaje)
                case 6:
                    nombre = input("Ingresa el nombre a buscar: ")
                    busca_y_muestra_por_nombre(nombre.lower(),lista_jugadores,6)
                case 7:
                    clave = "rebotes_totales"
                    lista_maximo = calcular_max_min_dato(lista_jugadores,"maximo",clave)
                    suma_final = suma(lista_jugadores,clave)
                    mensaje = "La cantidad de rebotes totales es de: {0} siendo {1} el jugador con la cantidad mas alta de: {2}".format(suma_final,lista_maximo[1],lista_maximo[0])
                    print(mensaje)
                case 8:
                    clave = "porcentaje_tiros_de_campo"
                    lista_maximo = calcular_max_min_dato(lista_jugadores,"maximo",clave)
                    suma_final = suma(lista_jugadores,clave)
                    promedio = sacar_promedio(suma_final,lista_jugadores)
                    mensaje = "El promedio de porcentaje tiros de campo es de: {0} siendo {1} el jugador con la cantidad mas alta de: {2}".format(promedio,lista_maximo[1],lista_maximo[0])
                    print(mensaje)
                case 9:
                    clave = "asistencias_totales"
                    lista_maximo = calcular_max_min_dato(lista_jugadores,"maximo",clave)
                    suma_final = suma(lista_jugadores,clave)
                    mensaje = "La cantidad de asistencias totales es de: {0} siendo {1} el jugador con la cantidad mas alta de: {2}".format(suma_final,lista_maximo[1],lista_maximo[0])
                    print(mensaje)
                case 10:
                    clave = "promedio_puntos_por_partido"
                    valor = input("Ingresa un valor: ")
                    dato_valido = re.search(r"^[0-9]+$",valor)
                    if dato_valido:
                        muestra_jugadores_mayor_que_valor_dado(int(valor),clave,lista_jugadores)
                    else:
                        print("Solo numeros enteros")
                case 11:
                    clave = "promedio_rebotes_por_partido"
                    valor = input("Ingresa un valor: ")
                    dato_valido = re.search(r"^[0-9]+$",valor)
                    if dato_valido:
                        muestra_jugadores_mayor_que_valor_dado(int(valor),clave,lista_jugadores)
                    else:
                        print("Solo numeros enteros")
                case 12:
                    clave = "promedio_asistencias_por_partido"
                    valor = input("Ingresa un valor: ")
                    dato_valido = re.search(r"^[0-9]+$",valor)
                    if dato_valido:
                        muestra_jugadores_mayor_que_valor_dado(int(valor),clave,lista_jugadores)
                    else:
                        print("Solo numeros enteros")
                case 13:
                    clave = "robos_totales"
                    lista_maximo = calcular_max_min_dato(lista_jugadores,"maximo",clave)
                    suma_final = suma(lista_jugadores,clave)
                    mensaje = "La cantidad de robos totales es de: {0} siendo {1} el jugador con la cantidad mas alta de: {2}".format(suma_final,lista_maximo[1],lista_maximo[0])
                    print(mensaje)
                case 14:
                    clave = "bloqueos_totales"
                    lista_maximo = calcular_max_min_dato(lista_jugadores,"maximo",clave)
                    suma_final = suma(lista_jugadores,clave)
                    mensaje = "La cantidad de bloqueos totales es de: {0} siendo {1} el jugador con la cantidad mas alta de: {2}".format(suma_final,lista_maximo[1],lista_maximo[0])
                    print(mensaje)
                case 15:
                    clave = "porcentaje_tiros_libres"
                    valor = input("Ingresa un valor: ")
                    dato_valido = re.search(r"^[0-9]+$",valor)
                    if dato_valido:
                        muestra_jugadores_mayor_que_valor_dado(int(valor),clave,lista_jugadores)
                    else:
                        print("Solo numeros enteros")
                case 16:
                    clave = "promedio_puntos_por_partido"
                    lista = quick_sort_estadistica(lista_jugadores,clave,True)
                    suma_final = suma(lista[1:],clave)
                    promedio = sacar_promedio(suma_final,lista[1:])
                    mensaje = "El promedio de puntos por partido sin el jugador de menor cantidad es de: {0} ".format(promedio)
                    print(mensaje)
                case 17:
                    clave = "logros"
                    lista = quick_sort(lista_jugadores,clave,False)
                    suma_final = suma_logros(lista,clave)
                    mensaje = "La cantidad de logros obtenidos es de: {0} siendo {1} el jugador con la cantidad mas alta de: {2}".format(suma_final,lista[0]["nombre"],len(lista[0][clave]))
                    print(mensaje)
                case 18:
                    clave = "porcentaje_tiros_triples"
                    valor = input("Ingresa un valor: ")
                    dato_valido = re.search(r"^[0-9]+$",valor)
                    if dato_valido:
                        muestra_jugadores_mayor_que_valor_dado(int(valor),clave,lista_jugadores)
                    else:
                        print("Solo numeros enteros")
                case 19:
                    clave = "temporadas"
                    lista_maximo = calcular_max_min_dato(lista_jugadores,"maximo",clave)
                    lista_jugador = []
                    suma_final = suma(lista_jugadores,clave)
                    mensaje = "La cantidad de temporadas totales es de: {0} siendo ".format(suma_final)
                    for jugador in lista_jugadores:
                        if lista_maximo[0] == jugador["estadisticas"]["temporadas"]:
                            lista_jugador.append(jugador["nombre"])
                    texto = ",".join(lista_jugador)
                    mensaje += texto + " los maximos con {0} temporadas".format(lista_maximo[0])
                    print(mensaje) 
                case 20:
                    clave = "porcentaje_tiros_de_campo"
                    lista_posicion = ["Base","Escolta","Alero","Ala-Pivot","Pivot"]
                    valor = input("Ingresa un valor: ")
                    dato_valido = re.search(r"^[0-9]+$",valor)
                    if dato_valido:
                        muestra_jugador_por_posicion(lista_jugadores,clave,lista_posicion,int(valor))
                    else:
                        print("Solo numeros enteros")
                case 23:
                    lista_titulo = ["Jugador","Puntos","Rebotes","Asistencias","Robos"]
                    crea_ranking_dream_team(lista_jugadores,lista_titulo)

                case 0:
                    break
                case _:
                    print("Opcion no valida,numeros del 0 al 23 sin el 21 o 22")
        else:
            print("Opcion no valida,numeros del 0 al 23 sin el 21 o 22")
        
nba_app(lista_nba)
#Ivan Matias Cantero

