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
Administradores =  CargarAdministradores()


######para reportes######
pasillosComprados = []
PasilloProductosComprados = []
MarcasCompradas = []
ClientesMontoComprados = []
ProductoCantidaCargados = []
ClientesFacturados = []
FacturaMontoRealizadas = []
cedulaFacturas = []
cantidadDescuento = 3
porcentajeDescuento = 5
#########################

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
def buscaEnLista2(lista,dato,indice):
    i =0
   
    listaR = []
    
    
    while(i < len(lista)):
        
        if(lista[i][indice] == dato):
            listaR +=[lista[i]]
        i += 1
    return listaR

def verificaNumero(n):
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    for i in range(len(n)):
        if (not(n[i] in numeros)):
            return False
    return True
def verificaComprar():
        cedula = input('¿Digite su cedula?')
        if(buscaEnLista(clientes,cedula,0) != -1):
            print("El cliente esta registrado")
            OpcionesComprar(cedula)
        else:
            print("El cliente no esta registrado")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                verificaComprar()
            elif(opcion == "2"):
                menu()
            else:
                print("El dato ingresado no es permitido")
                menu()


def verificaComprar():
        cedula = input('¿Digite su cedula?')
        if(buscaEnLista(clientes,cedula,0) != -1):
            print("El cliente esta registrado")
            menuClienteRegistrado(cedula)
        else:
            menuClienteNoRegistrado(cedula)
def verificaAdministrador():
        codigo = input('¿Digite su codigo de administrador?')
        if(buscaEnLista(Administradores,codigo,0) != -1):
            print("El Administrador esta registrado")
            menuAdministrador()
            
        else:
            print("El Administrador no esta registrado")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                verificaAdministrador()
            elif(opcion == "2"):
                menuQuienEntra()
            else:
                print("El dato ingresado no es permitido")
                menuQuienEntra()
    
def tiene13(codMarca):
    posicion = buscaEnLista(inventarios,codMarca,2)
    
    if(inventarios[posicion][5] == "0"):
        return True
    else:
        return False
def facturar():
    print("----------------------------------")
    print("Se esta factaurando")
    print("----------------------------------")
    global registroTienda,ListaProductos,RegistroTodasCompras,pasillosComprados,PasilloProductosComprados,MarcasCompradas,ClientesMontoComprados
    global ProductoCantidaCargados,ClientesFacturados,FacturaMontoRealizadas
    if(len(registroTienda) != 0):
        facturando = registroTienda[0]
        factura = open("Archivos/"+facturando[0]+(str)(cantidadFacturas(facturando[0])) +".txt", "w")
        i = 0

        nombre = buscaEnLista(clientes,facturando[0],0)
        factura.write("Consecutivo Factura: #"+ (str)(cantidadFacturas(facturando[0])) + "\n")
        factura.write("\n")
        factura.write("Cedula:"+ facturando[0] + "\n")
        factura.write("Nombre:"+ clientes[nombre][1] + "\n")
        factura.write("Telefono:"+ clientes[nombre][2] + "\n")
        factura.write("\n")
        factura.write("Producto\tCantidad\tPrecio Unitario\ttotal\n")
        
        
        #factura.write("Marca:CantidadxPrecio+= total" + "\n")
        #factura.write("\n")
        precioTotal = 0
        while (i< len(facturando[1])):
            cantidad = facturando[1][i][4] 
            precio = facturando[1][i][5]
            producto = facturando[1][i][3]
            string = ""+producto+"\t"+cantidad+"\n"+precio
            ListaProductos += [[facturando[1][i][2],facturando[1][i][4]]]
            productoMarca1 = buscaEnLista(marcasProductos,facturando[1][i][2],2)
            print(marcasProductos[productoMarca1][4] )
            marcasProductos[productoMarca1][4] = (str)((int)(marcasProductos[productoMarca1][4])-(int)(facturando[1][i][4]))
            print(marcasProductos[productoMarca1][4] )
            #####para #######
            productoComprando = facturando[1][i]

            pasillosComprados += [productoComprando[0]]
            for j in range((int)(facturando[1][i][4])):
                PasilloProductosComprados += [[productoComprando[0],productoComprando[3]]]
            MarcasCompradas += [productoComprando[2]]
            
            
            #################
            if (tiene13(facturando[1][i][2]) ):
                string += "+ 13% \t "
                total = ((int)(facturando[1][i][4])*(int)(facturando[1][i][5]))* 1.13
                string += (str)(total)
                precioTotal += total
            else:
                
                total = ((int)(facturando[1][i][4])*(int)(facturando[1][i][5]))
                string += (str)(total)
                precioTotal += total
            
            factura.write(string + "\n")

            i+= 1
        factura.write("\n")
        factura.write("Total:"+ (str)(precioTotal) + "\n")
        if(descuento(facturando[0])):
            factura.write("Descuento:"+ (str)(porcentajeDescuento) + "%\n")
            factura.write("Total a Pagar:"+ (str)(precioTotal-(precioTotal *(porcentajeDescuento/100))) + "\n")
        else:
            factura.write("Descuento:"+ (str)(0) + "%\n")
            factura.write("Total a Pagar:"+ (str)(precioTotal) + "\n")
        


        #######para reportes#####
        indiceClienteMonto = buscaEnLista(ClientesMontoComprados,facturando[0],0)
        if(indiceClienteMonto != -1):
            ClientesMontoComprados[indiceClienteMonto][1] = ClientesMontoComprados[indiceClienteMonto][1] + precioTotal
        else:
            ClientesMontoComprados += [[facturando[0],precioTotal]]
        ClientesFacturados += [facturando[0]]
        #print(ClientesMontoComprados)
        FacturaMontoRealizadas += [[facturando[0]+(str)(consecutivo),precioTotal]]
        #########################
        factura.close()
        RegistroTodasCompras += registroTienda[0]
        registroTienda = registroTienda[1:]
        
        menuAdministrador()
    else:
        print("No hay facturas pendientes")
        menuAdministrador()



