def hitung_mobil(jumlahSol, jumlahSur, jumlahJog, jumlahMag):
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0
    while True:
        asal = input(f'Masukan asal mobil (ketik "done" untuk keluar): ')
        if asal.lower() == 'Solo':
            jumlahSol += 1
        elif asal.lower() == 'Surabaya':
            jumlahSur += 1
        elif asal.lower() == 'Jogja':
            jumlahJog += 1
        elif asal.lower() == 'Magelang':
            jumlahMag += 1
        elif asal.lower() == 'Done':
            break
        else:
            break
    print(f'Jumlah Mobil Solo: {jumlahSol}')
    print(f'Jumlah Mobil Surabya: {jumlahSur}')
    print(f'Jumlah Mobil Jogja: {jumlahJog}')
    print(f'Jumlah Mobil Magelang: {jumlahMag}')