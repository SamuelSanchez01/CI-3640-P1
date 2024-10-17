#include <iostream>
#include <cmath>
#include <cassert>

class Quaternion {
    /*
    Class for quaternions with overloaded operators
    */
    public:
    double a, b, c, d;

    //Constructor
    Quaternion(double a, double b, double c, double d) : a(a), b(b), c(c), d(d) {}

    //Sum of 2 quat
    Quaternion operator+(const Quaternion& quat) const {
        return Quaternion(a + quat.a, b + quat.b, c + quat.c, d + quat.d);
    }

    /*
    Function to overload the * operator
    @param q: Quaternion object
    @return: Quaternion object
    */
    Quaternion operator*(const Quaternion& q) const {
        return Quaternion(
            a * q.a - b * q.b - c * q.c - d * q.d,
            a * q.b + b * q.a + c * q.d - d * q.c,
            a * q.c - b * q.d + c * q.a + d * q.b,
            a * q.d + b * q.c - c * q.b + d * q.a
        );
    }

    //Combine
    Quaternion operator~() const {
        return Quaternion(a, -b, -c, -d);
    }

    //Abs
    double operator&() const {
        return std::sqrt(a * a + b * b + c * c + d * d);
    }

    //Sum with scalar
    Quaternion operator+(double scalar) const {
        return Quaternion(a + scalar, b, c, d);
    }

    //Mult with scalar
    Quaternion operator*(double scalar) const {
        return Quaternion(a * scalar, b * scalar, c * scalar, d * scalar);
    }

    // Printer
    operator const char*() const {
        static char str[100];
        sprintf(str, "%f + %fi + %fj + %fk", a, b, c, d);
        return str;
    }
};

int main() {
    Quaternion q1(1, 2, 3, 4);
    Quaternion q2(5, 6, 7, 8);

    std::cout << "impresion de 1: " << q1 << std::endl;
    std::cout << "impresion de 2: " << q2 << std::endl;

    std::cout << "suma: " << q1 + q2 << std::endl;
    std::cout << "conjugada 1: " << ~q1 << std::endl;
    std::cout << "multiplicacion: " << q1 * q2 << std::endl;
    std::cout << "probando el and: " << &q1 << std::endl;

    std::cout << "suma escalar: " << q1 + 3 << std::endl;
    std::cout << "multiplicacion escalar: " << q1 * 3.0 << std::endl;

    return 0;
}