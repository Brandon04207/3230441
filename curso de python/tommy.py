Pesos = float (input( "ingrese cuantos pesos tiene: " ))
dolar = float (input( "ingrese cuantos dolares tiene:" ))
# float para que convierta la variable en numero entero con decimal 

primerPago = 15
segundoPago = 4000
tercerPago = 122000
cuartoPago = 26
quintoPago = 7
sextoPago = 35000
septimoPago = 14000
octavoPago = 26000
#le doy una variable a cada uno de los gastos 

sobrantePeso = Pesos -(segundoPago + tercerPago + sextoPago + septimoPago + octavoPago)
sobranteDolar = dolar - ( primerPago + cuartoPago + quintoPago)

 
if sobranteDolar >= 0:
    print (" lo que quedo en pesos fue", sobranteDolar )
    
else:
    print (" lo que quedo deviendo en pesos fue", sobranteDolar )
    
if sobrantePeso >= 0:
    print (" lo que quedo en pesos fue", sobrantePeso)

else:
    print (" lo que quedo devieando en pesos fue", sobrantePeso )