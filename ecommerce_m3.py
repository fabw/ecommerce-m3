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

def buscar_producto():
    pass





catalogo = [
    {"id": 1, "nombre": "camiseta", "categoria": "ropa", "precio": 15.99},
    {"id": 2, "nombre": "auriculares", "categoria": "tecnologia", "precio": 29.90},
    {"id": 3, "nombre": "lampara", "categoria": "hogar", "precio": 18.50},
    {"id": 4, "nombre": "balon de futbol", "categoria": "deportes", "precio": 22.00},
    {"id": 5, "nombre": "gel de ducha", "categoria": "aseo", "precio": 4.75}
]




    
opcion_usuario = ""

while opcion_usuario !="0":
    mostrar_menu()
    opcion_usuario = input("seleccione una opcion: ")
    if opcion_usuario =="1":
        mostrar_catalogo(catalogo)
    elif opcion_usuario=="2":
        pass
    elif opcion_usuario=="3":
        pass
    elif opcion_usuario=="4":
        pass
    elif opcion_usuario=="5":
        pass
    elif opcion_usuario=="0":
        pass
    else:
        print("Opción no valida")




