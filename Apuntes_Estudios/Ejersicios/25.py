"""Tres en Raya (Tic Tac Toe) 
 Requisitos Tablero: X | O | X --------- O | X | O --------- X | | O 
   Debes hacer turnos validar posiciones detectar ganador empate evitar sobrescribir casillas 
     Practicas matrices/listas lógica compleja estados validaciones"""

def juego():

    jugador_x = 0
    jugador_o = 0
    empates = 0

    while True:

        print("\n\t===== TRES EN RAYA =====\n")

        tablero = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        jugador = "X"

        while True:

            # MOSTRAR TABLERO
            print()

            for fila in tablero:
                print(f" {fila[0]} | {fila[1]} | {fila[2]}")
                print("-----------")

            print()

            # PEDIR DATOS
            try:
                fila = int(input(f"Jugador {jugador} - Fila (0-2): "))
                columna = int(input(f"Jugador {jugador} - Columna (0-2): "))

            except ValueError:
                print("Error: ingrese números válidos")
                continue

            # VALIDAR RANGO
            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print("Posición inválida")
                continue

            # VALIDAR CASILLA
            if tablero[fila][columna] != " ":
                print("Casilla ocupada")
                continue

            # COLOCAR FICHA
            tablero[fila][columna] = jugador

            # ===== VALIDAR GANADOR =====

            ganador = False

            # FILAS
            if tablero[0][0] == tablero[0][1] == tablero[0][2] != " ":
                ganador = True

            elif tablero[1][0] == tablero[1][1] == tablero[1][2] != " ":
                ganador = True

            elif tablero[2][0] == tablero[2][1] == tablero[2][2] != " ":
                ganador = True

            # COLUMNAS
            elif tablero[0][0] == tablero[1][0] == tablero[2][0] != " ":
                ganador = True

            elif tablero[0][1] == tablero[1][1] == tablero[2][1] != " ":
                ganador = True

            elif tablero[0][2] == tablero[1][2] == tablero[2][2] != " ":
                ganador = True

            # DIAGONALES
            elif tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
                ganador = True

            elif tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
                ganador = True

            # SI HAY GANADOR
            if ganador:

                print()

                for fila_tablero in tablero:
                    print(f" {fila_tablero[0]} | {fila_tablero[1]} | {fila_tablero[2]}")
                    print("-----------")

                print(f"\n Gano el jugador {jugador}")

                if jugador == "X":
                    jugador_x += 1
                else:
                    jugador_o += 1

                break

            # ===== VALIDAR EMPATE =====

            empate = True

            for fila_tablero in tablero:
                if " " in fila_tablero:
                    empate = False

            if empate:

                print()

                for fila_tablero in tablero:
                    print(f" {fila_tablero[0]} | {fila_tablero[1]} | {fila_tablero[2]}")
                    print("-----------")

                print("\n Empate")
                empates += 1
                break

            # CAMBIAR TURNO
            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"

        # ===== PUNTUACIONES =====

        print("\n===== MARCADOR =====")
        print(f"Jugador X: {jugador_x}")
        print(f"Jugador O: {jugador_o}")
        print(f"Empates: {empates}")

        # REPETIR
        repetir = input("\n¿Jugar otra vez? (si/no): ").lower()

        if repetir != "si":
            print("Saliendo del juego...")
            break


juego()