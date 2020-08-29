import parametros
import random
import sys
import funciones_tarea as ft
from tablero import print_tablero

total_ships = parametros.NUM_BARCOS
blast_radius = parametros.RADIO_EXP

def create_board(rows, columns, total_ships):
    #Esta funcion me entrega dos listas, una para el enemigo
    #y otra propia, ambas con los barcos ya instalados en su
    #tablero respectivo
    tablero_enemigo = []
    tablero_propio = []
    for row in range(int(rows)):
        tablero_enemigo.append([])
        tablero_propio.append([])
        cont = 0 
        while cont != int(columns):
            tablero_enemigo[row].append(" ")
            tablero_propio[row].append(" ")
            cont += 1 
        
    enemy_ships = ft.create_ships(rows, columns, total_ships)
    own_ships = ft.create_ships(rows, columns, total_ships)
    
    #Al comienzo del juego, en el tablero que se muestra en la 
    #consola solo se ven los barcos propios
    for ship in own_ships:
        coord_num = ft.from_A0_to_00(ship) #el primer digito es la columna
        for row in range(len(tablero_propio)):
            for box in range(len(tablero_propio[row])):
                if int(coord_num[0]) == box and int(coord_num[1]) == row:
                    tablero_propio[row][box] = "B"
                else:
                    continue

    tablero_enemigo_2 = tablero_enemigo            
    for ship in enemy_ships:
        coord_num = ft.from_A0_to_00(ship) #el primer digito es la columna
        for row in range(len(tablero_enemigo_2)):
            for box in range(len(tablero_enemigo_2[row])):
                if int(coord_num[0]) == box and int(coord_num[1]) == row:
                    tablero_enemigo_2[row][box] = "B"
                else:
                    continue                
    return(tablero_enemigo, tablero_propio, enemy_ships, own_ships, tablero_enemigo_2)
    

def game_menu(tablero_enemigo, tablero_propio):
    print("-" * 6 + "Menú de Juego" + "-" *  6)
    print_tablero(tablero_enemigo, tablero_propio, utf8 = True)
    print("")
    print("[0] Redirse\n[1] Lanzar una bomba\n[2] Salir del programa")
    print("")
    choice = input("Ingresa tu elección: ")
    valid_options = ["0", "1", "2"]
    while choice not in valid_options:}
        print("La opción ingresada no esa válida")
        choice = input("Ingresa tu elección: ")
    return(int(choice))

