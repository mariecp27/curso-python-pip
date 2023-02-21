import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # Solitud tipo GET al endpoint deseado
    print(r.status_code) # Muestra el status code de la solicitud
    print(r.text) # Muestra la respuesta como String

    categories = r.json() # Muesntra la resouesta como un JSON
    for category in categories:
        print(category['name'])