def OpcionesComprar(cedula):
        print("----------------------------------")
        print("Estas comprando")
        print("----------------------------------")
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
                productoscomprados += comprando(cedula)
                """codigoProducto = input('Ingrese el codigo de la marca que desea comprar')
                if(buscaEnLista(marcasProductos,codigoProducto,2) != -1):
                    cantidadProducto = input('Ingrese la cantidad que desea comprar')
                    if(verificaNumero(cantidadProducto)):
                        posicion = buscaEnLista(marcasProductos,codigoProducto,2)
                        if ((int)(cantidadProducto) <= (int)(marcasProductos[posicion][4])):
                            
                            productoscomprados += [[marcasProductos[posicion][0],marcasProductos[posicion][1],marcasProductos[posicion][2],marcasProductos[posicion][3],cantidadProducto,marcasProductos[posicion][5]]]
                            print("-----------------------------")
                            mostrarLista(productoscomprados)
                            continue
                        else:
                            print("No tenemos esa cantidad en gondola")
                            continue
                    else:
                        print("El dato ingresado es erroneo")
                        continue
                else:
                    print("El producto no se encuentra registrado")
                    continue"""
            elif(opcion == "5"):
                print("***********************")
                print("Eliminando productos")
                if(len(productoscomprados) > 0):
                
                    mostrarLista(productoscomprados)
                    productoeliminar = input('Ingrese el codigo de la marca que desea que desea eliminar')
                    posicion = (buscaEnLista(productoscomprados,productoeliminar,2))
                    if(posicion != -1):
                        productoscomprados.pop(posicion)
                        print("eliminado")
                    else:
                        print("Ese producto no esta en tu lista de compras")
                        continue
                else:
                    print("No tienes productos en tu carrito")
                    continue
            elif(opcion == "6"):
                print("Cancelando producto")
                break
            elif(opcion == "7"):
                global registroTienda
                if(len(productoscomprados) > 0):
                    listaCompraCliente += [productoscomprados]
                    registroTienda += [listaCompraCliente]
##                    print(registroTienda)

                else:
                    print("No compraste nada")

                break
                #listaCompraCliente += [productoscomprados]
                #registroTienda += [listaCompraCliente]
        menuClienteRegistrado(cedula)

def admministrador():
    while(True):
        contraseña = input('Digite la contraseña de administador')
        if(contraseña == "Admin"):
            return True
        else:
            print("Contraseña Incorrecta")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                break
    menuAdministrador()
        
            
def RevisarGondolas():
    print("----------------------------------")
    print("Estas Revisando Gondolas")
    print("----------------------------------")
    if(admministrador()):
        global ProductoCantidaCargados
        
        print("----------------")
        print("Lista de gondolas")
        mostrarLista(marcasProductos)
        print("----------------")
        print("Lista del inventario")
        mostrarLista(inventarios)
        print("----------------")
        for producto in marcasProductos:
            cantidadGondola=(int)(producto[4])
            if cantidadGondola<=2:
                while(True):
                   print("El producto "+ producto[2]+":"+producto[3]+" tiene pocas unidades")
                   cantidadSumar=input("Digite la cantidad que desea sumar")
                   
                   if(verificaNumero(cantidadSumar)):
                           cantidadSumar=(int)(cantidadSumar)
                           ######para reportes######
                           indiceClienteMonto = buscaEnLista(ProductoCantidaCargados,producto[2],0)
                           if(indiceClienteMonto != -1):
                                ProductoCantidaCargados[indiceClienteMonto][1] = ProductoCantidaCargados[indiceClienteMonto][1] + cantidadSumar
                           else:
                                ProductoCantidaCargados += [[producto[2],cantidadSumar]]
                           ##ProductoCantidaCargados += [[producto[2],cantidadSumar]]
                           #########################
                           cantidadGondola+=cantidadSumar
                           producto[4]=cantidadGondola
                           indiceproductoinventario=buscaEnLista(inventarios,producto[2],2)
                           inventarios[indiceproductoinventario][4]=(str)((int)(inventarios[indiceproductoinventario][4])-cantidadSumar)
                           break
                   else:
                        print("El dato ingresado es erroneo")
                        continue
               
        print("----------------")
        print("Lista de gondolas")
        mostrarLista(marcasProductos)
        print("----------------")
        print("Lista del inventario")
        print("----------------")
        mostrarLista(inventarios)
        menuAdministrador()
    

   

