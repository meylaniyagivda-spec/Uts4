import fungsi

while True:
    print("\n=== MENU BANGUN RUANG ===")
    print("1. Kubus")
    print("2. Balok")
    print("3. Prisma Segitiga")
    print("4. Tabung")
    print("5. Kerucut")
    print("6. Bola")
    print("7. Limas Segiempat")
    print("8. Limas Segitiga")
    print("9. Prisma Segiempat")
    print("10. Prisma Segilima")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        s = float(input("Masukkan sisi: "))
        print("Volume:", fungsi.volume_kubus(s))
        print("Luas:", fungsi.luas_kubus(s))

    elif pilihan == "2":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        print("Volume:", fungsi.volume_balok(p, l, t))
        print("Luas:", fungsi.luas_balok(p, l, t))

    elif pilihan == "3":
        a = float(input("Alas segitiga: "))
        ts = float(input("Tinggi segitiga: "))
        tp = float(input("Tinggi prisma: "))
        print("Volume:", fungsi.volume_prisma_segitiga(a, ts, tp))

    elif pilihan == "4":
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        print("Volume:", fungsi.volume_tabung(r, t))

    elif pilihan == "5":
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        print("Volume:", fungsi.volume_kerucut(r, t))

    elif pilihan == "6":
        r = float(input("Jari-jari: "))
        print("Volume:", fungsi.volume_bola(r))

    elif pilihan == "7":
        s = float(input("Sisi alas: "))
        t = float(input("Tinggi limas: "))
        print("Volume:", fungsi.volume_limas_segiempat(s, t))

    elif pilihan == "8":
        a = float(input("Alas segitiga: "))
        ts = float(input("Tinggi segitiga: "))
        tl = float(input("Tinggi limas: "))
        print("Volume:", fungsi.volume_limas_segitiga(a, ts, tl))

    elif pilihan == "9":
        s = float(input("Sisi alas: "))
        t = float(input("Tinggi prisma: "))
        print("Volume:", fungsi.volume_prisma_segiempat(s, t))

    elif pilihan == "10":
        la = float(input("Luas alas segilima: "))
        t = float(input("Tinggi prisma: "))
        print("Volume:", fungsi.volume_prisma_segilima(la, t))

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")