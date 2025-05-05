def crear_tablero(N: int):
    return [[0 for _ in range(N)] for _ in range(N)] #crea el tablero"

def mostrar_tablero_oculto(tablero:list[list[list]]): #se fija si acrtemos o no y si  ya disparmos
    for fila in tablero:
        linea = []
        for casillero in fila:
            if casillero == "X":
                linea.append("X") #barco acertado
            elif casillero == "-":
                linea.append("-") #tiro fallido
            else:
                linea.append("~") #agua
        print(" ".join(linea))

def colocar_barcos(tablero: List[List[int]], jugador: str, cantidad: int, N: in):
    print(f"\n{jugador}, ingresá las posiciones de tus barcos") 
    colocados = 0
    while colocados < cantidad: #si barco es menor a la cnatdiad de abrcos podemos seguir agregando, ademas aca hace la veriiacion para que se pueedan ubiar de manera correcta los abrcos 
        try:
            fila = int(input(f"Ingresá la FILA del barco {colocados + 1} (0 a {N - 1}): "))
            col = int(input(f"Ingresá la COLUMNA del barco {colocados + 1} (0 a {N - 1}): "))
            if fila < 0 or fila >= N or col < 0 or col >= N:
                print("Esa posición está fuera del tablero. Probá de nuevo.")
                continue
            if tablero[fila][col] == 1:
                print("Ya colocaste un barco ahí. Elegí otro lugar")
                continue
            tablero[fila][col] = 1
            colocados += 1
            print(f"Barco colocado en ({fila}, {col})\n")
        except ValueError:
            print("Por favor, ingresá un número válido.\n")

def turno_disparo(jugador: str, tablero_enemigo: List[List[int]], aciertos: int, cantidad_barcos: int, N: int) -> Tuple[int, bool]: #represnta el turno de cada jugador para dispara por turno y que sea alterando
    try:
        print(f"\n{jugador}, es tu turno de disparar.")
        fila = int(input(f"Elegí la FILA (0 a {N - 1}): "))
        col = int(input(f"Elegí la COLUMNA (0 a {N - 1}): "))

        if fila < 0 or fila >= N or col < 0 or col >= N:   #chque si los parametros son correctos y si no vuelve a la funcioon de acieto y le da el valor de false 
            print("Coordenadas fuera del tablero. Probá de nuevo.")
            return aciertos, False

        if tablero_enemigo[fila][col] == 1: #se fija si ahi hay o no un barco 
            print("Acertaste un barco")
            tablero_enemigo[fila][col] = "X"
            aciertos += 1
        elif tablero_enemigo[fila][col] == "X" or tablero_enemigo[fila][col] == "-":
            print("Ya disparaste ahí perdiste el turno.")
        else:
            print("Fallaste, no hay barco.")
            tablero_enemigo[fila][col] = "-"

        if aciertos == cantidad_barcos:
            print(f"\n{jugador} undiste todos los barcos del enemigo ¡Ganaste!")
            return aciertos, True

    except ValueError:
        print("Por favor, ingresá un número válido.")

    return aciertos, False


#incia el juego
N: int= 10
cantidadDeBarcos: int = 5

tablero_j1: List[List[int]] crear_tablero(N)
tablero_j2: List[List[int]] crear_tablero(N)

colocar_barcos(tablero_j1, "Jugador 1", cantidadDeBarcos)
print("\n" + "-" * 40)
colocar_barcos(tablero_j2, "Jugador 2", cantidadDeBarcos)

aciertos_j1: int = 0
aciertos_j2: int = 0

turno: int = 1  # 1 para jugador 1, 2 para jugador 2

while True:
    print("\n" + "=" * 40)
    if turno == 1:
        print("Tablero enemigo (Jugador 2):")
        mostrar_tablero_oculto(tablero_j2)
        aciertos_j1, gano = turno_disparo("Jugador 1", tablero_j2, aciertos_j1, cantidadDeBarcos)
        if gano:
            break
        turno = 2
    else:
        print("Tablero enemigo (Jugador 1):")
        mostrar_tablero_oculto(tablero_j1)
        aciertos_j2, gano = turno_disparo("Jugador 2", tablero_j1, aciertos_j2, cantidadDeBarcos)
        if gano:
            break
        turno = 1
