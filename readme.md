# Hava Kalitesi API Kullanımı

Bu proje, OpenWeatherMap API'sini kullanarak belirli bir coğrafi konum için hava kalitesi verilerini çekmekte ve hava kalitesi indeksine (AQI) göre tavsiyeler sunmaktadır. Proje, Python ile yazılmıştır ve kullanımı oldukça basittir.

## Gereksinimler

Projenin çalışması için aşağıdaki gereksinimlerin karşılanması gerekmektedir:

- **Python 3.x**: Python programlama dili .
- **requests** kütüphanesi: HTTP istekleri yapmak için kullanılır. Kurulum için aşağıdaki komutu kullanabilirsiniz:

    ```bash
    pip install requests
    ```

## Dosya Yapısı

Projenin dosya yapısı aşağıdaki gibidir:

- **`config.json`**: API anahtarı ve konum bilgilerini içeren yapılandırma dosyası.
- **`main.py`**: Hava kalitesi verilerini çekmek ve işlemek için gerekli olan Python kodunu içeren dosya.

## config.json

Bu dosya, API anahtarı ve konum bilgilerini içerir. Aşağıdaki gibi yapılandırılmalıdır:

```json
{
    "api_key": "YOUR_API_KEY",
    "lat": "YOUR_LATITUDE",
    "lon": "YOUR_LONGITUDE"
}
