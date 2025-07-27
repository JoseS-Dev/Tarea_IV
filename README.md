
# Tarea_IV

Este repositorio contiene la implementación de una herramienta para resolver problemas de Programación Entera Mixta (PEM) utilizando el **Método de Planos de Corte de Gomory**. Este proyecto fue desarrollado como parte de una tarea para la materia de **Métodos Cuantitativos**.

---

## 📚 Descripción del Proyecto

El programa permite al usuario definir interactivamente un problema de Programación Entera Mixta (donde algunas o todas las variables deben tomar valores enteros) y luego intenta encontrar su solución óptima. Utiliza la librería `PuLP` de Python para modelar y resolver las relajaciones lineales del problema, y numpy para manejar los cálculos numéricos. El corazón del proyecto reside en la implementación del algoritmo de **Cortes de Gomory**, que se aplica iterativamente para "cortar" las soluciones fraccionarias hasta alcanzar una solución entera.

### 🎯 Características Principales

* **Definición Interactiva del Problema:** Permite al usuario agregar variables, definir la función objetivo y añadir restricciones directamente desde la consola.
* **Soporte para Variables Enteras y Continuas:** Aunque se enfoca en problemas con componentes enteros, `PuLP` permite definir tipos de variables mixtas.
* **Aplicación de Cortes de Gomory:** Implementa el algoritmo para generar y añadir nuevos cortes que eliminan la región fraccionaria de la solución.
* **Uso de `PuLP`:** Aprovecha esta potente librería para el modelado y la resolución eficiente de las relajaciones lineales del problema.
* **Optimización por Maximización:** El modelo está configurado por defecto para problemas de maximización.

## 🚀 Cómo Empezar

Sigue estos pasos para clonar el repositorio, configurar tu entorno e iniciar el programa.

### 📦 Requisitos

Asegúrate de tener **Python 3.x** instalado en tu sistema. Las librerías necesarias son:
* `PuLP`
* `NumPy`

### 🛠️ Instalación y Configuración

1.  **Clona este repositorio:**
    ```bash
    git clone [https://github.com/JoseS-Dev/Tarea_IV.git](https://github.com/JoseS-Dev/Tarea_IV.git)
    cd Tarea_IV
    ```

2.  **Crea y activa un entorno virtual (altamente recomendado):**
    Un entorno virtual aísla las dependencias de tu proyecto de tu instalación global de Python.

    * **Crear el entorno virtual:**
        ```bash
        python -m venv venv
        ```
    * **Activar el entorno virtual:**
        * **En Windows (Símbolo del Sistema / `cmd`):**
            ```bash
            venv\Scripts\activate
            ```
        * **En Windows (PowerShell):**
            ```powershell
            .\venv\Scripts\Activate.ps1
            ```
        * **En Linux o macOS:**
            ```bash
            source venv/bin/activate
            ```
    Verás `(venv)` al inicio de tu línea de comandos, indicando que el entorno está activo.

3.  **Instala las dependencias:**
    Ya que no hay un `requirements.txt` explícito, instala las librerías manualmente. Puedes crear uno después de la instalación ejecutando `pip freeze > requirements.txt` si lo deseas para futuras referencias.
    ```bash
    pip install pulp numpy
    ```

### 🏃‍♂️ Ejecución del Programa

Con el entorno virtual activado y las dependencias instaladas, ejecuta el programa principal:

```bash
python main.py
````

#### ⌨️ Interacción en la Consola

El programa te presentará un menú interactivo para construir y resolver tu problema de PEM:

```
Bienvenido al programa de Programación Entera Mixta con Corte de Gomory
1. Agregar variable
2. Agregar función objetivo
3. Agregar restricción
4. Resolver problema
5. Salir
Seleccione una opción (1-4):
```

  * **1. Agregar variable:**
      * Te pedirá el `nombre` de la variable.
      * **Nota:** Actualmente, las variables se agregan por defecto como `Integer` (enteras) con `lowBound=0`. Si necesitas variables continuas o binarias, o límites inferiores diferentes, tendrías que modificar el código en `Clase/Corte.py` o extender la interfaz de usuario.
  * **2. Agregar función objetivo:**
      * Deberás ingresar el coeficiente para cada variable que ya hayas agregado.
      * **Nota:** El programa está configurado para **Maximizar**.
  * **3. Agregar restricción:**
      * Para cada variable existente, te pedirá su coeficiente en la restricción.
      * Luego, te pedirá el `límite` (lado derecho) de la restricción.
      * Te pedirá el `nombre` de la restricción.
      * **Importante:** El código actual en `Clase/Corte.py` asume el `sentido` de la restricción ( `<=`, `>=`, `==`). En la interfaz de `main.py` no se pide al usuario este `sentido`. Deberás ajustar `main.py` para solicitar el tipo de comparación o el código asumirá un tipo de restricción específico (la función `agregar_restriccion` en `Corte.py` espera un parámetro `sentido` que `main.py` no proporciona actualmente).
  * **4. Resolver problema:**
      * Esta opción inicia el proceso de resolución. Primero intentará resolver la relajación lineal y luego aplicará cortes de Gomory de forma iterativa si la solución no es entera.
      * **Nota Importante:** La lógica de `agregar_corte` en `main.py` usa una tabla fija (`tableau = np.array([[6, 4, 0, 24], [1, 2, 0, 6], [-1, 1, 0, 1]])`) y no la tabla real del problema definido interactivamente. **Esto significa que los cortes no se están aplicando sobre el modelo PuLP que el usuario define interactivamente, sino sobre una tabla fija de ejemplo.** Esto es el punto más crítico para la funcionalidad del método de planos de corte y requiere una revisión importante. Un enfoque correcto implicaría extraer el tableau simplex del modelo `PuLP` o integrar la lógica de cortes directamente con los objetos `PuLP`.

### ⚠️ Limitaciones y Puntos a Mejorar

  * **Interfaz de usuario para tipo de variables y cotas:** Actualmente, las variables se agregan por defecto como enteras con cota inferior 0. No hay opción para variables continuas, binarias o para especificar cotas superiores desde la interfaz.
  * **Tipo de comparación de restricciones:** La interfaz de usuario en `main.py` no solicita el tipo de comparación (`<=`, `>=`, `=`) para las restricciones. Este es un punto clave que necesita ser corregido para la correcta definición del modelo.
  * **Generación de cortes de Gomory:** La implementación actual de los cortes de Gomory en `main.py` no se integra correctamente con el modelo `PuLP` definido por el usuario, ya que opera sobre una matriz `numpy` fija. Para que el algoritmo funcione como se espera, la lógica de cortes debe interactuar directamente con el estado del problema `PuLP` después de cada relajación.
  * **Visualización:** El proyecto no incluye código de visualización para las soluciones o cortes.
  * **Mensajes de Error:** La validación de la entrada del usuario y el manejo de errores podrían ser más robustos.

### 🤝 Contribuciones

Si deseas contribuir a este proyecto, eres bienvenido a revisar el código, corregir errores, implementar las mejoras sugeridas o añadir nuevas funcionalidades. No dudes en
