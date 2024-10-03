class PizzaVariedad:
    # atributos de clase

    # método de inicialización
    def __init__(self,nombreVariedad,precio) -> None:
        # atributos de instancia
        self.__nombreVariedad: str = nombreVariedad
        self.__precio: float = precio
       
    # comandos
    def establecerNombreVariedad(self,nombreVariedad) -> None:
        self.__nombreVariedad = nombreVariedad

    def establecerPrecio(self,precio) -> None:
        self.__precio = precio
    
    # consultas
    def obtenerNombreVariedad(self) -> str:
        return self.__nombreVariedad
    
    def obtenerPrecio(self) -> float:
        return self.__precio
