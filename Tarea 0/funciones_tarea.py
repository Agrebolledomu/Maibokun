import random

#Creación de Menú de inicio
def start_menu():
    print("-" * 6 + "Menú de Inicio" + "-" *  6)
    print("")
    print("Selecciona una opción\n[0] Iniciar una partida\n[1] Ver Ranking de Puntajes\n[2] Salir")
    print("")
    choice = input("Ingresa tu elección (0, 1 o 2): ")
    valid_options = ["0", "1", "2"]
    while choice not in valid_options:
        print("La opción ingresada no esa válida")
        choice = input("Ingresa tu elección (0, 1 o 2): ")
    return(int(choice))

def from_A0_to_00(coord):
    abc = "ABCDEFGHIJKLMNO"
    indice = abc.find(coord[0])
    if len(coord) == 2:
        coord_num = [str(indice), str(coord[1])]
    elif len(coord) == 3:
        coord_num =[str(indice), str(coord[1]) + str(coord[2])]
    return(coord_num)

def from_00_to_A0(coord_lista):
    abc = "ABCDEFGHIJKLMNO"
    coord_A0 = str(abc[coord_lista[0]]) + str(coord_lista[1])
    return(coord_A0)

#Esta funcion crea y distribuye de forma aleatoria los barcos en un tablero cualquiera
def create_ships(rows, columns, total_ships):
    boxes = []
    abc = "ABCDEFGHIJKLMNO"
    for i in range(int(rows)):
        for j in range(int(columns)):
            boxes.append(str(abc[j]) + str(i))
    
    ships = []
    while len(ships) != total_ships:
        select = random.choice(boxes)
        boxes.remove(select)
        ships.append(select)
    
    return(ships)

#Esta funcion crea una lista con todas las casillas de un tablero
#Se usará para ver cuales son las casillas disponibles cuando el 
#juego comience a avanzar
def create_available_plays(rows, columns):
    boxes = []
    abc = "ABCDEFGHIJKLMNO"
    for i in range(int(rows)):
        for j in range(int(columns)):
            boxes.append(str(abc[j]) + str(i))
    return(boxes)

#Esta funcion toma un strin y corrobora que este sea un número entre 3 y 15
def check_coord(n):
    if (n.isdigit() == False) or (n.isalpha() == True):
        return(False)
    elif (int(n) < 3) or (int(n) > 15):
        return(False)
    else:
        return(True)

#Esta funcion verifica que el nick ingreado cumpla con lo pedido en el enunciado
def check_nickname(nickname):
    long = len(nickname)
    if long < 5:
        its_ok = False
    elif nickname.isalnum() == False:
        its_ok = False
    else:
        its_ok = True
    return(its_ok)

#Esta función muestra los 5 mejores puntajes
def show_ranking():
    print("-" * 6 + "Ranking de puntajes" + "-" *  6)
    print("Nick              Puntaje")
    path = "puntajes.txt"
    with open(path, 'rt') as archivo:
        lineas = archivo.readlines()
    for puntaje in lineas:
        lista_marca = puntaje.split(",")
        for i in lista_marca:
            i = i.strip()       
    #Falta que tome lista marca y ordena de mayor a menor de acuerdo al indice 1 (puntajes)      
        print(f"{lista_marca[0]:18s}{lista_marca[1]:7s}")


#x_bomb: fucnion que recibe una coordena valida y entraga un lista con
#todas las coordenas que afecta la bomba tipo x
def x_bomb(coord_num, radio, rows, columns):
    boxes_revealed = []
    boxes_revealed.append([int(coord_num[0]), int(coord_num[1])])
    col = int(coord_num[0])
    row = int(coord_num[1])
    for i in range(1, radio):
        sup_izq = [int((col - i)), int((row - i))]
        sup_der = [int((col + i)), int((row - i))]
        inf_izq = [int((col - i)), int((row + i))]
        inf_der = [int((col + i)), int((row + i))]
        boxes_revealed.append(sup_izq)
        boxes_revealed.append(sup_der)
        boxes_revealed.append(inf_izq)
        boxes_revealed.append(inf_der)
    
    boxes_revealed_1 = []
    for i in boxes_revealed:
        boxes_revealed_1.append(i)
    
    for i in boxes_revealed:
        if (i[0] < 0) or (i[1] < 0) or (i[0] > int(columns)) or (i[1] > int(rows)):
            boxes_revealed_1.remove(i)
    return(boxes_revealed_1)

def cross_bomb(coord_num, radio, rows, columns):
    boxes_revealed = []
    boxes_revealed.append([int(coord_num[0]), int(coord_num[1])])
    col = int(coord_num[0])
    row = int(coord_num[1])
    for i in range(1, radio):
        nort = [int(col), int(row - i)]
        este = [int(col + i), int(row)]
        sure = [int(col), int(row + i)]
        oest = [int(col - i), int(row)]
        boxes_revealed.append(nort)
        boxes_revealed.append(este)
        boxes_revealed.append(sure)
        boxes_revealed.append(oest)
    
    boxes_revealed_1 = []
    for i in boxes_revealed:
        boxes_revealed_1.append(i)
    
    for i in boxes_revealed:
        if (i[0] < 0) or (i[1] < 0) or (i[0] > int(columns)) or (i[1] > int(rows)):
            boxes_revealed_1.remove(i)
    return(boxes_revealed_1)

