from colorama import init, Fore

init(autoreset=True)

def crearTabla(n):
    tabla =[]
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(set())
        tabla.append(fila)
    return tabla

def imprimirTabla(tabla):
    for fila in tabla:
        fila_vacia = []
        for conjunto in fila:
            if conjunto:
                fila_vacia.append(conjunto)
            else:
                fila_vacia.append("vacio")
        print(fila_vacia)

def algoritmoCYK(gramatica, inicial, Cadena):
    n = len(Cadena)
    tabla = crearTabla(n)
    
    # Llenar la primera columna con las variables
    for i in range(n):
        for simbolo, produccion in gramatica.items():
            if Cadena[i] in produccion:
                tabla[i][0].add(simbolo)

    # primera columna de la tabla
    print(Fore.LIGHTYELLOW_EX + "Tabla (primera columna):")
    # for i in range(n):
    #     print(tabla[i][0])
    imprimirTabla(tabla)

    # Llenar el resto de la tabla
    for i in range(2, n + 1):
        for j in range(n - i + 1):
            for k in range(1, i):
                for izquierda in tabla[j][k - 1]:
                    for derecha in tabla[j + k][i - k - 1]:
                        # Genera la subcadena
                        for simbolo, produccion in gramatica.items():
                            if izquierda + derecha in produccion:
                                tabla[j][i - 1].add(simbolo)

    # Verificar si el símbolo inicial está en la celda [0, n-1]
    if inicial in tabla[0][n - 1]:
        print(Fore.GREEN + "Tabla Final")
        imprimirTabla(tabla)
        print(Fore.CYAN + "\nLa cadena es aceptada por la gramática.\n")
    else:
        print(Fore.GREEN + "Tabla Final")
        imprimirTabla(tabla)
        print(Fore.RED + "\nLa cadena es rechazada por la gramática.\n")
        

def main():
    gramaticas = [
        {
            'A': {'BC', 'AB', '1'},
            'B': {'AA', '0'},
            'C': {'CB', '1', '0'}
        },{
            'S': {'XY'},
            'X': {'SY', 'ZZ', '0'},
            'Y': {'XX'},
            'Z': {'1'}
        },{
            'S': {'AB'},
            'A': {'BB', 'a'},
            'B': {'AB', 'b'}
        }
    ]

    cadenas = ['110100', '00111', 'aabbb']
    iniciales = ['A', 'S', 'S']

    # empaquetamos las gramaticas, el simbolo inicial y las cadenas
    # para que no se ejecute 9 veces
    for gramatica, inicial, cadena in zip(gramaticas, iniciales, cadenas):
        print(f"Validando cadena '{cadena}' con la gramática: {gramatica}")
        algoritmoCYK(gramatica, inicial, cadena)
        print()

if __name__ == '__main__':
    main()
