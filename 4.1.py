input_suhu = input("Masukkan suhu tubuh: ")
try:
    suhu = int(input_suhu)
    if suhu > 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except:
    print("Input yang Anda masukkan salah. Silahkan coba lagi!")

