import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

list_data = []

def show_menu():
    clear_screen()
    print("===Aplikasi Kontak===")
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[0] Exit")
    print("--------------------------")


    menu = input("Pilih Menu: ")
    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()
    elif menu == '4':
        menu4()
    elif menu == '0':
        print("Terimakasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukkan tidak ada, Masukkan pilihan yang tersedia")
        kembali()

list_data = {}

def menu1():
    print('NIM  ||  Nama')
    if len(list_data) <= 0:
        print('Data Masih Kosong')
    else:
        for nim, nama in list_data.items():
            print(f"{nim}. {nama}")
    kembali()

def menu2():
    nim = input("Masukkan NIM Anda: ")
    nama = input("Masukkan Nama Anda: ")
    list_data[nim] = nama
    print("Data Berhasil Ditambahkan")
    kembali()

def menu3():
    nim = input("Masukkan NIM Anda: ")
    if nim in list_data:
        nama_baru = input('Masukkan nama Baru: ')
        list_data[nim] = nama_baru
        print('Nama Anda Telah Dirubah')
    else:
        print("NIM tidak ditemukan")
    kembali()

def menu4():
    nim = input("Masukkan NIM yang Ingin Dihapus: ")
    if nim in list_data:
        del list_data[nim]
        print("Data Berhasil Dihapus")
    else:
        print("NIM tidak ditemukan")
    kembali()

def kembali():
    print("\n")
    input("Tekan Enter untuk kembali")
    show_menu()

while(True):
    show_menu()