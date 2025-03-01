input1 = input("Masukkan bilangan pertama: ")
input2 = input("Masukkan bilangan kedua: ")
input3 = input("Masukkan bilangan ketiga: ")

try:
    a = int(input1)
    b = int(input2)
    c = int(input3)

    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    else:
        print("Terbesar: ", c)
except :
    print("Input yang Anda masukkan salah.Silahkan coba lagi!")