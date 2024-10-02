class Pizza:

    def __init__(self, var: str):
        self.__variedad = var

    def establecerVariedad(self, var: str):
        self.__variedad = var

    def obtenerVariedad(self):
        return self.__variedad
    
    def __repr__(self):
        return self.__variedad