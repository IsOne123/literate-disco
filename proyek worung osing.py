while True:
    print (" WELCOME TO WAROENG OSING KREATOR ")
    pesanan = []
    jumlah_pesanan = []
    harga = []
    total = 0
    while True:
        print (""" Menu Makanan\n
                1. Lalapan wader\t18.000
                2. Lalapan Lele\t20.000
                3. Lalapan Belut\t17.000
                4. Nasi Goreng\t10.000
                5. Mie Goreng\t8.000
                """)
        print("")
        while True :
            try:
                makanan = int(input("Masukkan Kode Makanan : "))
                if makanan <= 5 and makanan >= 0:
                    break
                else:
                    print ("Masukan Kode 1,2,3,4,5 aja / 0 kalo tidak pesan")
            except:
                print ("Masukan Kode 1,2,3,4,5 aja / 0 kalo tidak pesan")

        if makanan == 1:
            while True :
                try:
                    jumlah = int(input("Jumlah Lalapan wader : "))
                    break
                except:
                    print ("Hanya angka aja ya")
            pesanan.append("Lalapan Wader")
            jumlah_pesanan.append(jumlah)
            harga.append(18000 * jumlah)
            total = total + 18000 * jumlah
            
        elif makanan == 2:
            while True :
                try:
                    jumlah = int(input("Jumlah Lalapan Lele : "))
                    break
                except:
                    print ("Hanya angka aja ya")
            pesanan.append("Lalapan Lele")
            jumlah_pesanan.append(jumlah)
            harga.append(20000 * jumlah)
            total += 20000 * jumlah

        elif makanan == 3:
            while True :
                try:
                    jumlah = int(input("Jumlah Lalapan Belut : "))
                    break
                except:
                    print ("Hanya angka aja ya")
            pesanan.append("Lalapan Belut")
            jumlah_pesanan.append(jumlah)
            harga.append(17000 * jumlah)
            total = total + 17000 * jumlah

        elif makanan == 4:
            while True :
                try:
                    jumlah = int(input("Jumlah Nasi goreng : "))
                    break
                except:
                    print ("Hanya angka aja ya")
            pesanan.append("Lalapan Wader")
            jumlah_pesanan.append(jumlah)
            harga.append(18000 * jumlah)
            total += 18000 * jumlah

        elif makanan == 5:
            while True :
                try:
                    jumlah = int(input("Jumlah Mie goreng : "))
                    break
                except:
                    print ("Hanya angka aja ya")
            pesanan.append("Mie Goreng")
            jumlah_pesanan.append(jumlah)
            harga.append(8000 * jumlah)
            total = total + 8000 * jumlah

        elif makanan == 0 :
            break
        
        else:
            print ("""Pilih 1,2,3,4,5 / 0 jika tidak pesan
                   jangan yang lain""")

        while True :
            try:
                lanjut = str(input("y untuk pesan makanan / t untuk lanjut pesan minuman  : "))
            except:
                print ("Hanya angka y / t aja yaa")
            if lanjut == "t" or lanjut =="y":
                break
        if lanjut == "t":
                break
    while True:
        print("")
        print ("""Menu Minuman\n
                1. Susu D/P\t3.500 - 3.000
                2. Teh D/P\t3.000 - 2.500
                3. Jahe D/P\t4.000 - 3.000
                4. Coklat D/P\t5.000
                5. Air Putih\t0
                """)
        print("")
        while True :
            try:
                minuman = int(input("Masukkan Kode Minuman : "))
                if minuman <= 5 and minuman >= 0:
                    break
                else:
                    print ("Masukan Kode 1,2,3,4,5 aja / 0 kalo tidak pesan")
            except:
                print ("Masukan Kode 1,2,3,4,5 aja / 0 kalo tidak pesan")
           
                
        if minuman == 1:
            while True :
                try:
                    mode_minuman = str(input("d untuk dingin / p untuk panas : "))
                except:
                    print ("Hanya angka aja ya")
                if mode_minuman == "d" or mode_minuman =="p":
                    break
            if mode_minuman =="d":
                    while True :
                        try:
                            jumlah = int(input("Jumlah Susu Dingin : "))
                            break
                        except:
                            print ("Hanya angka aja ya")
                    pesanan.append("Susu Dingin ")
                    jumlah_pesanan.append(jumlah)
                    harga.append(3500 * jumlah)
                    total = total + 3500 * jumlah
            elif mode_minuman == "p":
                while True :
                    try:
                        jumlah = int(input("Jumlah Susu Panas : "))
                        break
                    except:
                        print ("Hanya angka aja ya")
                    pesanan.append("Susu Panas")
                    jumlah_pesanan.append(jumlah)
                    harga.append(3000 * jumlah)
                    total = total + 3000 * jumlah

        elif minuman == 2:
            while True :
                try:
                    mode_minuman = str(input("d untuk dingin / p untuk panas : "))
                except:
                    print ("Hanya angka aja ya")
                if mode_minuman == "d" or mode_minuman =="p":
                    break
            if mode_minuman =="d":
                    while True :
                        try:
                            jumlah = int(input("Jumlah Teh Dingin : "))
                            break
                        except:
                            print ("Hanya angka aja ya")
                    pesanan.append("Teh Dingin ")
                    jumlah_pesanan.append(jumlah)
                    harga.append(3000 * jumlah)
                    total = total + 3000 * jumlah
            elif mode_minuman == "p":
                    while True :
                        try:
                            jumlah = int(input("Jumlah Teh Panas : "))
                            break
                        except:
                            print ("Hanya angka aja ya")
                    pesanan.append("Teh Panas")
                    jumlah_pesanan.append(jumlah)
                    harga.append(2500 * jumlah)
                    total = total + 2500 * jumlah

        elif minuman == 3:
            while True :
                try:
                    mode_minuman = str(input("d untuk dingin / p untuk panas : "))
                except:
                    print ("Hanya angka aja ya")
                if mode_minuman == "d" or mode_minuman =="p":
                    break
            if mode_minuman =="d":
                    while True :
                        try:
                            jumlah = int(input("Jumlah Jahe Dingin : "))
                            break
                        except:
                            print ("Hanya angka aja ya")
                    pesanan.append("Jahe Dingin ")
                    jumlah_pesanan.append(jumlah)
                    harga.append(4000 * jumlah)
                    total = total + 4000 * jumlah
            elif mode_minuman == "p":
                    while True :
                        try:
                            jumlah = int(input("Jumlah Jahe Panas : "))
                            break
                        except:
                               print ("Hanya angka aja ya")
                    pesanan.append("Jahe Panas")
                    jumlah_pesanan.append(jumlah)
                    harga.append(3000 * jumlah)
                    total = total + 3000 * jumlah

        elif minuman == 4:
            while True :
                try:
                    mode_minuman = str(input("d untuk dingin / p untuk panas : "))
                except:
                    print ("Hanya angka aja ya")
                if mode_minuman == "d" or mode_minuman =="p":
                    break
            if mode_minuman =="d":
                    while True :
                        try:
                            jumlah = int(input("Jumlah Coklat Dingin : "))
                            break
                        except:
                            print ("Hanya angka aja ya")
                    pesanan.append("Coklat Dingin ")
                    jumlah_pesanan.append(jumlah)
                    harga.append(5000 * jumlah)
                    total = total + 5000 * jumlah
            elif mode_minuman == "p":
                    while True :
                        try:
                            jumlah = int(input("Jumlah Coklat Panas : "))
                            break
                        except:
                               print ("Hanya angka aja ya")
                    pesanan.append("Coklat Panas")
                    jumlah_pesanan.append(jumlah)
                    harga.append(5000 * jumlah)
                    total =  total + 5000 * jumlah

        elif minuman == 5:
            while True :
                try:
                    jumlah = int(input("Jumlah Air Putih : "))
                    break
                except:
                    print ("Hanya angka aja ya")
            pesanan.append("Air Putih")
            jumlah_pesanan.append(jumlah)
            harga.append(0 * jumlah)
            total = total + 0 * jumlah

        elif minuman == 0 :
            break
        
        lanjut = str(input("ingin pesan lagi y/t : "))
        if lanjut == "t":
            break

    print("")
    print ("pesanan =",pesanan)
    print ("jumlah pesanan =",jumlah_pesanan)
    print ("Harga Perpesanan =",harga)
    print ("Total Harga",total)
    print("")
    if total == 0:
        break 
    while True :
        try:
            bayar = int(input("Jumlah Uang Pembayaran = "))
            break
        except:
            print ("Hanya angka aja ya")
    if bayar > total:
        kembalian = bayar - total
        print("kembalian anda = ",total)
    elif bayar<total:
        kembalian = bayar - total
        print("Maaf ungan anda kurang = ",kembalian)
    elif bayar == total:
        print("Uang pas")
    print("")
    print("Terimakasih \nSelamat Datang Kembali\n")
        
