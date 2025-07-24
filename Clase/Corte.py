import pulp
import numpy as np

# Creamos la clase del Porblema de Programación Entera Mixta
class CorteGomory:
    def __init__(self):
        # Creamos el problema de maximización
        self.prob = pulp.LpProblem("Programacion_Entera_Mixta", pulp.LpMaximize)
        self.vars = {}
    
    # Funcion que agregar las variables al problema
    def agregar_variables(self, nombre, LowerBound=0, cat='Integer'):
        self.vars[nombre] = pulp.LpVariable(nombre, lowBound=LowerBound, cat=cat)
    
    # Función que agrega la función objetivo del problema
    def agregar_funcion_objetivo(self, coeficientes):
        self.prob += pulp.lpSum(coeficientes[nombre] * self.vars[nombre] for nombre in self.vars), "Función Objetivo"
    
    # Función que agrega las restricciones al problema
    def agregar_restriccion(self, coeficientes, sentido, valor):
        if sentido == '<=':
            self.prob += pulp.lpSum(coeficientes[nombre] * self.vars[nombre] for nombre in self.vars) <= valor, "Restriccion"
        
        elif sentido == '>=':
            self.prob += pulp.lpSum(coeficientes[nombre] * self.vars[nombre] for nombre in self.vars) >= valor, "Restriccion"
        
        elif sentido == '==':
            self.prob += pulp.lpSum(coeficientes[nombre] * self.vars[nombre] for nombre in self.vars) == valor, "Restriccion"
        
        else:
            return "Sentido de restricción no válido. Use '<=', '>=', o '=='"
    
    # Función para resolver el problema
    def resolver(self):
        self.prob.solve()
        print(f"Estado de la solución: {pulp.LpStatus[self.prob.status]}")
        for nombre in self.vars:
            print(f"{nombre} = {self.vars[nombre].varValue}")
        print(f"Valor óptimo de Z = {self.prob.objective.value()}")
    
    # Función para agregar el corte de Gomory
    def agregar_corte(self,tabla):
        filas, columnas = tabla.shape
        for i in range(filas):
            # Buscamos las fulas fraccionarias (donde el termino independiente no es entero)
            if not np.isclose(tabla[i, -1], np.floor(tabla[i, -1])):
                # Generamos un corte basado en la parte fraccionaria
                corte = np.floor(tabla[i, -1]) + 1 - tabla[i, :-1]
                for j in range(columnas - 1):
                    if not np.isclose(tabla[i, j], 0):
                        corte += (tabla[i, j] - np.floor(tabla[i, j])) * self.vars[list(self.vars.keys())[j]]
                
                # Agregamos el corte como una restricción al problema
                self.prob += corte <= 0, f'Corte_Gomory_{i}'
                print(f"Corte agregado: {corte}")
                return True
        return False
    