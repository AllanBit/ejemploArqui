'''
1. Corremos app.py
2. Iniciamos el cliente en un terminal dedicado
3. Mientras las dos aplicaciones esten corriendo, podremos observar su funcionamiento en GET y POST
'''


import requests

data = requests.get("http://127.0.0.1:5000/estudiantes")

print(data.status_code)
print(data.json())

