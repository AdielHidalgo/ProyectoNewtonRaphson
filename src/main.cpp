

#include <iostream>
#include <cmath>

double func(double x) {
  return std::pow(x, 3) + std::sqrt(x) - 6;
}

double deriv(double x) {
    return 3 * std::pow(x, 2) - 0.5 / std::sqrt(x);
}

double newtonRaphson(double x0, double tolerancia, int iteracionmax, double fixed_value, int tolerancia_decimales) {
    double x = x0;
    int iteracion = 0;

    while (iteracion < iteracionmax) {
        double f_x = func(x);
        double f_prime_x = deriv(x);
        double x_next = x - f_x / f_prime_x;

        // Redondear el resultado al número de decimales especificado
        double x_next_rounded = std::round(x_next * std::pow(10, tolerancia_decimales)) / std::pow(10, tolerancia_decimales);
        double fixed_value_rounded = std::round(fixed_value * std::pow(10, tolerancia_decimales)) / std::pow(10, tolerancia_decimales);

        if (std::abs(x_next - x) < tolerancia || x_next_rounded == fixed_value_rounded) {
            return x_next_rounded;
        }

        x = x_next;
        iteracion++;
    }

    throw std::runtime_error("El método de Newton-Raphson no convergió después de " + std::to_string(iteracionmax) + " iteraciones.");
}

int main() {
    double x0, tolerancia, fixed_value;
    int iteracionmax, tolerancia_decimales;
    
    std::cout << "Ingrese la aproximación inicial: ";
    std::cin >> x0;

    std::cout << "Ingrese la tolerancia: ";
    std::cin >> tolerancia;

    std::cout << "Ingrese el número de iteraciones deseadas: ";
    std::cin >> iteracionmax;

    std::cout << "¿Desea fijar un valor? (y/n): ";
    char use_fixed_value;
    std::cin >> use_fixed_value;

    if (use_fixed_value == 'y') {
        std::cout << "Ingrese el valor fijo deseado: ";
        std::cin >> fixed_value;

        std::cout << "Ingrese la cantidad de decimales para redondear: ";
        std::cin >> tolerancia_decimales;
    } else {
        fixed_value = 0;  // Puedes ajustar este valor si no hay un valor fijo específico
        tolerancia_decimales = 6;  // Puedes ajustar este valor según tus necesidades
    }

    // Llama a la función de Newton-Raphson
    double root = newtonRaphson(x0, tolerancia, iteracionmax, fixed_value, tolerancia_decimales);
    std::cout << "La raíz encontrada es: " << root << std::endl;

    return 0;
}
