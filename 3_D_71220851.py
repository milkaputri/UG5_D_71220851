import math
while True:
    jarak_awal = int(input('Masukan jarak awal (Dalam meter): '))
    if jarak_awal.lower() == 'stop' or 'berhenti':
        print('Program dihentikan')
        break
    sudut_el5 = input('Masukan sudut elevasi pada menit ke-5 (dalam derajat): ')
    sudut_el6 = input('Masukan sudut elevasi pada menit ke-6 (dalam derajat): ')
    heli_awal = jarak_awal * math.tan(sudut_el5)
    heli_akhir = (jarak_awal * math.tan(sudut_el6)) - (math.tan(sudut_el5))
    selisih_heli = heli_akhir * math.tan(sudut_el6)
    selisih_ketinggian = heli_akhir - heli_awal
    print(f'Selisih ketinggian done saat menit ke-5 dan ke-6 adalah {selisih_ketinggian} meter\n Program dihentikan')
