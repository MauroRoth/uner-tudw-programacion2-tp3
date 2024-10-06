from pizza import Pizza

class Mozo:
    # atributos de clase

    # método de inicialización
    def __init__(self, nombre: str):
        # atributos de instancia
        self.__nombre: str = nombre
        self.__pizzas: list[Pizza] = []

    # comandos
    def establecerNombre(self, nombre: str):
        self.__nombre = nombre

    def tomarPizzas(self, pizzas: list[Pizza]):
        pizzasTomadas = len(self.__pizzas)
        pizzasATomar = len(pizzas)
        if (pizzasATomar - pizzasTomadas) < 0:
            print(self.__nombre + ": El mozo puede tomar un máximo de 2 pizzas!")
        else:
            for pizza in pizzas:
                print(self.__nombre + ": tomando una de " + pizza.obtenerVariedad().obtenerNombreVariedad() + " para ser entregada")
                self.__pizzas.append(pizza)
    
    def servirPizzas(self):
        for pizza in self.__pizzas:
            print(self.__nombre + ": Sirviendo pizza de " + pizza.obtenerVariedad().obtenerNombreVariedad())
        self.__pizzas = []

    # consultas
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerPizzas(self):
        return self.__pizzas
    
    def obtenerEstadoLibre(self):
        return len(self.__pizzas) == 0