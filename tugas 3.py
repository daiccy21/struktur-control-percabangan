try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if 1 <= bulan <= 12:
        hari = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print("Jumlah hari:", hari[bulan - 1])
    else:
        print("Bulan tidak valid! (1-12)")
except:
    print("Input salah! Masukkan bilangan bulat.")