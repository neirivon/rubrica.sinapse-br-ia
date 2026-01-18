import googlemaps
import json
from datetime import datetime

# Configure sua API KEY aqui
API_KEY = "AIzaSyACQrTf33HFRxgsEv1VZSQQ-8nn93xcevs" 
gmaps = googlemaps.Client(key=API_KEY)

# Pontos Chave (Mesmos do seu GPX)
origin = "-18.9579529,-48.2299539" # Casa
destination = "-18.7645467,-48.2886511" # IFTM
waypoints = [
    "-18.9586936,-48.2315737", # Ponto Abelardo
    "-18.9375088,-48.2299736", # Terminal Sta Luzia
    "-18.8850513,-48.2540238"  # Terminal Umuarama
]

# Solicita a rota real (Driving mode segue as ruas)
directions_result = gmaps.directions(
    origin,
    destination,
    waypoints=waypoints,
    mode="driving",
    departure_time=datetime.now()
)

# Extrai apenas o que interessa: a geometria da linha (Polyline) decodificada
rota_pontos = []

# A API retorna 'legs' (trechos entre paradas). Vamos unir tudo.
if directions_result:
    for leg in directions_result[0]['legs']:
        for step in leg['steps']:
            # Decodifica a polilinha de cada passo
            # O googlemaps lib já faz isso, ou pegamos start/end location
            # Para alta precisão, usamos a polyline do step
            path = googlemaps.convert.decode_polyline(step['polyline']['points'])
            for point in path:
                rota_pontos.append([point['lat'], point['lng']])

    # Salva em JSON para o Streamlit usar
    with open("rota_detalhada_google.json", "w") as f:
        json.dump(rota_pontos, f)
    print(f"✅ Rota salva com {len(rota_pontos)} pontos de geometria real!")
else:
    print("Erro na API")
