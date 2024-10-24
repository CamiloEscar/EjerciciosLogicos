from AbstractFactory import AbstractFactory
from AbstractProductMonitor import AbstractProductMonitor
from AbstractProductMouse import AbstractProductMouse
from AbstractProductTeclado import AbstractProductTeclado

def printProductos(monitor: AbstractProductMonitor, mouse: AbstractProductMouse, teclado: AbstractProductTeclado):
    total = 0.00

    #Monitor
    print(monitor.getNombre())
    print(monitor.getColor())
    print(monitor.getResolucion())
    print(monitor.getCosto())
    print()
    
    #Mouse
    print(mouse.getNombre())
    print(mouse.getColor())
    print(mouse.getDPI())
    print(mouse.getCosto())
    print()
    
    #Teclado
    print(teclado.getNombre())
    print(teclado.getColor())
    print(teclado.getIdioma())
    print(teclado.getPorcentajeTeclas(), "%")
    print(teclado.getCosto())
    print()

    #total
    total = monitor.getCosto() + mouse.getCosto() + teclado.getCosto()
    print("TOTAL: ", total)

def client_code(factory_monitor: AbstractFactory, factory_mouse: AbstractFactory, factory_teclado: AbstractFactory) -> None:
    monitor = factory_monitor.crear_producto_a()
    mouse = factory_mouse.crear_producto_a()
    teclado = factory_teclado.crear_producto_a()

    printProductos(monitor, mouse, teclado)

    

def client_code_2(factory_monitor: AbstractFactory, factory_mouse: AbstractFactory, factory_teclado: AbstractFactory) -> None:
    monitor = factory_monitor.crear_producto_b()
    mouse = factory_mouse.crear_producto_b()
    teclado = factory_teclado.crear_producto_b()

    printProductos(monitor, mouse, teclado)