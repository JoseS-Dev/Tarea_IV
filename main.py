from Clase.Corte import CorteGomory

# Agregamos la clase main para correr el programa
def main():
    problema = CorteGomory()
    while True:
        print("Bienvenido al programa de Programación Entera Mixta con Corte de Gomory")
        print("1. Agregar variable")
        print("2. Agregar función objetivo")
        print("3. Agregar restricción")
        print("4. Resolver problema")

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
            