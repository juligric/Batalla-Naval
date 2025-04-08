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








# Mostramos el tablero
for fila in tablero:
    print(fila)