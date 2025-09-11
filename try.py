print("Python di VS Code sudah jalan 🚀")

contoh_teks = 'halo semua'
print(type(contoh_teks))

a=3
print (a)
print(type(a))

a=3
a = a+4
print(a)


contoh_list = [1, 2, 3, 4, 5, 6]
print(type(contoh_list))

contoh_listkedua = ['a', 'b', 'c', 'd', 'e']
print(contoh_listkedua[3])

contoh_list.append('abc')
print(contoh_list)

contoh_list = [[1,2,3,4,5], 'a', 'b', 77]
print(contoh_list[0][1])

contoh_set =set(['d', 'i', 'b','i', 'm', 'b', 'i', 'n', 'g'])
print(contoh_set)

daftar_harga = {'apel' : 5000, 'jeruk': 8500, 'mangga' : 7800, 'duku': 6500}
print(daftar_harga['mangga'])

print(list(daftar_harga.keys()))

print(list(daftar_harga.values()))

buah_belanjaan = ['apel', 'apel', 'apel', 'mangga', 'duku']
list_harga = [daftar_harga[x] for x in buah_belanjaan]
print(list_harga)

total_harga = sum(list_harga)
print(total_harga)

dictionary = {'apel': ['iphone 11', 'airpods', 'Macbook pro',],
              'Samsung': ['Galxy note 10', 'Galxy S9', 'Galaxy watch'],
              'sony': ['Xperia 1', 'Xperia 2', 'Xperia 3']}
print(dictionary['apel'][2])

print(1+2)
print(2+3)
print(3+4)

nama = 'hita'
print(f'Nama peserta adalah {nama}. Peserta tersebut telah tercatat')

nilai_1 = 90
nilai_2 = 100
nilai_3 = 80
print(f'Rata-rata nilai: {(nilai_1 + nilai_2 + nilai_3 / 3)} poin')

print(buah_belanjaan)
print(len(buah_belanjaan))

def luas_keliling(panjang, lebar):
    luas = panjang*lebar
    keliling = 2* (panjang+lebar)
    return luas, keliling

print(luas_keliling(10, 5))
print(luas_keliling(10, 5)[0])
    
jwb_luas, jwb_keliling =luas_keliling(7,4)
print(jwb_luas)
print(jwb_keliling)

def luas_keliling(panjang, lebar):
    luas = panjang*lebar
    keliling = 2* (panjang+lebar)

print('Luas Persegi Panjang:'(luas))
print('keliling persegi panjang:'(keliling))
return luas, keliling

