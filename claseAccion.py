import datetime
from datetime import datetime as dt

class accion:
    #parametros
    def __init__(self,nemotecnico,ultimo_precio=0):
        self.nemotecnico=nemotecnico
        self.ultimo_precio=ultimo_precio
        x = datetime.datetime.now()
        self.fecha=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
        self.precios_historicos = {
            self.fecha: self.ultimo_precio
        }
        
    def actualizar_ultimo_precio(self,precio):
        if (type(precio)==int or type(precio)==float):
            for ultimaFecha in self.precios_historicos:
                pass
            self.precios_historicos[ultimaFecha]=float(precio)
        else: 
            print(type(precio))
            print("No se puede ingresar caracteres '" , precio, "' en el precio ")
            
    def agregar_precio_historico(self,fechaNueva,precioNuevo):
        self.precios_historicos[fechaNueva]=float(precioNuevo)
    
    def obtener_precio_para_fecha(self,fechaConsulta):
        if fechaConsulta in self.precios_historicos:
            print("El valor de la fecha es : ", self.precios_historicos[fechaConsulta])
        else:
            print("El valor de la fecha es : " , 0)
            
    def obtener_rentabilidad(self):
        rentabilidad=1
        if (self.precios_historicos=={}):
            rentabilidad=0
        ct=0 #para generar el primer ingreso
        #calculo de las fechas mas antiguas y mas nuevas
        for x in self.precios_historicos:
            if(rentabilidad==0):
                print("rentabilidad=",rentabilidad)
                break
            ingresoFecha = dt.strptime(x, "%Y-%m-%d")
            if(ct==0):
                ct=ct+1
                primeraFecha = dt.strptime(x, "%Y-%m-%d")
                continue
            if (primeraFecha>ingresoFecha):
                ultimaFecha=primeraFecha
                primeraFecha=ingresoFecha
            else:
                if(ultimaFecha<ingresoFecha):
                    ultimaFecha=ingresoFecha
        #se devuelve su respectivo formato a las fechas
        primeraFecha= primeraFecha.strftime("%Y")+"-"+primeraFecha.strftime("%m")+"-"+primeraFecha.strftime("%d")
        ultimaFecha= ultimaFecha.strftime("%Y")+"-"+ultimaFecha.strftime("%m")+"-"+ultimaFecha.strftime("%d")
        
        #funciones para definir si se usa el ultimo valor ingresado o de la ultima fecha
        if(self.precios_historicos[ultimaFecha]==0 or ultimaFecha==False):
            for x in self.precios_historicos:
                if (self.precios_historicos[x]!= 0) :
                    ultimoPrecio=self.precios_historicos[x]
                    print(ultimoPrecio)
            rentabilidad = (ultimoPrecio/self.precios_historicos[primeraFecha]) -1
            print("rentabilidad=",rentabilidad)
        else:
            if(self.precios_historicos[primeraFecha]!=0):
                rentabilidad = (self.precios_historicos[ultimaFecha]/self.precios_historicos[primeraFecha])-1
            else:
                rentabilidad = 0
            print("rentabilidad=",rentabilidad)

#programa principal
accion = accion("GOOGL", 120.01 )
print("creacion de accion")
print(accion.precios_historicos)

accion.actualizar_ultimo_precio(13.4)
print("accion modificada")
print(accion.precios_historicos)

accion.agregar_precio_historico( "2019-07-20", 13.067 )
print("creacion de nuevo precio")
print(accion.precios_historicos)

print("Obteniendo precio segun fecha")
accion.obtener_precio_para_fecha("2019-07-20")

print("rentabilidad de la accion")
accion.obtener_rentabilidad()