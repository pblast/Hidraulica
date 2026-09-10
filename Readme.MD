PROGRAMA PARA EL CÁLCULO DE CIRCUITOS HIDRAULICOS

* main.py:
Crea las variables que definene el problema (tubería, fluido, bombas) y llama a las funciones para realizar los calculos
y hacer las gráficas

* Bombas.py
Crea las curvas de las bombas y define la clase de la bomba en la que se almacenan el modelo y tres puntos de caudal, presión y eficiencia

* Circuito.py
Hace todos los cálculos de perdidas de carga y genera las curvas de perdidas en función del caudal, los elementos que forman el circuito
y el fluido


NOTAS:
Una vez descargados los archivos hay que crear el entorno mediante el comando

    python3 -m venv venv

Hay que instalar los siguientes paquetes
    numpy
    matplotlib

Antes de ejecutar nada hay que activar el entorno virtual
      source venv/bin/activate