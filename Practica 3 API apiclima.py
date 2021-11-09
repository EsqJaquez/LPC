import requests, json

apikey = input("Introduce tu api key: ")
 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
ciudad = input("Introduce la ciudad : ")

url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + apikey + "&q=" + ciudad
 

aaa= requests.get(url)
 
x = aaa.json()
if x["cod"] != "404":
 
    
    y = x["main"]
 
   
    temperatura = y["temp"] -273.15
 
   
    presion = y["pressure"]
 
    
    humedad = y["humidity"]


    sensacion = y["feels_like"] -273.15
 
    
    z = x["weather"]
 
    
    descripcion = z[0]["description"]
 
 
    print(" Temperatura (kelvin) = " +
                    str(temperatura) +
          "\n presion amosferica (hPa) = " +
                    str(presion) +
          "\n humedad (porcentaje) = " +
                    str(humedad) +
	  "\n sensacion = " +
                    str(sensacion) +
          "\n descripcion = " +
                    str(descripcion))
 
else:
    print(" Ciudad no encontrada ")
