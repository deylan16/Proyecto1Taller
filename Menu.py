#Hola
from LectorDeArchivos import *
pasillos = CargarPasillos()
productosPasillo = CargarProductospasillo(pasillos)
marcasProductos = CargarMarcaproductos(productosPasillo)
inventarios = CargarInventario()
clientes = CargarClientes()
registroTienda = []
RegistroTodasCompras = []
consecutivo = 0
ListaProductos = []
def mostrarLista(lista):
    i =0
    while(i < len(lista)):
        print(lista[i])
        i += 1
   
def buscaEnLista(lista,dato,indice):
    i =0
    while(i < len(lista)):
        if(lista[i][indice] == dato):
            return i
        i += 1
    return -1

def verificaComprar():
        cedula = input('¿digital tu cedula?')
        if(buscaEnLista(clientes,cedula,0) != -1):
            print("El clientes esta registrado")
            OpcionesComprar(cedula)
        else:
            print("El cliente no esta registrado")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digital el numero de la opcion?')
            if(opcion == "1"):
                verificaComprar()
            elif(opcion == "2"):
                menu()

def tiene13(codMarca):
    posicion = buscaEnLista(inventarios,codMarca,2)
    
    if(inventarios[posicion][5] == "0"):
        return True
    else:
        return False
def facturar():
    global registroTienda,ListaProductos,RegistroTodasCompras
    if(len(registroTienda) != 0):
        facturando = registroTienda[0]
        factura = open("Archivos/"+facturando[0]+(str)(consecutivo) +".txt", "w")
        i = 0

        nombre = buscaEnLista(clientes,facturando[0],0)
        
        factura.write("Nombre:"+ clientes[nombre][1] + "\n")
        factura.write("Cedula:"+ facturando[0] + "\n")
        factura.write("Consecutivo:"+ (str)(consecutivo) + "\n")
        factura.write("Marca:CantidadxPrecio+= total" + "\n")
        factura.write("\n")
        precioTotal = 0
        while (i< len(facturando[1])):
  
            string = facturando[1][i][3]+ ":" +facturando[1][i][4] + "x" + facturando[1][i][5]
            ListaProductos += [[facturando[1][i][2],facturando[1][i][4]]]
            productoMarca1 = buscaEnLista(marcasProductos,facturando[1][i][2],2)
            marcasProductos[productoMarca1][4] = (str)((int)(marcasProductos[productoMarca1][4])-(int)(facturando[1][i][4]))
            
            if (tiene13(facturando[1][i][2]) ):
                string += "+ 13% = "
                total = ((int)(facturando[1][i][4])*(int)(facturando[1][i][5]))* 1.13
                string += (str)(total)
                precioTotal += total
            else:
                string += " = "
                total = ((int)(facturando[1][i][4])*(int)(facturando[1][i][5]))
                string += (str)(total)
                precioTotal += total
            
            factura.write(string + "\n")

            i+= 1
        factura.write("\n")
        factura.write("Monto total:"+ (str)(precioTotal) + "\n")
        factura.close()
        RegistroTodasCompras += registroTienda[0]
        registroTienda = registroTienda[1:]
        
        menu()
    else:
        print("No hay facturas pendientes")
        menu()



def OpcionesComprar(cedula):
        listaCompraCliente = [cedula]
        productoscomprados = []
        while (True):
            print("***********************")
            print("1.Pasillos")
            print("2.Productos")
            print("3.Marcas")
            print("4.Comprar producto")
            print("5.Eliminar producto")
            print("6.Cancelar")
            print("7.Terminar")

            print("***********************")
            opcion = input('¿digital el numero de la opcion?')
            if(opcion == "1"):
                print("***********************")
                print("Pasillos:")
                mostrarLista(pasillos)
                continue
            elif(opcion == "2"):
                print("***********************")
                print("Productos:")
                mostrarLista(productosPasillo)
                continue
            elif(opcion == "3"):
                print("***********************")
                print("Marcas:")
                mostrarLista(marcasProductos)
                continue
            elif(opcion == "4"):
                print("***********************")
                print("Comprando")
                codigoProducto = input('Ingrese el codigo del producto que desea comprar')
                if(buscaEnLista(productosPasillo,codigoProducto,1) != -1):
                    cantidadProducto = input('Ingrese la cantidad que desea comprar')
                    posicion = buscaEnLista(productosPasillo,codigoProducto,1)
                    productoscomprados += [[marcasProductos[posicion][0],marcasProductos[posicion][1],marcasProductos[posicion][2],marcasProductos[posicion][3],cantidadProducto,marcasProductos[posicion][5]]]
                    continue
                else:
                    print("El producto no se encuentra registrado")
                    continue
            elif(opcion == "5"):
                print("***********************")
                print("Eliminando productos")
                
                mostrarLista(productoscomprados)
                productoeliminar = input('Ingrese el codigo del producto que desea eliminar')
                posicion = (buscaEnLista(productoscomprados,productoeliminar,1))
                if(posicion != -1):
                    print("eliminado")
                else:
                    print("Ese producto no esta en tu lista de compras")
                    continue
            elif(opcion == "6"):
                print("Cancelando producto")
                break
            elif(opcion == "7"):
                global registroTienda
                listaCompraCliente += [productoscomprados]
                registroTienda += [listaCompraCliente]
                print(registroTienda)

                break
                #listaCompraCliente += [productoscomprados]
                #registroTienda += [listaCompraCliente]
        menu()
            
def RevisarGondolas():
    print("Estoy revisando gondolas")


def VerificarInventario():
    print("estoy en inventario")


def Reportes():
    print("Estoy en inventario")

    
def menu():
    print("***********************")
    print("1.Comprar")
    print("2.Facturar")
    print("3.Revisar góndolas")
    print("4.Verificar inventario")
    print("5.Reportes")
    print("***********************")
    opcion = input('¿digital el numero de la opcion?')
    if(opcion == "1"):
        verificaComprar()
    elif(opcion == "2"):
        facturar()
    elif(opcion == "3"):
        RevisarGondolas()
    elif(opcion == "4"):
        VerificarInventario()
    elif(opcion == "5"):
        Reportes()
    
menu()
