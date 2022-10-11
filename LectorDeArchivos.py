
def validaExistencia(i,lista,llave):
    j = 0
    esta = False
    while(j<len(lista)):
        if(lista[j][i] == llave):
            esta = True
            break
            
        else:
            esta = False
            
        j+= 1
    return esta
    


def lector(ruta,seccionLlave):
    archivo = open(ruta,"r")
    textoArchivo = archivo.read()
    seccionLectura = "";
    ListaCompleta = []
    sublista = []
    i = 0
    numeroSeccion = seccionLlave
    ignorar = False
    while(i < len(textoArchivo)):
        if(textoArchivo[i] == "\n"):
            if(ignorar == False):
                sublista += [seccionLectura]
                ListaCompleta += [sublista]
                sublista = []
                seccionLectura = ""
                numeroSeccion = 0
            else:
                sublista = []
                seccionLectura = ""
                numeroSeccion = 0
                ignorar = False
        elif(textoArchivo[i] == ";"):
            if(numeroSeccion == seccionLlave):
                if(validaExistencia(numeroSeccion,ListaCompleta,seccionLectura)== True):
                    i +=1
                    ignorar = True
                    sublista = []
                    seccionLectura = ""
                    numeroSeccion = 0
                    continue
            if(ignorar == False):
                sublista += [seccionLectura]
                seccionLectura = ""
                numeroSeccion +=1
        else:
            seccionLectura += textoArchivo[i]
        i+= 1
    if(textoArchivo[len(textoArchivo)-1] != "\n" and ignorar == False):
        sublista += [seccionLectura]
        ListaCompleta += [sublista]
        
    return ListaCompleta

def CargarPasillos():
    pasillos = lector("Archivos/Pasillos.txt",0);
    return pasillos

def CargarProductospasillo(pasillos):
    listaSinRevisar = lector("Archivos/ProductosPasillos.txt",1)
    listaRevisada = []
    i = 0
    while(i < len(listaSinRevisar)):
        if(validaExistencia(0,pasillos,listaSinRevisar[i][0]) == True):
            listaRevisada += [listaSinRevisar[i]]
        i += 1
    return listaRevisada

def CargarMarcaproductos(productosPasillo):
    listaSinRevisar = lector("Archivos/MarcasProductos.txt",2)
    listaRevisada = []
    i = 0
    while(i < len(listaSinRevisar)):
        if(validaExistencia(0,productosPasillo,listaSinRevisar[i][0]) == True and validaExistencia(1,productosPasillo,listaSinRevisar[i][1])):
            
            listaRevisada += [listaSinRevisar[i]]
        i += 1
    return listaRevisada

def CargarClientes():
    clientes = lector("Archivos/Clientes.txt",0);
    return clientes

def CargarInventario():
    inventario = lector("Archivos/Inventario.txt",2)
    return inventario

def CargarAdministradores():
    administradores = lector("Archivos/Administradores.txt",0);
    return administradores





