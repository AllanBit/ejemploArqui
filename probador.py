import requests


#----------------------APIs para probar--------------------------
#http://ip-api.com/json/          Endpoints: /
#https://catfact.ninja/           Endpoints: /fact    /facts
#https://jsonplaceholder.typicode.com/       Endpoints: /posts  /comments  /albums  /photos  /todos  /users
#https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true     Endpoint incluido
#https://timeapi.io/api/time/current/zone?timeZone=America%2FGuatemala       Enpoints: incluido



#Solo para usar la API de clima
'''
lat = 14.63 #Se obtiene con la primer api    ["lat"]
lon = -90.55 #Se obtiene con la primer api   ["lon"]

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Python script)",
    "Accept": "application/json"
}

res = requests.get(url, headers=headers)
print(res.json()) #Formateamos lo recibido en formato JSON para poder usarlo
'''



url = "https://catfact.ninja/fact"  #Cambiamos el URL con la API que requerimos
data = requests.get(url) #Hacemos la peticion con requests de tipo get
print(data.json()) #Formateamos lo recibido en formato JSON para poder usarlo
