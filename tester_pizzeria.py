from maestro_pizzero import MaestroPizzero
from mozo import Mozo
from orden import Orden
from pizza_variedad import PizzaVariedad
from pizza import Pizza

class TesterPizzeria:
    def main(self):
        # 7a. Crear objetos de tipo: 
        #   Único objeto MaestroPizzero 
        maestroPizzero1 = MaestroPizzero('Anibal')
        print('Maestro Pizzero: ', maestroPizzero1.obtenerNombre())
        #   Dos objetos de la clase mozo.
        mozo1 = Mozo('Alberto')
        mozo2 = Mozo('Luis')
        print('Mozo 1: ', mozo1.obtenerNombre())
        print('Mozo 2: ', mozo2.obtenerNombre())
        #   Varios objetos de la clase PizzaVariedad
        variedad1 = PizzaVariedad('primavera',7000)
        variedad2 = PizzaVariedad('especial',7500)
        variedad3 = PizzaVariedad('fugazeta',8500)
        variedad4 = PizzaVariedad('calabresa',10000)
        variedad5 = PizzaVariedad('humita',6500)
        variedad6 = PizzaVariedad('peperoni',8000)
        variedad7 = PizzaVariedad('margarita',10500)
        variedad8 = PizzaVariedad('cuatro quesos',10000)
        #   Varios objetos de la clase Pizza
        pizza1 = Pizza(variedad1)
        pizza2 = Pizza(variedad2)
        pizza3 = Pizza(variedad3)
        pizza4 = Pizza(variedad4)
        pizza5 = Pizza(variedad1)
        pizza6 = Pizza(variedad2)
        pizza7 = Pizza(variedad3)
        pizza8 = Pizza(variedad4)
        lista_pizzas1 = [pizza1,pizza2]
        lista_pizzas2 = [pizza3,pizza4]
        lista_pizzas3 = [pizza1,pizza3,pizza4]
        lista_pizzas4 = [pizza5,pizza6,pizza7,pizza8]
        print(50*'-')
        for pizza in lista_pizzas4:
            print(pizza.obtenerVariedad().obtenerNombreVariedad())
            print(pizza.obtenerVariedad().obtenerPrecio())
        #   Varios objetos de la clase Orden
        orden1 = Orden(1,lista_pizzas1)
        orden2 = Orden(2,lista_pizzas2)
        orden3 = Orden(3,lista_pizzas3)
        orden4 = Orden(4,lista_pizzas4)
        lista_ordenes = [orden1,orden2,orden3,orden4]
        print(50*'-')
        for orden in lista_ordenes:
            for pizza in orden.obtenerPizzas():
                print(pizza.obtenerVariedad().obtenerNombreVariedad())
                print(pizza.obtenerVariedad().obtenerPrecio())

        # 7b. Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.
        #   Mensaje tomarPedido()
        print(50*'-')
        maestroPizzero1.tomarPedido(orden1)
        maestroPizzero1.tomarPedido(orden2)
        maestroPizzero1.tomarPedido(orden3)
        maestroPizzero1.tomarPedido(orden4)
        print(maestroPizzero1.obtenerOrdenes()[0].obtenerNroOrden())
        #   Mensaje cocinar()
        print(50*'-')
        print(maestroPizzero1.obtenerOrdenes()[0].obtenerEstadoOrden())
        maestroPizzero1.cocinar()
        print(maestroPizzero1.obtenerOrdenes()[0].obtenerEstadoOrden())
        # print('\nLista de Pizzas por Cocinar')
        # list(map(lambda x: print(x.obtenerVariedad()),maestroPizzero1.obtenerPizzasPorCocinar()))

        # # Mensaje cocinar()
        # maestroPizzero1.cocinar()

        # print('\nLista de Pizzas por Entregar')
        # list(map(lambda x: print(x.obtenerVariedad()),maestroPizzero1.obtenerPizzasPorEntregar()))
        
        # # Mensaje entregar()
        # entregadas = maestroPizzero1.entregar()

        # print('\nEntregadas: ')
        # list(map(lambda x: print(x.obtenerVariedad()),entregadas))
        
        # print('\nLista de Pizzas por Entregar')
        # list(map(lambda x: print(x.obtenerVariedad()),maestroPizzero1.obtenerPizzasPorEntregar()))

        # # 5c. Enviar los mensajes tomarPizzas y servirPIzzas a los objetos de la clase Mozo creados en el punto a.
        # print(f'\nEstado del Mozo {mozo1.obtenerNombre()}: {mozo1.isEstadoLibre()}')
        # print(f'\nEstado del Mozo {mozo2.obtenerNombre()}: {mozo2.isEstadoLibre()}')
        
        # pizzas1 = [pizza1,pizza2,pizza3]
        # pizzas2 = [pizza4]

        # # Mensaje tomarPizzas()
        # mozo1.tomarPizzas(pizzas1)
        # print(f'\nPizzas tomadas por el Mozo {mozo1.obtenerNombre()}')
        # list(map(lambda x: print(x.obtenerVariedad()),mozo1.obtenerPizzas()))
        # print(f'\nEstado del Mozo {mozo1.obtenerNombre()}: {mozo1.isEstadoLibre()}')
        
        # mozo2.tomarPizzas(pizzas2)
        # print(f'\nPizzas tomadas por el Mozo {mozo2.obtenerNombre()}')
        # list(map(lambda x: print(x.obtenerVariedad()),mozo2.obtenerPizzas()))
        # print(f'\nEstado del Mozo {mozo2.obtenerNombre()}: {mozo2.isEstadoLibre()}')

        # # Mensaje servirPizzas()
        # mozo1.servirPizzas()
        # print(f'\nPizzas Servidas por el Mozzo {mozo1.obtenerNombre()}!!!')
        # list(map(lambda x: print(x.obtenerVariedad()),mozo1.obtenerPizzas())) # comprueba que el mozo no tiene pizzas
        # print(f'\nEstado del Mozo {mozo1.obtenerNombre()}: {mozo1.isEstadoLibre()}')

        # mozo2.servirPizzas()
        # print(f'\nPizzas Servidas por el Mozzo {mozo2.obtenerNombre()}!!!')
        # list(map(lambda x: print(x.obtenerVariedad()),mozo2.obtenerPizzas())) # comprueba que el mozo no tiene pizzas
        # print(f'\nEstado del Mozo {mozo1.obtenerNombre()}: {mozo1.isEstadoLibre()}')
        
if __name__ == '__main__':
    print('PIZZERÍA <<<DON PIPO>>>')
    print(50*'-')
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()