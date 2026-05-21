def electrodomesticos():
    productos = {}
    
    for i in range(10):
        nombreProducto = input (f"ingrese nombre del producto #{i+1}:")
        precioProducto = float(input(f"ingrese el precio de {nombreProducto}:"))
        
        productos[nombreProducto] = precioProducto
        
    return productos

def main():
    listaProductos = electrodomesticos()
    print("el diccionario de productos es:", listaProductos)
        