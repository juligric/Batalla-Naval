N = 10  # Podés cambiar este número a lo que quieras

# Creamos el tablero vacío
tablero = []

# Repetimos N veces para crear N filas
for i in range(N):
    fila = []  # Creamos una fila vacía
    for j in range(N):  # En cada fila, agregamos N columnas
        fila.append(0)  # Agregamos un 0 como columna vacía (sin barco)
    tablero.append(fila)  # Agregamos la fila completa al tablero

# Mostramos el tablero
for fila in tablero:
    print(fila)