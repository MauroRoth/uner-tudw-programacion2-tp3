from pizza_variedad import PizzaVariedad

class Pizza:
# atributos de clase
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA =3

    # método de inicialización
    def __init__(self, variedad: PizzaVariedad):
        # atributos de instancia
        self.__variedad: PizzaVariedad = variedad
        self.__estado: int = Pizza.ESTADO_POR_COCINAR

    # comandos
    def establecerVariedad(self, variedad: str):
        self.__variedad = variedad
    
    def establecerEstado(self, estado: int) -> None:
        self.__estado = estado

    # consultas   
    def __repr__(self):
        return self.__variedad
    
    def obtenerVariedad(self) -> PizzaVariedad:
        return self.__variedad
    
    def obtenerEstado(self) -> int:
        return self.__estado