# saya punya sederet angkat int 1 - 50
# angka tersebut 1-50 di looping
# setiap angka yang merupakan kelipatan dari angka 3, di ganti dengan tulisan "tak"
# setiap angka kelipatan 5, di ganti dengan tulisan "tik"
# setiap angka yang merupakan kelipatan 3&5, di ganti dengan tulisan "taktik"

# dikumpulkan minggu depan sebelum kelas dimulai
# kirim japri ke telegram bang uno dan mention di grup

# output tugas: 
# 1
# 2
# tak
# 4
# tik
# tak
# 7
# 8
# tak
# tik

for angka in range(1, 51):
    if angka % 3 == 0 and angka % 5 == 0:
        print("taktik")
    elif angka % 3 == 0:
        print("tak")
    elif angka % 5 == 0:
        print("tik")
    else:
        print(angka)