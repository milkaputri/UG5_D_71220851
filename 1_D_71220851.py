def ganti_kata(kalimat, cari, ganti):
    pecah = kalimat.split(',')
    for i in range(kalimat):
        if pecah == cari:
            cari = ganti
    baru = ' '.join(pecah)
    return baru
kalimat = input('Masukan kalimat : ')
cari = input('Kata yang dicari : ')
ganti = input('Diganti menjadi : ')
ganti_kata(kalimat,cari,ganti)