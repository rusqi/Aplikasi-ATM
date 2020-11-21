import random
import datetime
from customer import Customer

nasabah_atm = Customer("rusqi", 4444)

while True:
    id = int(input("Masukkan Nomor Pin: "))
    trial = 0

    while (id != int(nasabah_atm.checkPin()) and trial < 3):
        id = int(input("Nomor pin Anda Salah. Masukkan nomor lagi: "))
        trial += 1
        print(trial)

    if trial == 3:
        print("Error. Silahkan ambil kartu dan coba lagi..")
        exit()
    else:
        pass

    while True:
        print(' ' ' ')
        print("Selamat Datang!!")
        print(
            "pilihan Menu Utama: (0: Cek Saldo 1: Debet 2: Simpan 3: Ganti Pin 4: Keluar)"
        )
        user_input = int(input("Masukkan angka (0-4): "))

        if user_input == 0:
            print(nasabah_atm.checkBalance())
            break
        else:
            pass

        if user_input == 1:
            nominal = int(input("masukkan Nominalnya yang akan di debet: "))
            print(nasabah_atm.withdrawBalance(nominal))
            break
        else:
            pass

        if user_input == 2:
            nominal = int(input("masukkan Nominal yang akan di deposit: "))
            print('Saldo anda adalah: ' +
                  str(nasabah_atm.depositBalance(nominal)))
            break
        else:
            pass

        if user_input == 3:
            newCustPin = int(input("masukkan nomor pin baru: "))
            print("nomor pin Anda telah berhasil diubah dari " +
                  str(nasabah_atm.custPin) + " menjadi " + str(newCustPin))
        else:
            pass

        if user_input == 4:
            print(datetime.datetime.now())
            print(random.randint(100000, 1000000))
            exit()
        else:
            pass

        if user_input < 0 or user_input > 4:
            print('Tolong Masukkan nomor yang benar')
        else:
            pass