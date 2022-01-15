from datetime import datetime

def execution_time(func):
    # con *args como parámetros permitimos que no importa la cantidad de argumentos nombrados, la función la va a recibir
    # **kwargs logramos decirle que no importa la cantidad de parámetros
    # noombrados que le pasemos a la función (key = value), la función se ejecuta igual
    #  el * es el operador de desestructuración dentro de Python
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper
@execution_time
def random_func():
    # ponemos un _ porque no nos interesa la variable de cada vuelta
    for _ in range (1, 10000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola "+ nombre)

suma(5, 5)
random_func()
saludo("Yael")