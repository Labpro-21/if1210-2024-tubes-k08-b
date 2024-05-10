import os
import time

# Fungsi untuk membuat sebuah nomor acak
def LCG(a, c, m):
    seed = int(os.getpid()*123 + time.time()*45) 
    x2 = (a * seed + c) % m # Rumus Dasar LCG
    return x2
# Seed ditentukan menggunakan process id dan time agar selalu bervariasi
# *123, *45 hanya untuk menambah kerandoman

# Fungsi untuk memastikan bahwa nomor acak yang didapat berada pada range yang ditentukan
def GenerateNumber(x2,num_range):
    a = 48271
    c = 0
    m = 2**31 - 1
    # Nilai-nilai diatas diapakai dalam C++11 dalam fungsi minstd_rand
    x2 = (a * x2 + c) % m
    return int((x2 / (m - 1)) * (num_range[1] - num_range[0]) + num_range[0])
# Dapet formula dari yt :)

# Fungsi yang digunakan untuk mensimplifikasi sehingga hanya perlu menyertakan batas-batasnnya
def RNG(x,y):
    a = 48271
    c = 0
    m = 2**31 - 1
    return GenerateNumber(LCG(a,c,m),[x,y])