from maestro_pizzero import MaestroPizzero
from mozo import Mozo
from orden import Orden
from pizza_variedad import PizzaVariedad
from pizza import Pizza
import os

class TesterPizzeria:
    listar_pizzas = lambda p: print(f'\tPizza {p[0]+1} -V: {p[1].obtenerVariedad().obtenerNombreVariedad()} -E:{p[1].obtenerEstado()}')
    
    def clearConsole():
        command = "clear"
        if os.name in ("nt", "dos"): 
            command = "cls"
        os.system(command)

    def main(self):
        TesterPizzeria.clearConsole()
        # 7a. Crear objetos de tipo PizzaVariedad, Pizza, Orden, MaestroPizzero y Mozo.: 
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

        lista_variedades = [variedad1,variedad2,variedad3,variedad4,variedad5,variedad6,variedad7,variedad8]
        print(50*'-')
        print('Variedad de Pizza: Precio')
        list(map(lambda pv: print(f'\t{pv.obtenerNombreVariedad()}: ${pv.obtenerPrecio()}'),lista_variedades))
        
        #   Varios objetos de la clase Pizza
        pizza1 = Pizza(variedad1)
        pizza2 = Pizza(variedad2)
        pizza3 = Pizza(variedad3)
        pizza4 = Pizza(variedad4)
        pizza5 = Pizza(variedad5)
        pizza6 = Pizza(variedad6)
        pizza7 = Pizza(variedad7)
        pizza8 = Pizza(variedad8)
        lista_pizzas = [pizza1,pizza2,pizza3,pizza4,pizza5,pizza6,pizza7,pizza8]      

        print(50*'-')
        print('Pizza Nº -Variedad -Estado')
        l = enumerate(lista_pizzas)
        list(map(TesterPizzeria.listar_pizzas,l))

        #   Varios objetos de la clase Orden
        lista_pizzas1 = [pizza7]
        lista_pizzas2 = [pizza1,pizza2]
        lista_pizzas3 = [pizza2,pizza4,pizza8]
        lista_pizzas4 = [pizza5,pizza6,pizza7,pizza8]

        orden1 = Orden(1,lista_pizzas1)
        orden2 = Orden(2,lista_pizzas2)
        orden3 = Orden(3,lista_pizzas3)
        orden4 = Orden(4,lista_pizzas4)
        lista_ordenes = [orden1,orden2,orden3,orden4]
        
        print(50*'-')
        print('Pizzas por Órdenes')
        for orden in lista_ordenes:
            print(f'Orden Nº: {orden.obtenerNroOrden()}')
            list(map(TesterPizzeria.listar_pizzas,enumerate(orden.obtenerPizzas())))

        # 7b. Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.
        #   Mensaje tomarPedido()
        print(50*'-')
        maestroPizzero1.tomarPedido(orden1)
        maestroPizzero1.tomarPedido(orden2)
        maestroPizzero1.tomarPedido(orden3)
        maestroPizzero1.tomarPedido(orden4)

        print('Mensaje tomar pedido a Maestro Pizzero')
        print('Órdenes tomadas por maestro pizzero:')
        list(map(lambda x: print('Orden Nº ',x.obtenerNroOrden()),maestroPizzero1.obtenerOrdenes()))
        
        # #   Mensaje cocinar()
        print(50*'-')
        print('Mensaje cocinar a Maestro Pizzero')
        print('Estado Orden:',maestroPizzero1.obtenerOrdenes()[0].obtenerEstadoOrden())
        print('Estado Pizza:',pizza1.obtenerEstado())
        maestroPizzero1.cocinar()
        print('Luego de enviar el mensaje cocinar a Maestro Pizzero')
        print('Estado Orden:',maestroPizzero1.obtenerOrdenes()[0].obtenerEstadoOrden())
        print('Estado Pizza:',pizza1.obtenerEstado())

        #   Mensaje entregar()
        print(50*'-')
        print('Mensaje entregar a Maestro Pizzero')
        o = orden4
        print(f'Estado Orden: {o.obtenerEstadoOrden()}')
        list(map(TesterPizzeria.listar_pizzas,enumerate(o.obtenerPizzas())))
        pizzas_entregadas = maestroPizzero1.entregar(o)
        print('Luego de enviar el mensaje')
        print('Pizzas Entregadas')
        list(map(TesterPizzeria.listar_pizzas,enumerate(pizzas_entregadas)))
        print(f'Estado Orden: {o.obtenerEstadoOrden()}')
        list(map(TesterPizzeria.listar_pizzas,enumerate(o.obtenerPizzas())))

        # 7c. Enviar los mensajes tomarPizzas y servirPIzzas a los objetos de la clase Mozo creados en el punto a.
        print(50*'-')
        print('Mensaje tomarPizzas a Mozo\n')
        print(25*'-')
        print('Estados de los mozos antes de enviar el mensaje.')
        print(f'Estado del Mozo {mozo1.obtenerNombre()}: {mozo1.obtenerEstadoLibre()}')
        print(f'Estado del Mozo {mozo2.obtenerNombre()}: {mozo2.obtenerEstadoLibre()}')
        print(25*'-')

        #  Mensaje tomarPizzas()
        print(f'\nMensaje tomarPizzas enviado a {mozo1.obtenerNombre()}')
        mozo1.tomarPizzas(lista_pizzas3)
        
        print(f'\nPizzas tomadas por el Mozo {mozo1.obtenerNombre()}')
        print(f'\nEstado del Mozo {mozo1.obtenerNombre()}: {mozo1.obtenerEstadoLibre()}')

        print(25*'-')
        print(f'\nMensaje tomarPizzas enviado a {mozo2.obtenerNombre()}')
        mozo2.tomarPizzas(lista_pizzas3)

        print(f'\nPizzas tomadas por el Mozo {mozo2.obtenerNombre()}')
        print(f'\nEstado del Mozo {mozo2.obtenerNombre()}: {mozo2.obtenerEstadoLibre()}')
        
        #  Mensaje servirPizzas()
        print(50*'-')
        print('Mensaje servirPizzas a Mozo\n')
        print(25*'-')
        mozo1.servirPizzas()
        print(f'\nPizzas Servidas por el Mozzo {mozo1.obtenerNombre()}!!!')
        list(map(lambda x: print(x.obtenerVariedad()),mozo1.obtenerPizzas())) # comprueba que el mozo no tiene pizzas
        print(f'\nEstado del Mozo {mozo1.obtenerNombre()}: {mozo1.obtenerEstadoLibre()}')
        
        print(25*'-')
        mozo2.servirPizzas()
        print(f'\nPizzas Servidas por el Mozzo {mozo2.obtenerNombre()}!!!')
        list(map(lambda x: print(x.obtenerVariedad()),mozo2.obtenerPizzas())) # comprueba que el mozo no tiene pizzas
        print(f'\nEstado del Mozo {mozo2.obtenerNombre()}: {mozo2.obtenerEstadoLibre()}')
        
        # 7d. Mostrar la transición de estados de los objetos de las clases Orden y Pizza.
        ## Este punto fue realizado en la medida que se enviaban los mensajes en los puntos anteriores.

        # 7e. Calcular y mostrar el costo total de las órdenes creadas.
        print(50*'-')
        print('Costo total de las órdenes creadas.')
        total: float = 0.0
        for orden in lista_ordenes:
            print(f'Orden Nº {orden.obtenerNroOrden()}: ${orden.calcularTotal()}')
            total += orden.calcularTotal()
        print(f'TOTAL: ${total}')

        
if __name__ == '__main__':
    print('PIZZERÍA <<<DON PIPO>>>')
    print(50*'-')
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()