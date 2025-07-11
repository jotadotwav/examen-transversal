#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
};

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
#funcion para stock
def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if (datos[0].lower() == marca.lower ()):
            total += stock[codigo][1];
    print(f"el stock total para {marca} es: {total}");

#Funcion de busqueda por precio
def busqueda_por_precio (precio_min, precio_max):
    resultados = [];
    for codigo, datos in productos.items():
        precio = stock[codigo][0]
        if precio >= precio_min and precio <= precio_max and stock[codigo][1] > 0 :
            resultados.append(datos [0] + "---" + codigo);
    if resultados:
        resultados.sort();
        print("productos encontrados: ", resultados);
    else:
        print(" no hay productos en ese rango de precio")



#Funcion de actualizar precio
def actualizar_precio(codigo, nuevo_precio):
    if (codigo in stock):
        stock[codigo][1] = nuevo_precio
        return True;
    return False;


#MENU
def main():
    while True:
        try:
            print("*** MENU PRINCIPAL ***")
            print("1. Stock marca.")
            print("2. Búsqueda por precio.")
            print("3. Actualizar precio.")
            print("4. Salir.")
            opc = int(input("Ingrese opción: "))
        except ValueError:
            print(" ingrese un valor numerico correcto porfavor")
        if opc == 1 :
            marca = input("ingrese la marca del producto que desea: ")
            stock_marca(marca);
        elif opc == 2:
            while True:
                try:
                    precio_min = int(input("ingrese el precio minimo: "))
                    precio_max = int(input("ingrese el precio maximo: "))
                    busqueda_por_precio(precio_min, precio_max)
                except ValueError:
                    print("Debe ingresar valores enteros!!")
                else:
                    break;
        elif opc == 3:
            while True:
                codigo = input("ingresa codigo de producto: ")
                try:
                    nuevo_precio = float(input("ingresa nuevo precio"))
                    if actualizar_precio(codigo, nuevo_precio):
                        print("precio actualizado! ")
                    else:
                        print("el codigo no existe")
                except ValueError:
                    print("ingresa solo numeros")
                repetir = input("Desea actualizar otro precio (s/n)?:").lower();
                if(repetir != 's'):
                    break;

        elif opc == 4:
            print(" adios! ")
            break;
        else: 
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    main();