def VerificarInventario():
    print("----------------------------------")
    print("Estas Revisando Inventario")
    print("----------------------------------")
    if(admministrador()):
        mostrarLista(inventarios)
        for Productos in inventarios:
            CantidadStock=(int)(Productos[4])
            if CantidadStock<=20:
                while(True):
                    print("El producto "+ Productos[2]+":"+Productos[3]+" tiene pocas unidades")
                    CantidadSumar=input("Ingrese la cantidad que desea sumar")
                    if(verificaNumero(CantidadSumar)):
                        CantidadSumar=(int)(CantidadSumar)
                    
                        CantidadStock+=CantidadSumar
                        Productos[4]=CantidadStock
                        break
                    else:
                        print("El dato ingresado es erroneo")
                        continue
        mostrarLista(inventarios)
        menuAdministrador()



def moda(lista):
    frecuencia = {}

    for valor in lista:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1

    masFrecuentes = max(frecuencia.values())

    modas = [key for key, valor in frecuencia.items()
                      if valor == masFrecuentes]

    return modas
 

def modaInversa(lista):
    frecuencia = {}

    for valor in lista:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1

    menosFrecuentes = min(frecuencia.values())

    modas = [key for key, valor in frecuencia.items()
                      if valor == menosFrecuentes]

    return modas


######para reportes######
#pasillosComprados = []
#PasilloProductosComprados = []
#MarcasCompradas = []
#ClientesMontoComprados = []
#ProductoCantidaCargados = []
#ClientesFacturados = []
#FacturaMontoRealizadas = []
#########################
def Hagalista(lista,llave,indice):
    result = []
    for i in lista:
        
        if(i[indice] == llave):
            result += [i[1]]
    return result
           
def montosFactutados(lista):
    monto = 0
    resultado = []
    for n in lista:
        if((int)(n[1]) > monto):
            monto = (int)(n[1])
            resultado = [n]
        elif((int)(n[1]) == monto):
            
            resultado += [n]
    return resultado
def montosFactutadosmenos(lista):
    monto = montosFactutados(lista)[0][1]
    resultado = []
    for n in lista:
        if((int)(n[1]) < monto):
            monto = (int)(n[1])
            resultado = [n]
        elif((int)(n[1]) == monto):
            
            resultado += [n]
    return resultado
