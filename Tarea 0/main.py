import parametros

#Para utilizar los parámetros dentro de este archivo, tendríamos
#que llamarlo de la forma:
total_ships = parametros.NUM_BARCOS
print(total_ships)

from tablero import print_tablero

tablero_enemigo = [['X', ' ', 'X'],[' ', ' ', ' '],['F', ' ', ' ']]
tablero_propio = [['B', ' ', ' '],['B', ' ', ' '],[' ', ' ', 'B']]
print_tablero(tablero_enemigo, tablero_propio)