#-------------------------Inicio del juego--------------------------
game_finish = False
while game_finish == False: 
    elec = ft.start_menu()
    if elec == 0:
        nick = input("Ingresa tu nickname: ")
        validar = ft.check_nickname(nick)
        while not validar:
            print("\nTu nickname debe tener mínimo 5 caracteres, todos alfanuméricos.\n \n[0] Volver al menú")
            print("[1] Ingresar nickname nuevamente\n")
            elec1 = input("Selecciona una opción: ")
            if int(elec1) == 0:
                elec2 = ft.start_menu()
                #Elegir nick
                if int(elec2) == 0:
                    nick = input("Ingresa tu nickname: ")
                    validar = ft.check_nickname(nick)
                #Ver Ranking de puntajes
                elif int(elec2) == 1:
                    ft.show_ranking()
                    game_finish = True

                #Salir
                elif int(elec2) == 2:
                    sys.exit()
                    game_finish = True

                else:
                    print("Debe ingresar una de las opciones disponibles (0, 1 o 2): ")
                
    
            elif int(elec1) == 1:
                nick = input("Ingresa tu nickname: ")
                validar = ft.check_nickname(nick)
            
            else:
                print("Debe ingresar una de las opciones disponibles (0 o 1): ")
        
        #Se solicita el número de filas y columnas para crear el tablero
        print("Ingrese el número de columnas y fila del tablero")
        rows = str(input("Filas: "))
        while not ft.check_coord(rows):
            print("Debes ingresar un número, en el rango [3,15]. Vuelve a intenarlo")
            rows = str(input("Filas: "))
        columns = str(input("Columnas: "))
        while not ft.check_coord(columns):
            print("Debes ingresar un número, en el rango [3,15]. Vuelve a intenarlo")
            columns = str(input("Columnas: "))
        
        start_board = create_board(int(rows), int(columns), total_ships)

        enemy_visible_board = start_board[0] #tablero del enemigo que se muestra en la terminal
        enemy_ships_board = start_board[4]  #trablero del enemigo que almacena la pos de los baros y no se guarda
        own_board = start_board[1] #tablero propio que se actualiza

        elec3 = game_menu(enemy_visible_board, own_board)
        
        #Se crean dos listas que representan las jugadas válidas para cada jugador
        #De esta forma, cuando una jugada sea válida se sacará de la lista correspondiente
        #para que más tarde esta juganda no esté disponible
        available_enemy_plays = ft.create_available_plays(rows, columns)
        available_own_plays = ft.create_available_plays(rows, columns)

        #La siguiente lista almacena las bombas disponibles
        bomb_list = ["regular_bomb", ["cross_bomb", "x_bomb", "diamond_bomb"]]
        while int(elec3) == 1:    
            if len(bomb_list) == 2: #significa que no se ha usado la bomba especial
                print("Seleccina un tipo de bomba\n")
                print("[0] Bomba Regular\n[1] Bomba especial\n")
                valid_options_0 = ["0", "1"]
                elec4 = input("Ingresa tu elección: ")
                while elec4 not in valid_options_0:
                    print("Ingresa una opción válida (0 o 1): ")
                    elec4 = input("Ingresa tu elección: ")

                if int(elec4) == 0:
                    print("\nSeleccionaste una bomba regular")
                    elec5 = input("Ingresa una coordenada (Formato: A0): ")
                    #Se debe verificar que la coordenada ingresada sea válida
                    #Para lo cual usamos las listas con las jugadas disponibles
                    var = ft.check_its_ok(elec5, available_own_plays)
                    while not var:
                        print("Esta coordenada no cumple el formato, o ya no está disponible")
                        elec5 = input("Ingresa una coordenada (Formato: A0): ")
                        var = ft.check_its_ok(elec5, available_own_plays)
                    print(f"Has disparado a la casilla {elec5}")
                    enemy_visible_board = ft.update_enemy_board(elec5, blast_radius, enemy_visible_board, enemy_ships_board, "regular_bomb", available_own_plays, rows, columns)[0]
                    available_own_plays = ft.update_enemy_board(elec5, blast_radius, enemy_visible_board, enemy_ships_board, "regular_bomb", available_own_plays, rows, columns)[1]
                    barco_encontrado = ft.update_enemy_board(elec5, blast_radius, enemy_visible_board, enemy_ships_board, "regular_bomb", available_own_plays, rows, columns)[2]
                    print_tablero(enemy_visible_board, own_board)
                    if barco_encontrado == True:
                        print("Has encontrado un barco enemigo, juega de nuevo")
                        elec3 = game_menu(enemy_visible_board, own_board)
                    else: 
                        #Ahora juega el enemigo, para esto, hago que de la lists available_enemy_plays se elija un elemento
                        #al azar que representara la jugada del rival
                        jugada_rival = random.choice(available_enemy_plays)
                        own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                        available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                        barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                        print(f"El oponente eligio la casilla {jugada_rival}")
                        print_tablero(enemy_visible_board, own_board)
                        while barco_aliado_encontrado:
                            print("El oponente encontro uno de tus barcos, juega de nuevo")
                            jugada_rival = random.choice(available_enemy_plays)
                            own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                            available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                            barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]

                        elec3 = game_menu(enemy_visible_board, own_board)

                #Seleccion de bomba especial
                elif int(elec4) == 1: 
                    print("\nSeleccionaste una bomba especial\n")
                    print("[0] Bomba X\n[1] Bomba Cruz\n[2] Bomba Diamante\n")
                    valid_options_1 = ["0", "1", "2"]
                    elec5 = input("Selecciona una bomba especial\n")
                    while elec5 not in valid_options_1:
                        print("Opción inválida")
                        elec5 = input("Ingresa una opción válida (0, 1 0 2): ")
                    
                    if int(elec5) == 0:
                        print("Seleccionaste la Bomba X")
                        tipo_bomba = "x_bomb"
                        elec6 = input("Ingresa una coordenada (Formato A0): ")
                        var = ft.check_its_ok(elec6, available_own_plays)
                        while not var:
                            print("Esta coordenada no cumple el formato, o ya no está disponible")
                            elec6 = input("Ingresa una coordenada (Formato: A0): ")
                            var = ft.check_its_ok(elec6, available_own_plays)
                        
                        print(f"Has disparado a la casilla {elec6}")
                        enemy_visible_board = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[0]
                        available_own_plays = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[1]
                        barco_encontrado = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[2]
                        print_tablero(enemy_visible_board, own_board)
                        bomb_list.pop(1)
                        if barco_encontrado == True:
                            print("Has encontrado un barco enemigo, juega de nuevo")
                            elec3 = game_menu(enemy_visible_board, own_board)
                        else: 
                            #Turno oponente
                            jugada_rival = random.choice(available_enemy_plays)
                            own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                            available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                            barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                            print(f"El oponente eligio la casilla {jugada_rival}")
                            while barco_aliado_encontrado:
                                print("El oponente encontro uno de tus barcos, juega de nuevo")
                                jugada_rival = random.choice(available_enemy_plays)
                                own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                                available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                                barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]

                            elec3 = game_menu(enemy_visible_board, own_board)
                        

                    elif int(elec5) == 1:
                        print("Seleccionaste la Bomba Cruz")
                        tipo_bomba = "cross_bomb"
                        elec6 = input("Ingresa una coordenada (Formato A0): ")
                        var = ft.check_its_ok(elec6, available_own_plays)
                        while not var:
                            print("Esta coordenada no cumple el formato, o ya no está disponible")
                            elec6 = input("Ingresa una coordenada (Formato: A0): ")
                            var = ft.check_its_ok(elec6, available_own_plays)
                        print(f"Has disparado a la casilla {elec6}")
                        enemy_visible_board = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[0]
                        available_own_plays = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[1]
                        barco_encontrado = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[2]
                        print_tablero(enemy_visible_board, own_board)
                        bomb_list.pop(1)
                        if barco_encontrado == True:
                            print("Has encontrado un barco enemigo, juega de nuevo")
                            elec3 = game_menu(enemy_visible_board, own_board)
                        #Turno oponente
                        else:
                            jugada_rival = random.choice(available_enemy_plays)
                            own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                            available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                            barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                            print(f"El oponente eligio la casilla {jugada_rival}")
                            while barco_aliado_encontrado:
                                print("El oponente encontro uno de tus barcos, juega de nuevo")
                                jugada_rival = random.choice(available_enemy_plays)
                                own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                                available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                                barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                        
                            elec3 = game_menu(enemy_visible_board, own_board)
                        

                    elif int(elec5) == 2:
                        print("Seleccionaste la Bomba Diamante")
                        tipo_bomba = "diamond_bomb"
                        elec6 = input("Ingresa una coordenada (Formato A0): ")
                        var = ft.check_its_ok(elec6, available_own_plays)
                        while not var:
                            print("Esta coordenada no cumple el formato, o ya no está disponible")
                            elec6 = input("Ingresa una coordenada (Formato: A0): ")
                            var = ft.check_its_ok(elec6, available_own_plays)
                        print(f"Has disparado a la casilla {elec6}")
                        enemy_visible_board = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[0]
                        available_own_plays = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[1]
                        barco_encontrado = ft.update_enemy_board(elec6, blast_radius, enemy_visible_board, enemy_ships_board, tipo_bomba, available_own_plays, rows, columns)[2]
                        print_tablero(enemy_visible_board, own_board)
                        bomb_list.pop(1)
                        if barco_encontrado == True:
                            print("Has encontrado un barco enemigo, juega de nuevo")
                            elec3 = game_menu(enemy_visible_board, own_board)
                        else:
                            #Turno oponente
                            jugada_rival = random.choice(available_enemy_plays)
                            own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                            available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                            barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                            print(f"El oponente eligio la casilla {jugada_rival}")
                            while barco_aliado_encontrado:
                                print("El oponente encontro uno de tus barcos, juega de nuevo")
                                jugada_rival = random.choice(available_enemy_plays)
                                own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                                available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                                barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                        
                            elec3 = game_menu(enemy_visible_board, own_board)

            elif len(bomb_list) == 1:
                print("Solo te quedan bombas regulares")
                elec4 = input("Ingresa una coordenada (Formato: A0): ")
                var = ft.check_its_ok(elec4, available_own_plays)
                while not var:
                    print("Esta coordenada no cumple el formato, o ya no está disponible")
                    elec4 = input("Ingresa una coordenada (Formato: A0): ")
                    var = ft.check_its_ok(elec4, available_own_plays)
                print(f"Has disparado a la casilla {elec5}")
                enemy_visible_board = ft.update_enemy_board(elec5, blast_radius, enemy_visible_board, enemy_ships_board, "regular_bomb", available_own_plays, rows, columns)[0]
                available_own_plays = ft.update_enemy_board(elec5, blast_radius, enemy_visible_board, enemy_ships_board, "regular_bomb", available_own_plays, rows, columns)[1]
                barco_encontrado = ft.update_enemy_board(elec5, blast_radius, enemy_visible_board, enemy_ships_board, "regular_bomb", available_own_plays, rows, columns)[2]
                print_tablero(enemy_visible_board, own_board)
                if barco_encontrado == True:
                    print("Has encontrado un barco enemigo, juega de nuevo")
                    elec3 = game_menu(enemy_visible_board, own_board)
                else:
                #Turno oponente
                    jugada_rival = random.choice(available_enemy_plays)
                    own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                    available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                    barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                    print(f"El oponente eligio la casilla {jugada_rival}")
                    while barco_aliado_encontrado:
                        print("El oponente encontro uno de tus barcos, juega de nuevo")
                        jugada_rival = random.choice(available_enemy_plays)
                        own_board = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[0]
                        available_enemy_plays = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[1]
                        barco_aliado_encontrado = ft.update_own_board(jugada_rival, own_board, available_enemy_plays)[2]
                        
                    elec3 = game_menu(enemy_visible_board, own_board)

        #if elec3 == 0: #rendirse
            #se debe calcular el puntaje y volver al menu principal
                 



                

                        



           

    #Ver Ranking de Puntajes
    elif elec == 1:
        ft.show_ranking()
        game_finish = True

    #Salir de la consola
    elif elec == 2:
        sys.exit()
        game_finish = True     

    #Cualquier otra cosa ingresa que no sea 0, 1 o 2, se indica un error
    else:
        print("Debes ingresar una de las opciones disponibles (0, 1 o 2): ")            





        

        

#tablero_enemigo = [['X', ' ', 'X'],[' ', ' ', ' '],['F', ' ', ' ']]
#tablero_propio = [['B', ' ', ' '],['B', ' ', ' '],[' ', ' ', 'B']]
#print_tablero(tablero_enemigo, tablero_propio)
