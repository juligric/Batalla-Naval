
#todo lo que esta por fuera de lo visto en clase lo obtuve ya que mi papa es progamdor y me ayudo a resolverlo 
#todos los bonus estan en el link del repo 

import random 
N = 10  # Podés cambiar este número a lo que quieras
cantidadDeBarcos = 10
intentos = 15

# Creamos el tablero vacío
tablero = []

# Repetimos N veces para crear N filas
for i in range(N):
    fila = []
    for j in range(N):
        fila.append(0)
    tablero.append(fila)

# Colocamos barcos al azar
barcosColocados = 0
while barcosColocados < cantidadDeBarcos:
    fila = random.randint(0, N - 1)
    col = random.randint(0, N - 1)
    if tablero[fila][col] == 0:
        tablero[fila][col] = 1  # Poner un barco
        barcosColocados += 1  # ¡Sumar uno al contador!






print("\nTablero oculto:")
for fila in tablero:
    linea = []
    for casillero in fila:
        linea.append("~")  # Muestra todos los casilleros como agua
    print(" ".join(linea))



aciertos = 0
fallos = 0

while intentos > 0:
    try:
        fila_disparo = int(input("\nElegí la FILA (0 a {}): ".format(N - 1)))
        col_disparo = int(input("Elegí la COLUMNA (0 a {}): ".format(N - 1)))

        # Validar que las coordenadas sean válidas
        if fila_disparo < 0 or fila_disparo >= N or col_disparo < 0 or col_disparo >= N:
            print(" Coordenadas fuera del tablero. Probá de nuevo.\n")
            continue

        # Verificar si acertamos en un barco
        if tablero[fila_disparo][col_disparo] == 1:
            print(" ¡Acertaste un barco!\n")
            tablero[fila_disparo][col_disparo] = "X"  # Marcamos un barco acertado
            aciertos += 1
        elif tablero[fila_disparo][col_disparo] == "X" or tablero[fila_disparo][col_disparo] == "-":
            print(" Ya disparaste ahí. Probá otra posición.\n")
            continue
        else:
            print(" Fallaste, no hay barco.\n")
            tablero[fila_disparo][col_disparo] = "-"  # Marcamos un fallo
            fallos += 1

        intentos -= 1
        print(f" Intentos restantes: {intentos}\n")

        # Verificar si ganaste
        if aciertos == cantidadDeBarcos:
            print(" ¡Ganaste! Encontraste todos los barcos.\n")
            break

    except ValueError:
        print(" Por favor, ingresá un número válido.\n")
