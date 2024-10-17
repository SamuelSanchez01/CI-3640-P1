# Lenguaje Swift

## Descripción

Swift es un lenguaje de programación de propósito general, multi-paradigma y compilado, creado por Apple en 2014. Está diseñado para ser seguro, rápido y expresivo, y se utiliza principalmente para el desarrollo de aplicaciones para productos Apple


## Alcances y asociaciones

Swift utiliza un alcance estático y asociación superficial por defecto (puede usarse profunda pero no es el comportamiento general).

Ventajas:

Disminución de errores por verificacion de tipos.
Rendimiento, la compilación a código máquina optimiza la ejecución.

Desventajas:

Curva de aprendizaje alta
Al estar orientado 100% en apple pueden haber bugs en otros sistemas que tarden en arreglarse


## Módulos y gestión de nombres

Swift organiza el código en módulos. Los módulos pueden ser importados utilizando la palabra import. Por ejemplo:

` import Foundation `

Y se exporta sin necesidad de declarar el "export"

## Alias, sobrecarga y polimorfismo

Con la palabra clave typealias podemos crear alias de tipos.

Swift también soporta la sobrecarga de funciones y el polimorfismo a través de protocolos y herencia.

## El compilador y otras herramientas

Compilador: El compilador de Swift está integrado en Xcode y se puede consultar su documentación [Aquí](https://www.swift.org/documentation/swift-compiler/).
Depurador: LLDB es el depurador utilizado con Swift.
Frameworks: Swift se integra con frameworks SwiftUI y Foundation.
Gestión de dependencias: Swift Package Manager (SPM) facilita la gestión de dependencias y la distribución de paquetes.
Documentación: Swift provee la documentación oficial en [swift.org](https://www.swift.org/documentation/) proporcionan una buena documentación