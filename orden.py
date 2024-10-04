from pizza import Pizza

class Orden:
    # atributos de clase
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3

    # método de inicialización
    def __init__(self, nroOrden: int, pizzas: list[Pizza]) -> None:
        # atributos de instancia
        self.__nroOrden: int = nroOrden
        self.__pizzas: list[Pizza] = pizzas
        self.__estadoOrden: int = Orden.ESTADO_INICIAL
    
    # comandos
    def establecerNroOrden(self,nroOrden) -> None:
        self.__nroOrden = nroOrden
    
    def establecerPizzas(self,pizzas: Pizza) -> None:
        self.__pizzas = pizzas

    def establecerEstadoOrden(self,estadoOrden: int) -> None:
        self.__estadoOrden = estadoOrden

    # consultas
    def obtenerNroOrden(self) -> int:
        return self.__nroOrden
    
    def obtenerPizzas(self) -> list[Pizza]:
        return self.__pizzas
    
    def obtenerEstadoOrden(self) -> int:
        return self.__estadoOrden
    
    def calcularTotal(self) -> float:
        total: float = 0.0      
        for pizza in self.__pizzas:
            total += pizza.obtenerVariedad().obtenerPrecio()
        return total
        

        