def diamond_bomb(coord_num, radio, rows, columns):
    lista = []
    col = coord_num[0]
    row = coord_num[1]
    for i in range(radio): #rep fila
        for j in range(radio - i): # rep columna
            lista.append([col + j, row + i])
            lista.append([col + j, row - i])
            lista.append([col - j, row + i])
            lista.append([col - j, row - i])

    boxes_revealed = []
    for i in lista:
        if i not in boxes_revealed:
            boxes_revealed.append(i)
    boxes_revealed_1 = []
    for i in boxes_revealed:
        boxes_revealed_1.append(i)
    for i in boxes_revealed:
        if (i[0] < 0) or (i[1] < 0) or (i[0] > int(columns)) or (i[1] > int(rows)):
            boxes_revealed_1.remove(i)
    return(boxes_revealed_1)

#check_its_ok: función que verifica que no se haya lanzado una bomba en
#una posicion lanzada anteriormente
def check_its_ok(coord, available_plays):
    #aca estaba el its_ok = True
    for play in available_plays:
        if coord == play:
            return True
        else:
            continue
    return False

#update_board: funcion que toma una coordenada valida y actualiza
#el tablero de acuerdo al tipo de bomba
def update_enemy_board(coord, radio, tablero_visible, tablero_con_barcos, 
tipo_bomba, jugadas_disponibles, rows, columns):
    coord_num = from_A0_to_00(coord)
    ship_found = False
    if tipo_bomba == "regular_bomb":
        for row in range(len(tablero_con_barcos)):
            for col in range(len(tablero_con_barcos[row])):
                if (int(coord_num[0]) == col) and (int(coord_num[1]) == row):
                    if tablero_con_barcos[row][col] == "B":
                        tablero_con_barcos[row][col] = "F"
                        tablero_visible[row][col] = "F"
                        ship_found = True
                    elif tablero_con_barcos[row][col] == " ":
                        tablero_con_barcos[row][col] = "X"
                        tablero_visible[row][col] = "X"
                else:
                    continue
        jugadas_disponibles.remove(coord)   
        return (tablero_visible, jugadas_disponibles, ship_found) 
        #tal vez sea mejor sacar jugads disponibles, y usarla en la corrida del juego    
    
    elif tipo_bomba == "x_bomb":
        damaged_boxes = x_bomb(coord_num, radio, rows, columns)
        for box in damaged_boxes:
            coord_A0 = from_00_to_A0(box)
            for row in range(len(tablero_con_barcos)):
                for col in range(len(tablero_con_barcos[row])):
                    if (box[0] == col) and (box[1] == row):
                        if tablero_con_barcos[row][col] == "B":
                            tablero_con_barcos[row][col] = "F"
                            tablero_visible[row][col] = "F"
                            jugadas_disponibles.remove(coord_A0)
                            ship_found = True
                        elif tablero_con_barcos[row][col] == " ":
                            tablero_con_barcos[row][col] = "X"
                            tablero_visible[row][col] = "X"
                            jugadas_disponibles.remove(coord_A0)
                        else:
                            continue
        return (tablero_visible, jugadas_disponibles) 
    
    elif tipo_bomba == "cross_bomb":
        damaged_boxes = cross_bomb(coord_num, radio, rows, columns)
        for box in damaged_boxes:
            coord_A0 = from_00_to_A0(box)
            for row in range(len(tablero_con_barcos)):
                for col in range(len(tablero_con_barcos[row])):
                    if (box[0] == col) and (box[1] == row):
                        if tablero_con_barcos[row][col] == "B":
                            tablero_con_barcos[row][col] = "F"
                            tablero_visible[row][col] = "F"
                            jugadas_disponibles.remove(coord_A0)
                            ship_found = True
                        elif tablero_con_barcos[row][col] == " ":
                            tablero_con_barcos[row][col] = "X"
                            tablero_visible[row][col] = "X"
                            jugadas_disponibles.remove(coord_A0)
                        else:
                            continue
        return (tablero_visible, jugadas_disponibles) 

    elif tipo_bomba == "diamond_bomb":
        damaged_boxes = diamond_bomb(coord_num, radio, rows, columns)
        for box in damaged_boxes:
            coord_A0 = from_00_to_A0(box)
            for row in range(len(tablero_con_barcos)):
                for col in range(len(tablero_con_barcos[row])):
                    if (box[0] == col) and (box[1] == row):
                        if tablero_con_barcos[row][col] == "B":
                            tablero_con_barcos[row][col] = "F"
                            tablero_visible[row][col] = "F"
                            jugadas_disponibles.remove(coord_A0)
                            ship_found = True
                        elif tablero_con_barcos[row][col] == " ":
                            tablero_con_barcos[row][col] = "X"
                            tablero_visible[row][col] = "X"
                            jugadas_disponibles.remove(coord_A0)
                        else:
                            continue
        return (tablero_visible, jugadas_disponibles) 

def update_own_board(coord, tablero_propio, jugadas_disponibles):
    coord_num = from_A0_to_00(coord)
    ship_found = False
    for row in range(len(tablero_propio)):
        for col in range(len(tablero_propio[row])):
            if (int(coord_num[0]) == col) and (int(coord_num[1]) == row):
                if tablero_propio[row][col] == "B":
                    tablero_propio[row][col] = "F"
                    ship_found = True
                elif tablero_propio[row][col] == " ":
                    tablero_propio[row][col] = "X"
                else:
                    continue
    jugadas_disponibles.remove(coord)
    return(tablero_propio, jugadas_disponibles, ship_found)      

def score_calculation(rows, columns, total_ships, enemigos_descubiertos, aliados_descubiertos):
    final_score = max(0, (rows * columns * total_ships * (enemigos_descubiertos - aliados_descubiertos)))
    return (final_score)          


           


            


                    




##def update_board(coord, tablero):



 