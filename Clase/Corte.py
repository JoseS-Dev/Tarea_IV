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
    
    