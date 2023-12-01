import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, simplify, parse_expr

def newtonRaphson(funcion, derivada_funcion, x_inicial, iteraciones_max=100, decimales=8):
    """
    Método de Newton-Raphson para encontrar la raíz de una función.

    Parámetros:
    - funcion: La función para la cual encontrar la raíz.
    - derivada_funcion: La derivada de la función.
    - x_inicial: Valor inicial para comenzar la iteración.
    - iteraciones_max: Número máximo de iteraciones permitidas.
    - decimales: Cantidad de decimales para redondear en cada iteración.

    Devuelve:
    - La raíz encontrada.
    """
    print('{:^15s} {:^15s} {:^15s}'.format('x', 'f(x)', 'df(x)'))
    k = 0
    while k < iteraciones_max:
        x_nueva = round(x_inicial - funcion(x_inicial) / derivada_funcion(x_inicial), decimales)
        print('{:15.{decimales}f} {:15.{decimales}f} {:15.{decimales}f}'.format(x_nueva, funcion(x_nueva),
                                                                                    derivada_funcion(x_nueva), decimales=decimales))
        x_inicial = x_nueva
        k += 1
    return x_inicial

def mostrar_menu():
    """
    Muestra el menú de bienvenida para el programa.
    """
    print("Bienvenido al programa de derivación y Newton-Raphson.")
    print("Por favor, ingrese la función en términos de 'x' utilizando la nomenclatura indicada.")
    print("Ejemplos de formato:")
    print("  - x**2 para x al cuadrado")
    print("  - exp(x) para e^x")
    print("  - sin(x) para seno de x")
    print("  - sqrt(x) para raíz cuadrada de x")
    print("  -  También puedes especificar la base, por ejemplo, base el logaritmo_natural_base_e = log(x, 10)")
    print("Ejemplo: exp(x) + sin(x**2) - sqrt(x)")
    print("Ingrese 'salir' para cerrar el programa.")

def main():
    x = symbols('x')

    while True:
        mostrar_menu()

        expresion_str = input("\nIngrese la función: ")

        if expresion_str.lower() == 'salir':
            print("¡Hasta luego!")
            break

        try:
            funcion = parse_expr(expresion_str)
        except:
            print("Error: La expresión ingresada no es válida.")
            continue

        derivada = diff(funcion, x)
        derivada_simplificada = simplify(derivada)

        print(f"\nLa derivada de {funcion} con respecto a x es: {derivada_simplificada}")

        # Modificaciones solicitadas por el usuario
        decimales = int(input("Ingrese la cantidad de decimales para trabajar: "))
        iteraciones_max = int(input("\nIngrese el número total de iteraciones: "))
        x_min = float(input("Ingrese el valor mínimo del intervalo: "))
        x_max = float(input("Ingrese el valor máximo del intervalo: "))
        x_inicial = round(float(input("Ingrese la raíz aproximada inicial: ")), decimales)

        # Llamada al algoritmo de Newton-Raphson con modificaciones
        raiz = newtonRaphson(lambda x: funcion.subs('x', x),
                              lambda x: derivada_simplificada.subs('x', x), x_inicial, iteraciones_max, decimales)
        print(f'\nRaíz encontrada por Newton-Raphson: {raiz}')

        # Gráfico
        x_vals = np.linspace(x_min, x_max, 100)
        y_vals = [funcion.subs('x', val) for val in x_vals]

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='Función')
        ax.scatter(raiz, funcion.subs('x', raiz), color='red', label=f'Raíz: {raiz}')
        ax.set_title('Función y Raíz encontrada por Newton-Raphson')
        ax.legend()
        ax.grid()

        plt.show()
        fig.savefig("newtonraphson.pdf", bbox_inches='tight')

if __name__ == "__main__":
    main()
