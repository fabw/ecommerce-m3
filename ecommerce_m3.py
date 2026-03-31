def mostrar_menu():
    print("\nBienvenido/a tu Ecommerce")
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")

def mostrar_catalogo(catalogo):
    for producto in catalogo:
        print(f'ID: {producto["id"]} | Nombre: {producto["nombre"]} | Categoría: {producto["categoria"]} | Precio: {producto["precio"]}€')

def buscar_producto(catalogo):
    busqueda =[]
    buscar = input("Ingrese el nombre o la categoría del producto que desea buscar ")
    for producto in catalogo:
        if buscar == producto["nombre"] or buscar == producto["categoria"]:
            busqueda.append({
                "id": producto["id"], 
                "nombre": producto["nombre"], 
                "categoria":producto["categoria"], 
                "precio":producto["precio"]   
                })
    if busqueda:
        mostrar_catalogo(busqueda)
    else:
        print("Producto no encontrado")

def agregar_al_carrito(catalogo, carrito):
    producto_existe = 0 
    agregar = int(input("Ingrese el id del producto que desea agregar a su carrito de compras: "))
    for producto in catalogo:
        if agregar == producto["id"]:
            producto_existe = 1
            cantidad = int(input("Ingrese la cantidad de unidades que desea: "))
            if cantidad > 0:
                carrito.append({
                "id": producto["id"], 
                "nombre": producto["nombre"], 
                "categoria":producto["categoria"], 
                "cantidad": cantidad,
                "precio":producto["precio"]   
                })
            else:
                print("La cantidad no puede ser cero o menor")
    if  producto_existe == 0:
        print("Producto no encontrado")

def ver_carrito(carrito):
    total=0
    if carrito:
        for producto in carrito:
            print(f'ID: {producto["id"]} | Nombre: {producto["nombre"]} | Cantidad: {producto["cantidad"]} | Precio: {producto["precio"]}€ | Subtotal:{producto["cantidad"]*producto["precio"]}€')
            total += producto["cantidad"]*producto["precio"]
        print(f'El total de su compra es de: {total}€')    
    else:
        print("Su carrito de compras esta vacio")


def vaciar_carrito(carrito):
    carrito.clear()
    print("Su carrito de compras se ha vaciado exitosamente")

catalogo = [
    {"id": 1, "nombre": "camiseta", "categoria": "ropa", "precio": 15.99},
    {"id": 2, "nombre": "auriculares", "categoria": "tecnologia", "precio": 29.90},
    {"id": 3, "nombre": "lampara", "categoria": "hogar", "precio": 18.50},
    {"id": 4, "nombre": "balon de futbol", "categoria": "deportes", "precio": 22.00},
    {"id": 5, "nombre": "gel de ducha", "categoria": "aseo", "precio": 4.75}
]

carrito = []
opcion_usuario = ""

while opcion_usuario !="0":
    mostrar_menu()
    opcion_usuario = input("seleccione una opcion: ")
    if opcion_usuario =="1":
        mostrar_catalogo(catalogo)
    elif opcion_usuario=="2":
        buscar_producto(catalogo)
    elif opcion_usuario=="3":
        agregar_al_carrito(catalogo, carrito)
    elif opcion_usuario=="4":
        ver_carrito(carrito)
    elif opcion_usuario=="5":
        vaciar_carrito(carrito)
    elif opcion_usuario=="0":
        print("Saliendo de l aplicacion")
    else:
        print("Opción no valida")
