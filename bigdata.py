# Langkah 1: Impor library yang dibutuhkan
# 'requests' untuk membuat permintaan HTTP (menghubungi URL)
# 'json' untuk menampilkan data JSON agar lebih rapi (opsional, tapi sangat membantu)
import requests
import json

# Langkah 2: Tentukan alamat API yang akan dihubungi
# Saya memilih 'routes_prop_stats_geo.json' dari file Word Anda,
# karena deskripsinya "berisi daftar semua rute... beserta statistik terbaru."
# Ini sepertinya data yang paling menarik dan dinamis.
API_URL = "http://data.addinsight.com/ACT/routes_prop_stats_geo.json"

print(f"Mencoba mengambil data dari: {API_URL}")

# Langkah 3: Gunakan blok 'try...except' untuk penanganan error
# Ini adalah praktik yang baik jika misalnya koneksi internet Anda terputus
# atau server sedang tidak bisa diakses.
try:
    # Mengirim permintaan GET ke URL API.
    response = requests.get(API_URL)

    # Memeriksa apakah permintaan berhasil (kode status 200 artinya 'OK').
    # Jika ada error (seperti 404 Not Found), ini akan memunculkan pengecualian.
    response.raise_for_status()

    # Mengubah respons dari format JSON (teks) menjadi objek Python (list/dictionary)
    data = response.json()

    print("Data berhasil diambil!")
    print("-" * 20)

    # Langkah 4: Proses dan tampilkan data yang diterima
    
    # Data yang diterima adalah sebuah list, kita cek dulu berapa banyak rute yang didapat.
    # Cek tipe data dan key yang tersedia
    print(f"Tipe data hasil response: {type(data)}")
    print(f"Key tersedia: {list(data.keys())}")

    # Jika data adalah dict dan ada key 'features', ambil dari sana
    if isinstance(data, dict) and "features" in data:
        routes = data["features"]
    elif isinstance(data, list):
        routes = data
    else:
        print("Format data tidak dikenali.")
        routes = []

    print(f"Ditemukan data untuk {len(routes)} rute lalu lintas.")

    if routes:
        print("\nBerikut adalah contoh data mentah untuk rute pertama:")
        print(json.dumps(routes[0], indent=2))
        print("-" * 20)

    print("\nBerikut adalah statistik lalu lintas terbaru untuk beberapa rute:")
    for rute in routes[:5]:
        # Jika GeoJSON, properties ada di rute['properties']
        props = rute.get("properties", rute)
        nama_rute = props.get("Name", "Nama tidak tersedia")
        waktu_tempuh = props.get("TT", 0)
        keterlambatan = props.get("Delay", 0)
        waktu_tempuh_menit = waktu_tempuh // 60
        waktu_tempuh_detik = waktu_tempuh % 60

        print(
            f"\n📍 Rute: {nama_rute}\n"
            f"   - Waktu Tempuh Saat Ini: {waktu_tempuh_menit} menit {waktu_tempuh_detik} detik\n"
            f"   - Keterlambatan: {keterlambatan} detik dari kondisi normal"
        )


except requests.exceptions.HTTPError as errh:
    print(f"❌ Http Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"❌ Error Koneksi: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"❌ Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"❌ Terjadi kesalahan: {err}")