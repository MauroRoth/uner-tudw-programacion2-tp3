from pizza import Pizza
from orden import Orden

class MaestroPizzero:
    # atributos de clase

    # método de inicialización
    def __init__(self, nombre: str):
        # atributos de instancia
        self.__nombre: str = nombre
        self.__ordenes: list[Orden] = list()

    # comandos 
    def establecerNombre(self, nombre: str):
        self.__nombre: str = nombre

    def tomarPedido(self, orden: Orden) -> None:
        self.__ordenes.append(orden)

    def cocinar(self): # REVISAR ESTE METODO, SE DEBE PODER MODIFICAR LAS LISTAS
        for orden in self.__ordenes:
            if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
                orden.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)
                self.__ordenes[self.__ordenes.index(orden)] = orden
                for pizza in orden.obtenerPizzas():
                    pizza.establecerEstado(Pizza.ESTADO_COCINADA)
                    self.__ordenes
                    

    def entregar(self, orden: Orden) -> list[Pizza]:
        pizzas_a_entregar = list()
        for index, pizza in enumerate(orden.obtenerPizzas()):
            if index < 2: 
                pizzas_a_entregar.append(pizza)
                pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)    
            else: break
        contador = 0 
        for pizza in orden.obtenerPizzas():
            if pizza.obtenerEstado == Pizza.ESTADO_ENTREGADA:
                contador += 1
        if contador == len(orden.obtenerPizzas()):
            orden.establecerEstadoOrden(Orden.ESTADO_ENTREGADA)
        return pizzas_a_entregar

    # consultas
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerOrdenes(self):
        return self.__ordenes
    
   