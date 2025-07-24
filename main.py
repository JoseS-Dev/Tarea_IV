from Clase.Corte import CorteGomory
import numpy as np
# Agregamos la clase main para correr el programa
def main():
    problema = CorteGomory()
    while True:
        print("Bienvenido al programa de Programación Entera Mixta con Corte de Gomory")
        print("1. Agregar variable")
        print("2. Agregar función objetivo")
        print("3. Agregar restricción")
        print("4. Resolver problema")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            nombre = input("Ingrese el nombre de la variable: ")
            problema.agregar_variables(nombre)
            print(f"Variable '{nombre}' agregada.")
        
        elif opcion == '2':
            coeficientes = {}
            for nombre in problema.vars.keys():
                coef = float(input(f"Ingrese el coeficiente para {nombre}: "))
                coeficientes[nombre] = coef
            problema.agregar_funcion_objetivo(coeficientes)
            print("Función objetivo establecida.")
        
        elif opcion == '3':
            coeficientes = {}
            for nombre in problema.vars.keys():
                coef = float(input(f"Ingrese el coeficiente para {nombre}: "))
                coeficientes[nombre] = coef
            limite = float(input("Ingrese el límite de la restricción: "))
            nombre_restriccion = input("Ingrese el nombre de la restricción: ")
            problema.agregar_restriccion(coeficientes, limite, nombre_restriccion)
            print("Restricción agregada.")
        
        elif opcion == '4':
            problema.resolver()
            # Obtener la tabla simplex (conceptual, usando valores directos)
            tableau = np.array([
                [6, 4, 0, 24],  # Restricción 1
                [1, 2, 0, 6],   # Restricción 2
                [-1, 1, 0, 1]   # Restricción 3
            ])
            # Aplicar el algoritmo de cortes iterativamente
            while True:
                # Agregar un corte de Gomory si se encuentra
                if not problema.agregar_corte(tableau):
                    break
                # Resolver el problema con los nuevos cortes
                problema.resolver()
            # Mostrar la solución final
            print(f"Solución óptima entera: {[f'{nombre} = {var.varValue}' for nombre, var in problema.vars.items()]}")
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.") 

if __name__ == "__main__":
    main()
