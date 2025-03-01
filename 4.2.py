input_bilangan = input("Masukkan suatu bilangan: ")
try:
    bilangan = int(input_bilangan)
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    else:
        print("Nol")
except ValueError:
    print("Input yang Anda masukkan salah.Silahkan coba lagi !")