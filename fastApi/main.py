#importamos la biblioteca fastapi que instalamos con pip
from fastapi import FastAPI
#creamos una instancia de la clase fastapi
app = FastAPI()

#--------------------------------------------------------------
#POST: para crear datos
#GET: para obtener datos
#PUT: para actualizar datos
#DELETE: para eliminar datos
#--------------------------------------------------------------

@app.get("/")
#async: puede recibir varias peticiones al mismo tiempo sin bloquear el servidor, es decir, puede manejar varias solicitudes simultáneamente sin esperar a que una se complete antes de atender la siguiente
async def root():
    return {"clase": "hola parcero"}

#----------------------------------

#ls me dice donde estoy ubicado
#cd me lleva a la carpeta que le indique
#cd. me lleva a la carpeta anterior

#-------------------------------------


@app.get ("/ADSO")
async def adso ():
    return {"clase":"clase 506"}


#-----------------------------------------

@app.get ("/ADSO/506")
async def adso506 ():
    return {"clase":"clase 506 de ADSO"}

@app.get ("/musica")
async def musica ():
    return {"musica":"me gusta la musica de los 80s"}

@app.get ("/peliculas")
async def peliculas ():
    return {"peliculas":"me gusta las peliculas de terror"}

@app.get ("/mascota")
async def mascota ():
    return {"mascota": "gatos gordos"}

