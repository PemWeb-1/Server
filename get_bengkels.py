import requests

# URL endpoint untuk mendapatkan daftar semua bengkel
url = 'http://127.0.0.1:5000/get_bengkels'

# Mengirim permintaan GET untuk mendapatkan data bengkel
response = requests.get(url)

# Memeriksa kode status respons
if response.status_code == 200:
    # Data bengkel dalam format JSON
    bengkels = response.json()
    # Menampilkan daftar bengkel
    for bengkel in bengkels:
        print(f'Nama: {bengkel["nama"]}, Latitude: {bengkel["latitude"]}, Longitude: {bengkel["longitude"]}')
else:
    print('Gagal mendapatkan data bengkel.')
