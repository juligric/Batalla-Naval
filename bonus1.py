
#todo lo que esta por fuera de lo visto en clase lo obtuve ya que mi papa es progamdor y me ayudo a resolverlo 

import random 
N: int = 10  # Podés cambiar este número a lo que quieras
cantidadDeBarcos = 10
intentos = 15

# Creamos el tablero vacío
tablero = list[list[list]]

# Repetimos N veces para crear N filas
for i in range(N):
    fila: list[int] = []
    for j in range(N):
        fila.append(0)
    tablero.append(fila)

# Dejá que el usuario elija dónde poner los barcos
print("\nJugador 1: Ingresá las posiciones de los barcos")
barcosColocados: int  = 0

while barcosColocados < cantidadDeBarcos:
    try:
        fila: int = int(input(f"Ingresá la FILA del barco {barcosColocados + 1} (0 a {N - 1}): "))
        col: int = int(input(f"Ingresá la COLUMNA del barco {barcosColocados + 1} (0 a {N - 1}): "))

        # Validar si está dentro del tablero
        if fila < 0 or fila >= N or col < 0 or col >= N:
            print("Esa posición está fuera del tablero. Probá de nuevo.")
            continue

        # Validar que no haya ya un barco en esa posición
        if tablero[fila][col] == 1:
            print("Ya colocaste un barco ahí. Elegí otra posición.")
            continue

        tablero[fila][col] = 1
        barcosColocados += 1
        print(f"Barco colocado en ({fila}, {col})\n")

    except ValueError:
        print("Por favor, ingresá un número válido.\n")

print("\nTablero oculto:")
for fila in tablero:
    linea: list[str] = []
    for casillero in fila:
        linea.append("~")  # Muestra todos los casilleros como agua
    print(" ".join(linea))

aciertos: int = 0
fallos: int = 0

while intentos > 0:
    try:
        fila_disparo: int= int(input("\nElegí la FILA (0 a {}): ".format(N - 1)))
        col_disparo: int = int(input("Elegí la COLUMNA (0 a {}): ".format(N - 1)))

        # Validar que las coordenadas sean válidas
        if fila_disparo < 0 or fila_disparo >= N or col_disparo < 0 or col_disparo >= N:
            print("Coordenadas fuera del tablero. Probá de nuevo.\n")
            continue

        # Verificar si acertamos en un barco
        if tablero[fila_disparo][col_disparo] == 1:
            print("¡Acertaste un barco!\n")
            tablero[fila_disparo][col_disparo] = "X"  # Marcamos un barco acertado
            aciertos += 1
        elif tablero[fila_disparo][col_disparo] == "X" or tablero[fila_disparo][col_disparo] == "-":
            print("Ya disparaste ahí. Probá otra posición.\n")
            continue
        else:
            print("Fallaste, no hay barco.\n")
            tablero[fila_disparo][col_disparo] = "-"  # Marcamos un fallo
            fallos += 1

        intentos -= 1
        print(f"Intentos restantes: {intentos}\n")

        # Verificar si ganaste
        if aciertos == cantidadDeBarcos:
            print("¡Ganaste! Encontraste todos los barcos.\n")
            break

    except ValueError:
        print("Por favor, ingresá un número válido.\n")
