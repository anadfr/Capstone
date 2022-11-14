# start

import os
os.system('cls')

def menu():
    global pilihanmenu
    print('''
1. Tampilkan Isi PIPA
2. Ubah Isi PIPA
3. Tambahkan Aset Baru ke PIPA
4. Hapus Aset dari PIPA
5. Keluar Program
''')
    pilihanmenu=str(input(f'{masukan()}'))

def masukan():
    return 'Masukan angka sesuai daftar diatas untuk melakukan langkah yang diinginkan : '

asetlist={
    5:['iWatch',87],
    1:['iPad',43],
    3:['iPhone',251],
    2:['MacBook',127]
    }

def sortaset():
    global asetsort
    asetsort={key:val for key,val in sorted(asetlist.items(), key=lambda ele:ele[0])}

def printall():
    print('\nID Aset\tNama Aset\tJumlah Aset')
    for k,v in asetsort.items():
        print(f'{k}\t{v[0]}\t\t{v[1]}')      

def invalid():
    print('\nInput yang diberikan tidak valid, silahkan coba lagi')

def displayaset():
    sortaset()
    while True:
        pilihansubmenu=str(input(f'''
1. Tampilkan Seluruh Isi PIPA
2. Pilih Aset Untuk Ditampilkan
3. Kembali ke Menu Awal

{masukan()}'''))
        if pilihansubmenu=='1':
            if len(asetsort)==0:
                print('\nAset pada PIPA Kosong')
            else:
                printall()
            continue
        elif pilihansubmenu=='2':
            if len(asetsort)==0:
                print('\nAset pada PIPA Kosong')
            else:
                inputaset=(input('Masukan ID Aset untuk ditampilkan : '))
                try:
                    if int(inputaset) in asetsort.keys():
                        print('\nID Aset\tNama Aset\tJumlah Aset')
                        print(f'{inputaset}\t{asetsort[int(inputaset)][0]}\t\t{asetsort[int(inputaset)][1]}')
                    else:
                        print('\nID Aset tidak terdaftar pada PIPA, silahkan coba lagi')
                except ValueError:invalid()
        elif pilihansubmenu=='3':
            break
        else:
            invalid()
            continue

def ubahaset():
    while True:
        ubahinput=str(input(f'''
Apakah anda ingin melanjutkan mengubah isi aset PIPA?
1. Lanjut ubah aset PIPA
2. Kembali ke Menu Awal

{masukan()}'''))
        if ubahinput=='1':
            try:
                idinput=int(input('Masukan ID Aset yang ingin diubah : '))
                if idinput in asetlist.keys():
                    idinput2=str(input(f'''
ID Aset {idinput} bernama '{asetlist[idinput][0]}' berjumlah sebanyak {asetlist[idinput][1]}.
Apa yang ingin anda ubah dari aset ?
1. Nama Aset
2. Jumlah Aset

{masukan()}'''))
                    if idinput2=='1':
                        namanew=str(input('Masukan nama aset baru : '))
                        while True:
                            check=input(f"\nKonfirmasi perubahan nama aset '{asetlist[idinput][0]}' menjadi '{namanew}' ? (Y/N) ")
                            if check.upper()=='Y':
                                asetlist[idinput][0]=namanew
                                print('Perubahan nama aset berhasil dilakukan')
                                break
                            elif check.upper()=='N':
                                print('Perubahan nama aset dibatalkan')
                                break
                            else: invalid()
                    elif idinput2=='2':
                        while True:
                            jumlahin=str(input('\nKetik + untuk menambah jumlah aset atau - untuk mengurangi jumlah aset : '))
                            if jumlahin=='+':
                                kurang=0
                                tambah=int(input('Berapa banyak aset untuk ditambahkan ? '))
                                break
                            elif jumlahin=='-':
                                tambah=0
                                kurang=int(input('Berapa banyak aset untuk dikurangi ? '))
                                break
                            else: invalid()
                        while True:
                            fin=str(input('Konfirmasi operasi perubahan jumlah aset ? (Y/N) '))
                            if fin.upper()=='Y':
                                asetlist[idinput][1]+=tambah
                                asetlist[idinput][1]-=kurang
                                if asetlist[idinput][1]==0:
                                    del asetlist[idinput]
                                    sortaset()
                                print('Jumlah aset berhasil diubah')
                                break
                            elif fin.upper()=='N':
                                break
                            else:invalid()
                else:print('ID Aset tidak terdaftar dalam PIPA')
            except ValueError:invalid()
        elif ubahinput=='2':
            break
        else:invalid()

def tambahaset():
    while True:
        try:
            submenu=int(input(f'''
Apakah anda ingin lanjut menambahkan aset baru ?
1. Lanjut tambah aset baru
2. Kembali ke Menu Awal

{masukan()}'''))
            if submenu==1:
                idin=int(input('Masukan ID Aset baru untuk ditambahkan : '))
                if idin in asetlist.keys():
                    print('ID Aset telah terdaftar, silahkan ulangi')
                else:
                    namain=str(input('Masukan Nama Aset baru untuk ditambahkan : '))
                    jumlahin=int(input(f'Masukan Jumlah Aset {namain} untuk ditambahkan : '))
                    fin=str(input(f"Konfirmasi penambahan aset baru bernama '{namain}' sebanyak {jumlahin} dengan ID {idin} ? (Y/N) "))
                    if fin.upper()=='Y':
                        asetlist.update({idin:[namain,jumlahin]})
                        sortaset()
                        print('Aset baru berhasil ditambahkan ke PIPA')
                        break
                    elif fin.upper()=='N':
                        continue
                    else:invalid()
            elif submenu==2:
                break
        except ValueError:invalid()

def delaset():
    while True:
        try:
            submenu=int(input(f'''
Apakah anda ingin lanjut menghapus aset dari PIPA ?
1. Lanjut hapus aset PIPA
2. Kembali ke Menu Awal

{masukan()}'''))
            if submenu==1:
                hapusin=int(input('Masukan ID Aset untuk dihapus dari PIPA : '))
                if hapusin in asetlist.keys():
                    while True:
                        fin=str(input(f'Konfirmasi penghapusan aset bernama {asetlist[hapusin][0]} sebanyak {asetlist[hapusin][1]} ? (Y/N) '))
                        if fin.upper()=='Y':
                            del asetlist[hapusin]
                            print('Aset telah berhasil dihapus dari PIPA')
                            break
                        elif fin.upper()=='N':
                            break
                elif hapusin not in asetlist.keys():
                    print('ID Aset tidak terdaftar pada PIPA')
            elif submenu==2:
                break
        except ValueError:invalid()

# main loop

print('Selamat Datang di Program Inventaris Penyimpanan Aset (PIPA)')
os.system("pause")
t=True
while t:
    menu()
    if pilihanmenu=='1':
        displayaset()
    elif pilihanmenu=='2':
        ubahaset()
    elif pilihanmenu=='3':
        tambahaset()
    elif pilihanmenu=='4':
        delaset()
    elif pilihanmenu=='5':
        while True:
            keluar=input('Apakah anda yakin ingin keluar dari program ? (Y/N) ')
            if keluar.upper()=='Y':
                print('Anda telah keluar dari program. Terima kasih.')
                t=False
                break
            elif keluar.upper()=='N':
                break
    else:invalid()