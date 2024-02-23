# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:04:10 2024

@author: EMİNE
"""


class Library:
    def __init__(self):
        
        self.file = open("books.txt", "a+")  # "a+" kipi dosyayı okuma ve yazma modunda açar
        self.file.seek(0)  # Dosyanın başına git
        self.kitaplar = self.file.readlines()  # Dosyanın içeriğini oku ve kitaplar listesine aktar

    def __del__(self):
        # Dosyayı kapat
        self.file.close()

    def kitapları_listele(self):
        # Kütüphanedeki kitapları listele
        if not self.kitaplar:  
            print("Kütüphanede hiç kitap yoktur.")
        else:
            print("Kütüphanedeki kitapları listele:")
            for kitap in self.kitaplar:
                # Her bir kitabın bilgilerini ekrana yazdır
                kitap_bilgisi = kitap.strip().split(",")  
                kitap_adı, yazar, yayın_tarihi, sayfa_sayısı = kitap_bilgisi
                print(f"Kitap Adı: {kitap_adı}, Yazar: {yazar}")

    def kitap_ekle(self):
        # Kullanıcıdan yeni bir kitap eklemesi için bilgileri al
        kitap_adı = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayın_tarihi = input("Yayın Tarihi: ")
        sayfa_sayısı = input("Sayfa Sayısı: ")

        # Yeni kitabı dosyaya ekle ve listeye ekle
        yeni_kitap = f"{kitap_adı},{yazar},{yayın_tarihi},{sayfa_sayısı}\n"
        self.file.write(yeni_kitap)
        self.kitaplar.append(yeni_kitap)
        print("Kitap başarıyla eklendi.")

    def kitap_sil(self, kitap_adı):
        # Verilen kitap adına sahip kitabı kütüphaneden sil
        güncellenmiş_kitaplar = []
        for kitap in self.kitaplar:
            if kitap_adı not in kitap:
                güncellenmiş_kitaplar.append(kitap)

        if len(güncellenmiş_kitaplar) == len(self.kitaplar):
            # Silinecek kitap bulunamadı
            print(f"'{kitap_adı}' adlı kitap bulunamadı.")
            return

        # Dosyanın içeriğini güncelle
        self.file.seek(0)
        self.file.write("") 

        for kitap in güncellenmiş_kitaplar:
            self.file.write(kitap)

        # Kitaplar listesini güncelle
        self.kitaplar = güncellenmiş_kitaplar
        print(f"'{kitap_adı}' adlı kitap başarıyla silindi.")

def library_menu(lib):
    # Kütüphane işlemleri için bir menü oluştur ve kullanıcıdan seçim yapmasını iste
    print(" LIBRARY MENU ")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")

    menu_secimi = input("LIBRARY MENU'den yapmak istediğiniz işlemi seçin: ")

    if menu_secimi == "1":
        lib.kitapları_listele()
    elif menu_secimi == "2":
        lib.kitap_ekle()
    elif menu_secimi == "3":
        silinecek_kitap = input("Silmek istediğiniz kitabın adını girin: ")
        lib.kitap_sil(silinecek_kitap)
    else:
        print("Seçtiğiniz rakama uygun komut bulunamadı. Geçerli bir rakam seçiniz.")


lib = Library()

library_menu(lib)