def Reportes():
    print("----------------------------------")
    print("Estas en la seccion de reportes")
    print("----------------------------------")
    while ( True):
            
            
            print("***********************")
            print("1.Pasillo mas visitado")
            print("2.Pasillo menos visitado")
            print("3.Productos por pasillo mas vendido")
            print("4.Marcas mas vendidas")
            print("5.Cliente que mas compro")
            print("6.Cliente que menos compro")
            print("7.Producto que mas se cargo en las Gondolas")
            print("8.Cliente que mas facturo")
            print("9.Marcas de un producto")
            print("10.Factura de mayor monto")
            print("11.Productos de un pasillo")
            print("12.Clientes del supermercado")
            print("13.Pasillos del supermercado")
            print("14.Inventario del supermercado")
            print("15.Volver al menu")

            print("***********************")
            opcion = input('¿digital el numero de la opcion?')
            if(opcion == "1"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print("Pasillo más visitado:")
                    print(moda(pasillosComprados))
                    continue
            
            elif(opcion == "2"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print("Pasillo menos visitado:")
                    print(modaInversa(pasillosComprados))
                    continue
            
            elif(opcion == "3"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print("Productos por pasillo más vendidos:")
                    mostrarLista(pasillos)
                    buscarpasillo=input("Ingrese el pasillo que desea buscar")
                    if buscaEnLista(pasillos,buscarpasillo,0)!=-1:
                        
                        resultado = ""
                        
                       
                        print("El producto mas comprado del pasillo "+buscarpasillo+" es:"+resultado)
                        print(moda(Hagalista(PasilloProductosComprados,buscarpasillo,0)))
                    else:
                        print("El pasillo no esta")
                        
                    continue
            elif(opcion == "4"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print("Marcas más vendidos:")
                    print(moda(MarcasCompradas))
                    continue

                
            elif(opcion == "5"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print("Cliente que más compro:")
                    print(montosFactutados(ClientesMontoComprados))

                    continue
            elif(opcion == "6"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print(montosFactutadosmenos(ClientesMontoComprados))

                
                    continue
            elif(opcion == "7"):
                print("***********************")
                print("Producto que más se cargó en las Góndolas:")
                print(montosFactutados(ProductoCantidaCargados))

                continue
            elif(opcion == "8"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print("Cliente que más facturo:")
                    print(moda(ClientesFacturados))

                    continue
            elif(opcion == "9"):
                print("***********************")
                print("Marcas de un producto:")
                mostrarLista(productosPasillo)
                BuscarPasillo=input("Ingrese el pasillo que desea buscar")
                indice=buscaEnLista(productosPasillo,BuscarPasillo,0)
                if indice!=-1:
                    BuscarProducto=input("Ingrese el producto que desea buscar")
                    indice2=buscaEnLista(productosPasillo,BuscarProducto,1)
                    if indice2!=-1:
                        for p in marcasProductos:
                            if (BuscarPasillo == p[0]  and BuscarProducto ==p[1] ):
                                print(p)
                    else:
                        print("El producto no esta")
                else:
                    print("El pasillo no esta")

                continue
            elif(opcion == "10"):
                if RegistroTodasCompras==[]:
                    print("No se ha facturado nada")
                    
                    continue
                else:
                    print("***********************")
                    print("Factura de mayor monto:")
                    print(montosFactutados(FacturaMontoRealizadas))
                    

                    continue
            elif(opcion == "11"):
                print("***********************")
                print("Productos de un pasillo:")
                mostrarLista(productosPasillo)
                BuscarPasillo=input("Ingrese el pasillo que desea buscar")
                indice=buscaEnLista(productosPasillo,BuscarPasillo,0)
                if indice!=-1:
                    
                    indice=buscaEnLista(productosPasillo,BuscarPasillo,0)
                    mostrarLista(productosPasillo[indice])
                else:
                    print("El pasillo no esta")
                continue
            
            elif(opcion == "12"):
                print("***********************")
                print("Clientes del supermercado:")
                mostrarLista(clientes)
                continue 
            elif(opcion == "13"):
                print("***********************")
                print("Pasillos del supermercado:")
                mostrarLista(pasillos) 
                continue 
            elif(opcion == "14"):
                print("***********************")
                print("Inventario del supermercado:")
                mostrarLista(inventarios)

            elif(opcion == "15"):
                break
                    
            else:
                print("1.Desea volver a intentar")
                print("2.Volver al menu")
                print("***********************")
                opcion2 = input('¿digital el numero de la opcion?')
                if(opcion2 == "1"):
                    continue 
                elif(opcion2 == "2"):
                    break
                else:
                    print("El dato ingresado no es permitido")
                    break
    menuAdministrador()
        
    
##########################################################
def comprando(cedula):
    productoscomprados = []
    while(True):
        
        codigoPasillo = input('¿Digite su codigo del pasillo')
        listaCodigoPasillo = buscaEnLista2(marcasProductos,codigoPasillo,0)
        mostrarLista(listaCodigoPasillo)
        
        if(listaCodigoPasillo != []):
            codigoProducto = input('¿Digite su codigo del producto')
            listaCodigoPasilloCodigoProducto = buscaEnLista2(listaCodigoPasillo,codigoProducto,1)
            mostrarLista(listaCodigoPasilloCodigoProducto)
            if(listaCodigoPasilloCodigoProducto != []):
                codigoMarca = input('¿Digite su codigo de Marca')
                listaCodigoPasilloCodigoMarca = buscaEnLista2(listaCodigoPasilloCodigoProducto,codigoMarca,2)
                if(listaCodigoPasilloCodigoMarca != []):
                    print(listaCodigoPasilloCodigoMarca[0])
                    cantidadProducto = input('Ingrese la cantidad que desea comprar')
                    if(verificaNumero(cantidadProducto)):
                        
                        if ((int)(cantidadProducto) <= (int)(listaCodigoPasilloCodigoMarca[0][4])):
                            
                            productoscomprados += [[listaCodigoPasilloCodigoMarca[0][0],listaCodigoPasilloCodigoMarca[0][1],listaCodigoPasilloCodigoMarca[0][2],listaCodigoPasilloCodigoMarca[0][3],cantidadProducto,listaCodigoPasilloCodigoMarca[0][5]]]
                            print("-----------------------------")
                            mostrarLista(productoscomprados)
                            print("***********************")
                            print("1.Seguir Comprando")
                            print("2.volver al menu")
                            print("***********************")
                            opcion = input('¿digite el numero de la opcion?')
                            if(opcion == "1"):
                                    comprando(cedula)
                            elif(opcion == "2"):
                                    OpcionesComprar(cedula)
                            else:
                                return OpcionesComprar(cedula)
                        else:
                            print("No tenemos esa cantidad en gondola te puedo vender "+listaCodigoPasilloCodigoMarca[0][4])
                            print("***********************")
                            print("1.No")
                            print("2.Si ")
                            print("***********************")
                            opcion = input('¿digite el numero de la opcion?')
                            if(opcion == "1"):
                                print("***********************")
                                print("1.Seguir Comprando")
                                print("2.volver al menu")
                                print("***********************")
                                opcion = input('¿digite el numero de la opcion?')
                                if(opcion == "1"):
                                    comprando(cedula)
                                elif(opcion == "2"):
                                    OpcionesComprar(cedula)
                                else:
                                    return OpcionesComprar(cedula)
                            elif(opcion == "2"):
                                productoscomprados += [[listaCodigoPasilloCodigoMarca[0][0],listaCodigoPasilloCodigoMarca[0][1],listaCodigoPasilloCodigoMarca[0][2],listaCodigoPasilloCodigoMarca[0][3],listaCodigoPasilloCodigoMarca[0][4],listaCodigoPasilloCodigoMarca[0][5]]]
                                mostrarLista(productoscomprados)
                                print("***********************")
                                print("1.Seguir Comprando")
                                print("2.volver al menu")
                                print("***********************")
                                opcion = input('¿digite el numero de la opcion?')
                                if(opcion == "1"):
                                    comprando(cedula)
                                elif(opcion == "2"):
                                    OpcionesComprar(cedula)
                                else:
                                    return OpcionesComprar(cedula)
                            else:
                                print("***********************")
                                print("1.Seguir Comprando")
                                print("2.volver al menu")
                                print("***********************")
                                opcion = input('¿digite el numero de la opcion?')
                                if(opcion == "1"):
                                    comprando(cedula)
                                elif(opcion == "2"):
                                    OpcionesComprar(cedula)
                                else:
                                    return OpcionesComprar(cedula)
                            
                    else:
                        print("El dato ingresado es erroneo")
                        continue
                else:
                    print("codigo incorrecto")
                    print("***********************")
                    print("1.volver a intentar")
                    print("2.volver al menu")
                    print("***********************")
                    opcion = input('¿digite el numero de la opcion?')
                    if(opcion == "1"):
                        continue
                    elif(opcion == "2"):
                        return productoscomprados
                    else:
                        return productoscomprados   

            else:
                print("codigo incorrecto")
                print("***********************")
                print("1.volver a intentar")
                print("2.volver al menu")
                print("***********************")
                opcion = input('¿digite el numero de la opcion?')
                if(opcion == "1"):
                    continue
                elif(opcion == "2"):
                    return productoscomprados
                else:
                    return productoscomprados            
        else:
            print("codigo incorrecto")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                return productoscomprados
            else:
                return productoscomprados    
        
def consultarPrecio():
    mostrarLista(marcasProductos)
    while(True):
        codigoPasillo = input('¿Digite su codigo del pasillo')
        listaCodigoPasillo = buscaEnLista2(marcasProductos,codigoPasillo,0)
        mostrarLista(listaCodigoPasillo)
        
        if(listaCodigoPasillo != []):
            codigoProducto = input('¿Digite su codigo del producto')
            listaCodigoPasilloCodigoProducto = buscaEnLista2(listaCodigoPasillo,codigoProducto,1)
            mostrarLista(listaCodigoPasilloCodigoProducto)
            if(listaCodigoPasilloCodigoProducto != []):
                codigoMarca = input('¿Digite su codigo de Marca')
                listaCodigoPasilloCodigoMarca = buscaEnLista2(listaCodigoPasilloCodigoProducto,codigoMarca,2)
                if(listaCodigoPasilloCodigoMarca != []):
                    print(listaCodigoPasilloCodigoMarca[0][5])
                    
                    return -1
                else:
                    print("codigo incorrecto")
                    print("***********************")
                    print("1.volver a intentar")
                    print("2.volver al menu")
                    print("***********************")
                    opcion = input('¿digite el numero de la opcion?')
                    if(opcion == "1"):
                        continue
                    elif(opcion == "2"):
                        return -1
                    else:
                        return -1   

            else:
                print("codigo incorrecto")
                print("***********************")
                print("1.volver a intentar")
                print("2.volver al menu")
                print("***********************")
                opcion = input('¿digite el numero de la opcion?')
                if(opcion == "1"):
                    continue
                elif(opcion == "2"):
                    return -1
                else:
                    return -1            
        else:
            print("codigo incorrecto")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                return -1
            else:
                return -1
    


def consultarProductos():
    mostrarLista(pasillos)
    while(True):
        codigoPasillo = input('¿Digite su codigo del pasillo')
        listaCodigoPasillo = buscaEnLista2(productosPasillo,codigoPasillo,0)
        
        
        if(listaCodigoPasillo != []):
            mostrarLista(listaCodigoPasillo)
            return -1

                    
        else:
            print("codigo incorrecto")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                return -1
            else:
                return -1

def cantidadFacturas(cedula):
    contador  = 0
    for i in ClientesFacturados:
        if cedula == ClientesFacturados[0]:
                contador += 1
    return contador

def descuento(cedula):
    contador  = 0
    for i in ClientesFacturados:
        if cedula == ClientesFacturados[0]:
                contador += 1
    if contador >= cantidadDescuento:
        return True
    else:
        return False    







    
def menu():
    print("----------------------------------")
    print("Estas en el menu principal")
    print("----------------------------------")
    print("***********************")
    print("1.Comprar")
    print("2.Facturar")
    print("3.Revisar góndolas")
    print("4.Verificar inventario")
    print("5.Reportes")
    print("***********************")
    opcion = input('¿digite el numero de la opcion?')
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
    else:
        print("El dato ingresado no es permitido")
        menu()

def menuQuienEntra():
    print("----------------------------------")
    print("Estas en el menu para elegir quien entra")
    print("----------------------------------")
    print("***********************")
    print("1.Administrador")
    print("2.Cliente")
    
    print("***********************")
    opcion = input('¿digite el numero de la opcion?')
    if(opcion == "1"):
        verificaAdministrador()
    elif(opcion == "2"):
        verificaComprar()
    
    else:
        print("El dato ingresado no es permitido")
        menuQuienEntra()

def menuClienteRegistrado(cedula):
    print("----------------------------------")
    print("Estas en el menu de cliente registrado")
    print("----------------------------------")
    print("1.Consultar precio")
    print("2.Consultar Descuento")
    print("3.Consultar Productos")
    print("4.Comprar")
    print("5.volver al menu inicial")
    print("***********************")
    opcion = input('¿digite el numero de la opcion?')
    if(opcion == "1"):
        print("Consultando precio")
        consultarPrecio()
        menuClienteRegistrado(cedula)
    elif(opcion == "2"):
        print("Consultando Descuentos")
        if descuento(cedula):
            print("Tiene descuento de "+porcentajeDescuento+"%")
        else:
            print("No tiene descuento")
        menuClienteRegistrado(cedula)
    elif(opcion == "3"):
        print("Consultando productos")
        consultarProductos()
        menuClienteRegistrado(cedula)
    elif(opcion == "4"):
        print("Comprando")
        OpcionesComprar(cedula)
    
    elif(opcion == "5"):
        menuQuienEntra()
    
    
    else:
        print("El dato ingresado no es permitido")
        menuClienteNoRegistrado()
    print("----------------------------------")

def menuClienteNoRegistrado(cedula):
    print("----------------------------------")
    print("Estas en el menu de cliente no registrado")
    print("***********************")
    print("1.Consultar precio")
    print("2.Consultar Productos")
    print("3.volver al menu inicial")
    print("***********************")
    opcion = input('¿digite el numero de la opcion?')
    if(opcion == "1"):
        print("Consultando precio")
        consultarPrecio()
        menuClienteNoRegistrado(cedula)
    elif(opcion == "2"):
        print("Consultando productos")
        consultarProductos()
        menuClienteNoRegistrado(cedula)
    elif(opcion == "3"):
        menuQuienEntra()
    
    
    else:
        print("El dato ingresado no es permitido")
        menuClienteNoRegistrado(cedula)
    print("----------------------------------")

def insertarProductonuevo():
    global marcasProductos,inventarios
    mostrarLista(pasillos)
    while(True):
        CodigoPasillo=input('¿digite su codigo del Pasillo?')
        listaCodigoPasillo=buscaEnLista2(pasillos,CodigoPasillo,0)
        if (listaCodigoPasillo)!=[]:
            mostrarLista(listaCodigoPasillo)
            CodigoProducto=input('¿digite su codigo del Producto?')
            listaCodigoProducto=buscaEnLista2(productosPasillo,CodigoProducto,0)
            if (listaCodigoProducto)!=[]:
                mostrarLista(listaCodigoProducto)
                CodigoMarca=input('¿digite su codigo de Marca?')
                listaCodigoMarcas=buscaEnLista2(marcasProductos,CodigoMarca,0)
                if (listaCodigoMarcas)==[]:
                    nombre=input('¿digite el nombre')
                    productoNuevoMarcasProductos = [CodigoPasillo,CodigoProducto,CodigoMarca,nombre]
                    productoNuevoInventario= [CodigoPasillo,CodigoProducto,CodigoMarca,nombre]
                    while(True):
                        cantidadGondola=input('¿digite la cantidad Gondola que desea')
                        if verificaNumero(cantidadGondola)==True:
                            productoNuevoMarcasProductos+=[cantidadGondola]
                            break
                        else:
                            print("El dato ingresado no es un numero")
                            continue
                    while(True):
                        precio=input('¿digite el precio que desea')
                        if verificaNumero(precio)==True:
                            productoNuevoMarcasProductos +=[precio]
                            break
                        else:
                            print("El dato ingresado no es un numero")
                            continue       
                    while(True):
                        cantidadStock=input('¿digite la cantidad de Stock que desea')
                        if verificaNumero(cantidadStock)==True:
                            productoNuevoInventario += [cantidadStock]
                            break
                        else:
                            print("El dato ingresado no es un numero")
                            continue  
                    while(True):
                            codigoCanasta=input('¿digite la codigo Canasta que desea')
                            print("El dato ingresado no es un numero")
                            if codigoCanasta=="0" or codigoCanasta=="1":
                                print("Codigo recibido ")
                                productoNuevoInventario += [codigoCanasta]
                                break
                                
                            else:
                                print("Codigo no permitido")
                                continue 
                    marcasProductos += [productoNuevoMarcasProductos]
                    inventarios += [productoNuevoInventario]
                    break

                else:
                    print("codigo incorrecto")
                    print("***********************")
                    print("1.volver a intentar")
                    print("2.volver al menu")
                    print("***********************")
                    opcion = input('¿digite el numero de la opcion?')
                    if(opcion == "1"):
                        continue
                    elif(opcion == "2"):
                        return -1
                    else:
                        return -1
            else:
                print("codigo incorrecto")
                print("***********************")
                print("1.volver a intentar")
                print("2.volver al menu")
                print("***********************")
                opcion = input('¿digite el numero de la opcion?')
                if(opcion == "1"):
                    continue
                elif(opcion == "2"):
                    return -1
                else:
                    return -1
        else:
            print("codigo incorrecto")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                return -1
            else:
                return -1
    menuAdministrador()
        
def eliminarProducto():
    mostrarLista(marcasProductos)
    while(True):
        codigoPasillo = input('¿Digite su codigo del pasillo')
        listaCodigoPasillo = buscaEnLista2(marcasProductos,codigoPasillo,0)
        mostrarLista(listaCodigoPasillo)
        
        if(listaCodigoPasillo != []):
            codigoProducto = input('¿Digite su codigo del producto')
            listaCodigoPasilloCodigoProducto = buscaEnLista2(listaCodigoPasillo,codigoProducto,1)
            mostrarLista(listaCodigoPasilloCodigoProducto)
            if(listaCodigoPasilloCodigoProducto != []):
                codigoMarca = input('¿Digite su codigo de Marca')
                listaCodigoPasilloCodigoMarca = buscaEnLista2(listaCodigoPasilloCodigoProducto,codigoMarca,2)
                if(listaCodigoPasilloCodigoMarca != []):
                    print(listaCodigoPasilloCodigoMarca[0])
                    print("1.Si")
                    print("2.No")
                    eliminar = input("Desea eliminar el producto ")
                    if eliminar == "1":
                        print("Eliminando producto")
                        posMarcasProductos = buscaEnLista(marcasProductos,codigoMarca,2)
                        posInventario = buscaEnLista(inventarios,codigoMarca,2)
                        marcasProductos.pop(posMarcasProductos)
                        inventarios.pop(posInventario)
                        
                    else:
                        print("No se elimino el producto")
                        return -1

                    
                    
                    return -1
                else:
                    print("codigo incorrecto")
                    print("***********************")
                    print("1.volver a intentar")
                    print("2.volver al menu")
                    print("***********************")
                    opcion = input('¿digite el numero de la opcion?')
                    if(opcion == "1"):
                        continue
                    elif(opcion == "2"):
                        return -1
                    else:
                        return -1   

            else:
                print("codigo incorrecto")
                print("***********************")
                print("1.volver a intentar")
                print("2.volver al menu")
                print("***********************")
                opcion = input('¿digite el numero de la opcion?')
                if(opcion == "1"):
                    continue
                elif(opcion == "2"):
                    return -1
                else:
                    return -1            
        else:
            print("codigo incorrecto")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                return -1
            else:
                return -1
    
def ModificarProducto():
    
    mostrarLista(marcasProductos)
    while(True):
        codigoPasillo = input('¿Digite su codigo del pasillo')
        listaCodigoPasillo = buscaEnLista2(marcasProductos,codigoPasillo,0)
        mostrarLista(listaCodigoPasillo)
        
        if(listaCodigoPasillo != []):
            codigoProducto = input('¿Digite su codigo del producto')
            listaCodigoPasilloCodigoProducto = buscaEnLista2(listaCodigoPasillo,codigoProducto,1)
            mostrarLista(listaCodigoPasilloCodigoProducto)
            if(listaCodigoPasilloCodigoProducto != []):
                codigoMarca = input('¿Digite su codigo de Marca')
                listaCodigoPasilloCodigoMarca = buscaEnLista2(listaCodigoPasilloCodigoProducto,codigoMarca,2)
                if(listaCodigoPasilloCodigoMarca != []):
                    nombre =input('digite el nombre que desea')
                    precio = 0
                    while(True):
                        precio=input('¿digite el precio que desea')
                        if verificaNumero(precio)==True:
                            break
                        else:
                            print("El dato ingresado no es un numero")
                            continue       
                    posMarcasProductos = buscaEnLista(marcasProductos,codigoMarca,2)
                    posInventario = buscaEnLista(inventarios,codigoMarca,2)
                    marcasProductos[posMarcasProductos][3] = nombre
                    marcasProductos[posMarcasProductos][5] = precio
                    inventarios[posInventario][3]
                    


                    
                    
                    
                else:
                    print("codigo incorrecto")
                    print("***********************")
                    print("1.volver a intentar")
                    print("2.volver al menu")
                    print("***********************")
                    opcion = input('¿digite el numero de la opcion?')
                    if(opcion == "1"):
                        continue
                    elif(opcion == "2"):
                        return -1
                    else:
                        return -1   

            else:
                print("codigo incorrecto")
                print("***********************")
                print("1.volver a intentar")
                print("2.volver al menu")
                print("***********************")
                opcion = input('¿digite el numero de la opcion?')
                if(opcion == "1"):
                    continue
                elif(opcion == "2"):
                    return -1
                else:
                    return -1            
        else:
            print("codigo incorrecto")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                return -1
            else:
                return -1

def registrarCiente():
    global clientes
    while(True):
        cedulaNueva = input('¿Digite su cedula')
        listacliente = buscaEnLista2(clientes,cedulaNueva,0)
        
        
        if(listacliente == []):
            if (verificaNumero(cedulaNueva)):
                nombreCliente = input("Ingresa el nombre")
                celularCliente = input("Tu numero de celular")
                correoCliente = input("Tu numero de correo")
                clientes += [[cedulaNueva,nombreCliente,celularCliente,correoCliente]]
                mostrarLista(clientes)
                return -1
            else:
                print("La cedula solo puede tener numeros")
                continue
           
        else:
            print("Esa cedula ya esta registrada")
            print("***********************")
            print("1.volver a intentar")
            print("2.volver al menu")
            print("***********************")
            opcion = input('¿digite el numero de la opcion?')
            if(opcion == "1"):
                continue
            elif(opcion == "2"):
                return -1
            else:
                return -1
    

def menuAdministrador():
    global cantidadDescuento
    global porcentajeDescuento
    print("----------------------------------")
    print("Estas en el menu de administrador")
    print("*********************************")
    print("1.Mantenimiento de la Base de Datos")
    print("\ta.Insertar Producto nuevo")
    print("\tb.Eliminar un Producto")
    print("\tc.Modificar un producto de una marca,modificando el precio o el nombre")
    print("\td.Consultar Precio")
    print("\te.Consultar Descuento")
    print("\tf.Modicar el Descuento")
    print("\tg.Registrar Clientes")
    print("2.Facturar")
    print("3.Revisar góndolas")
    print("4.Verificar inventario")
    print("5.Reportes")
    print("6.Volver al menu principal")
    print("***********************")
    opcion =input('¿digite el numero de la opcion?')
    if (opcion=="1"):
        print("Mantenimiento de la Base de Datos")
    elif (opcion=="a"):
        print("Insertar Producto nuevo")
        insertarProductonuevo()
    elif (opcion=="b"):
        
        print("Eliminar un Producto")
        eliminarProducto()
        menuAdministrador()
    elif (opcion=="c"):
        print("Modificar un producto de una marca,modificando el precio o el nombre")
        ModificarProducto()
        menuAdministrador()
    elif (opcion=="d"):
        print("Consultar Precio")
        consultarPrecio()
        menuAdministrador()
    elif (opcion=="e"):
        print("Consultar Descuento")
        print("El descuento es de "+(str)(porcentajeDescuento)+"%")
        print("Se aplica despues de la factura numero "+(str)(cantidadDescuento))
        menuAdministrador()
    elif (opcion=="f"):
        print("Modicar el Descuento")
        while(True):
            CantidadFacturas=input('digite el numero de facturas requerido para aplicar descuento')
            if verificaNumero(CantidadFacturas)==True:
                cantidadDescuento =  (int)(CantidadFacturas)
                print("Se cambio a que se aplique un descuento despues de la factura numero" + (str)(cantidadDescuento))
                break
            else:
                print("El dato ingresado no es un numero")
                continue
        while(True):
            CantidadPorcentaje=input('digite el numero del descuento a aplicar')
            if verificaNumero(CantidadPorcentaje)==True:
                porcentajeDescuento =  (int)(CantidadPorcentaje)
                print("Se aplica un decuento de "+(str)(CantidadPorcentaje)+"%")
                break
            else:
                print("El dato ingresado no es un numero")
                continue
        menuAdministrador()      
    elif (opcion=="g"):
        print("Registrar Clientes")
        registrarCiente()
        menuAdministrador()
    elif (opcion=="2"):
        facturar()
    elif (opcion=="3"):
        RevisarGondolas()
    elif (opcion=="4"):
        VerificarInventario()
    elif (opcion=="5"):
        Reportes()
    elif (opcion=="6"):
        menuQuienEntra()
    else:
        print("El dato ingresado no es permitido")    
menuQuienEntra()
