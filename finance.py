import json
import os

DATA_FILE = "finance.json"

# Load 
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("File data rusak. Membuat ulang...")
            return {"saldo": 0, "transaksi": []}
    else:
        return {"saldo": 0, "transaksi": []}

# Savedata
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Adddata
def tambah_transaksi(data, jenis, jumlah, keterangan):
    if jenis == "pemasukan":
        data["saldo"] += jumlah
    elif jenis == "pengeluaran":
        data["saldo"] -= jumlah
    data["transaksi"].append({"jenis": jenis, "jumlah": jumlah, "keterangan": keterangan})
    save_data(data)

# Viewdata
def tampilkan_transaksi(data):
    print("\nDaftar Transaksi:")
    for i, t in enumerate(data["transaksi"], 1):
        print(f"{i}. {t['jenis'].title()} - Rp{t['jumlah']} - {t['keterangan']}")
    print(f"\nTotal Saldo: Rp{data['saldo']}\n")

# Resetdata
def reset_data():
    konfirmasi = input("Apakah kamu yakin ingin mereset semua data? (y/n): ").lower()
    if konfirmasi == "y":
        data_baru = {"saldo": 0, "transaksi": []}
        save_data(data_baru)
        print("Data berhasil direset!\n")
        return data_baru
    else:
        print("Reset dibatalkan.\n")
        return load_data()

# Main program
def main():
    data = load_data()

    while True:
        print("|==================================================|")
        print("|            Manajemen Keuangan Pribadi            |")
        print("|==================================================|")
        print("|             1. Tambah Pemasukan                  |")
        print("|             2. Tambah Pengeluaran                |")
        print("|             3. Lihat Transaksi dan Saldo         |")
        print("|             4. Keluar                            |")
        print("|             5. Reset Data                        |")
        print("|==================================================|")
        
        pilihan = input("\nPilih menu (1-5):")
        
        if pilihan == "1":
            jumlah = int(input("Jumlah pemasukan: "))
            keterangan = input("Keterangan: ")
            tambah_transaksi(data, "pemasukan", jumlah, keterangan)
        elif pilihan == "2":
            jumlah = int(input("Jumlah pengeluaran: "))
            keterangan = input("Keterangan: ")
            tambah_transaksi(data, "pengeluaran", jumlah, keterangan)
        elif pilihan == "3":
            tampilkan_transaksi(data)
        elif pilihan == "4":
            print(".....")
            break
        elif pilihan == "5":
            data = reset_data()
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
