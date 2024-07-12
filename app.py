import requests
import json

def getconfig(filename="config.json"):
    with open (filename,'r') as configfile:
        config=json.load(configfile)
        return config

def getairquality(api_key,lat,lon):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'
    response=requests.get(url)
    data=response.json()
    return data

def aqi_advice(aqi):
    if aqi == 1:
        return "Hava kalitesi iyi. Dışarıda zaman geçirmek için güvenli."
    elif aqi == 2:
        return "Hava kalitesi kabul edilebilir. Hassas gruplar dikkatli olmalı."
    elif aqi == 3:
        return "Hava kalitesi orta düzeyde. Hassas gruplar uzun süre dışarıda kalmaktan kaçınmalı."
    elif aqi == 4:
        return "Hava kalitesi kötü. Hassas gruplar dışarıda kalmamalı, diğerleri dikkatli olmalı."
    elif aqi == 5:
        return "Hava kalitesi çok kötü. Herkes dışarıda kalmaktan kaçınmalı."
    else:
        return "Geçersiz AQI değeri."

def main():
    config = getconfig()  
    api_key = config['api_key']
    lat = config['lat']
    lon = config['lon']
    
    air_quality_data = getairquality(api_key, lat, lon)
    
    aqi = air_quality_data['list'][0]['main']['aqi']
    
    print(f"Hava Kalitesi İndeksi (AQI): {aqi}")
    print(aqi_advice(aqi))

if __name__ == "__main__":
    main()