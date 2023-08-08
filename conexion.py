import mysql.connector
import random

class Conectar_BD():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host= "127.0.0.1",
                port= 3306, 
                user= "root",
                password= "usain10879",
            
                db= "practica_con_leo",
                auth_plugin='mysql_native_password'
            )
            if self.conexion.is_connected():
                print("LA CONEXION FUE EXITOSA")
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")
            
        finally:
            if self.connexion.is_connected():
                self.cenexion.close()
                print("LA CONEXION FUE CERRADA")  
                
    def Insetar_Producto(self, Id, nombre, precio, proveedores,):
        if self.conexion.is_connected():
            try:
                cursor = self. conexion.cursor()
                sentenciaSQL = "INSERT INTO Productos values (%s,%s,%s,%s,)" 
                data = (Id, nombre, precio, proveedores)
                cursor.execute(sentenciaSQL,data) 
                cursor.Conexion.commit()
                cursor.Conexxion.close()
            
            except mysql.connetor.Error as descripcionDelError:
                print("¡Hubo un error al intentar conectar la base de datos", descripcionDelError)
                
    def Listado_De_Productos(Self):
        if Self.conexion.is_conneted():
            try:
                cursor = Self. conexion.cursor()
                sentenciaSQL = "SELECT * FROM Productos"
                cursor.execute(sentenciaSQL)
                resultados =cursor.fetchall()
                cursor.Conexion.close()
                return resultados
            except mysql.connector.Error as descripcionDelError:
                print("¡Hubo un Error al intentar conectar la base de datos", descripcionDelError)
                
                
                
                
    
        
            
            
            