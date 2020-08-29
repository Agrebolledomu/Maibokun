import funciones_tarea as ft

rows = input("Ingesa el numero de fila: ")
columns = input("Ingrea el numero de columnas: ")
available_enemy_plays = ft.create_available_plays(rows, columns)
available_own_plays = ft.create_available_plays(rows, columns)
print(available_enemy_plays)
print(available_own_plays)

