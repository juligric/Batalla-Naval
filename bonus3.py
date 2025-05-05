
#todo lo que esta por fuera de lo visto en clase lo obtuve ya que mi papa es progamdor y me ayudo a resolverlo 


def crear_tablero(N: int)
    return [[0 for _ in range(N)] for _ in range(N)]  # Crea el tablero

def mostrar_tablero_oculto(tablero: List[List[int]]):  # Muestra los barcos, marcando los aciertos y fallos
    for fila in tablero:
        linea = []
        for casillero in fila:
            if casillero == "X":
                linea.append("X")  # Acertaste un barco
            elif casillero == "-":
                linea.append("-")  # Fallaste en el disparo
            else:
                linea.append("~")  # Casilla vacía sin disparar
        print(" ".join(linea))

def contar_casillas_ocupadas(tablero):  # Cuenta cuántas casillas están ocupadas por barcos
    total:  int = 0
    for fila in tablero:
        total += fila.count(1)  # Cuenta los barcos en el tablero
    return total

def colocar_barcos(tablero: List[List[int]], jugador: str, cantidad_barcos: int, tamano_maximo_barco: int = 3):
    print(f"\n{jugador}, ingresá las posiciones de tus barcos (hasta {tamano_maximo_barco} casillas)")
    colocados: int = 0
    while colocados < cantidad_barcos:
        try:
            fila: int = int(input(f"Ingresá la FILA del barco {colocados + 1} (0 a {N - 1}): "))
            col: int = int(input(f"Ingresá la COLUMNA del barco {colocados + 1} (0 a {N - 1}): "))
            tamaño: int = int(input(f"Ingresá el tamaño del barco (1 a {tamaño_maximo_barco}): "))
            if tamaño < 1 or tamano > tamaño_maximo_barco:
                print(f"El tamaño del barco debe ser entre 1 y {tamaño_maximo_barco}.")
                continue
            
            if fila < 0 or fila >= N or col < 0 or col >= N:
                print("Esa posición está fuera del tablero. Probá de nuevo.")
                continue
            
            if any(tablero[fila][col + i] == 1 for i in range(tamano) if col + i < N):  # Verifica si hay espacio y si ya hay barco
                for i in range(tamano):
                    tablero[fila][col + i] = 1
                colocados += 1
                print(f"Barco de tamaño {tamano} colocado en ({fila}, {col})\n")
            else:
                print("No hay espacio para colocar el barco allí. Probá otra posición.")
        except ValueError:
            print("Por favor, ingresá un número válido.\n")

def turno_disparo(jugador: str, tablero_enemigo:  List[List[int]], aciertos: int, cantidad_casillas: int    ):
    try:
        print(f"\n{jugador}, es tu turno de disparar.")
        fila: int = int(input(f"Elegí la FILA (0 a {N - 1}): "))
        col: int = int(input(f"Elegí la COLUMNA (0 a {N - 1}): "))

        if fila < 0 or fila >= N or col < 0 or col >= N:
            print("Coordenadas fuera del tablero. Probá de nuevo.")
            return aciertos, False

        if tablero_enemigo[fila][col] == 1:  # Si hay un barco en esa posición
            print("Acertaste un barco")
            tablero_enemigo[fila][col] = "X"  # Marca el barco como hundido
            aciertos += 1
        elif tablero_enemigo[fila][col] == "X" or tablero_enemigo[fila][col] == "-":
            print("Ya disparaste ahí perdiste el turno.")
        else:
            print("Fallaste, no hay barco.")
            tablero_enemigo[fila][col] = "-"  # Marca el fallo

        if aciertos == cantidad_casillas:
            print(f"\n{jugador} hundió todos los barcos enemigos ¡Ganaste!")
            return aciertos, True

    except ValueError:
        print("Por favor, ingresá un número válido.")

    return aciertos, False


# --- INICIO DEL JUEGO ---
N = 10
cantidadDeBarcos: int = 5

tablero_j1: list[list[list]] = crear_tablero(N)
tablero_j2:list[list[list]] = crear_tablero(N)

colocar_barcos(tablero_j1, "Jugador 1", cantidadDeBarcos)
print("\n" + "-" * 40)
colocar_barcos(tablero_j2, "Jugador 2", cantidadDeBarcos)

total_casillas_j1: int= contar_casillas_ocupadas(tablero_j1)
total_casillas_j2: int = contar_casillas_ocupadas(tablero_j2)

aciertos_j1: int = 0
aciertos_j2: int = 0

turno: int = 1  # 1 para jugador 1, 2 para jugador 2

while True:
    print("\n" + "=" * 40)
    if turno == 1:
        print("Tablero enemigo (Jugador 2):")
        mostrar_tablero_oculto(tablero_j2)
        aciertos_j1, gano = turno_disparo("Jugador 1", tablero_j2, aciertos_j1, total_casillas_j2)
        if gano:
            break
        turno = 2
    else:
        print("Tablero enemigo (Jugador 1):")
        mostrar_tablero_oculto(tablero_j1)
        aciertos_j2, gano = turno_disparo("Jugador 2", tablero_j1, aciertos_j2, total_casillas_j1)
        if gano:
            break
        turno = 1
