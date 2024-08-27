import requests
from config import API_URL, API_KEY

def extract_data(lat=-34.61315, lon=-58.37723):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")

if __name__ == "__main__":
    data = extract_data()
    print(data)