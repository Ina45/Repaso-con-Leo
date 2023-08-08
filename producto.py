




class producto():

    ID = 0,
    Nombre = "",
    precio = 0,
    proveedores = 0

    def __init__(self, nombre, precio, proveedores):
        self.Id = id
        self.Nombre = nombre
        self.Precio = precio 
        self.Proveedores = proveedores
        
    def MostrarDatos(self):
            print('el Id del proucto es:'+self.ID+'cuyo nombre es:'+self.Nombre+ 'su precio es:'
                  +self.precio+ 'con un proveedores:'+self.Proveedores)
     
Id = 1       
Nombre = 'piedras'
precio = 5
proveedores= 2
Panaderia = producto ( 1,"piedra", 5, 2)
Panaderia.mostrardatos() 

#para comentar control+k+c
#para descomentar control+k+u

class insumos():
    ID=0
    Nombre ='' 
    Cantidad =0 
    Precio =0

    def __init__(self,id,nombre,cantidad,precio):

        self.ID = id
        self.Nombre = nombre
        self.Cantidad = cantidad
        self.Precio=precio
def MostrarDatos (self):
        print("el id del producto es:"+self.ID+"su nombre es:"+self.Nombre+"la cantidad es :"+self.Cantidad+
              "y su precio es:"+self.Precio)    
        
class produccion_diaria ():
    ID =0 
    Fecha =0 
    Producto ="",
    Personal_responsable ="",

    def _init_(self,id,fecha,producto,personal_responsable):
        self.Id = id
        self.Fecha = fecha
        self.Producto = producto
        self.Personal_responsable = personal_responsable

class receta ():
     ID=0
     Producto="",
     Insumo="",
     Cantidad=0

     def _init_(self,id,producto,insumo,cantidad) :
        self.Id=id
        self.Producto=producto
        self.Insumo=insumo
        self.Cantidad=cantidad

class proveedores ():

    Id= 0
    Nombre="",
    Direccion= "",
    Telefono=0    

    def _init_(self,id,nombre,direccion,telefono):
        self.Id=id
        self.Nombre=nombre
        self.Direccion=direccion
        self.Telefono=telefono


     
    
        
        
