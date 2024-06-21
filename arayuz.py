import iö_Eyüp_ve_Safa_lib as ed

def veritabaniHazirlama():
    try:
        ilk_kurulum = ed.VT_Olustur()
        ilk_kurulum.tablolariOlustur()
        ilk_kurulum.verileriGir()
        ilk_kurulum.baglantiyiKapat()
    except Exception as e:
            print(f"Hata Oluştu: {str(e)}")

while True:
    print("\n","-"*50,"\n")
    print("\t","1 => Kullanıcı İşlemleri")
    print("\t","2 => Kategori İşlemleri")
    print("\t","3 => Ürün İşlemleri")
    print("\t","4 => Sipariş İşlemleri")
    print("\t","5 => Sepet Görüntüle")
    secim = input("\nKullanmak istediğiniz menüyü seçiniz (çıkmak için x giriniz) : ")
    
    if secim == "0":
        veritabaniHazirlama()

    elif secim == "1":
        while True:
            kullanici = ed.Kullanicilar()
            print("\n","-"*50)
            print("\n\t","1 => Kullanıcı Ekle")
            print("\t","2 => Kullanıcı Sil")
            print("\t","3 => Kullanıcı Güncelle")
            print("\t","4 => Tüm Kullanıcıları Gör")
            print("\t","5 => İsme Göre Kullanıcı Gör")
            print("\t","6 => Alan Kısıtına Göre Kullanıcıları Gör")
            kullaniciSecim = input("\nKullanmak istediğiniz menüyü seçiniz (üst menüye çıkmak için x giriniz) : ")
            if kullaniciSecim == "1":
                kullanici.kullaniciEkle()
            elif kullaniciSecim == "2":
                kullanici.kullaniciSil()
            elif kullaniciSecim == "3":
                kullanici.kullaniciGuncelle()
            elif kullaniciSecim == "4":
                kullanici.tumKullaniciGetir()
            elif kullaniciSecim == "5":
                kullanici.isimKullaniciGetir()
            elif kullaniciSecim == "6":
                kullanici.alanGetir()
            elif kullaniciSecim == "x" or kullaniciSecim == "X":
                break

    elif secim == "2":
        while True:
            kategori = ed.Kategoriler()
            print("\n","-"*50)
            print("\n\t","1 => Kategori Ekle")
            print("\t","2 => Kategori Sil")
            print("\t","3 => Kategori Güncelle")
            print("\t","4 => Tüm Kategorileri Gör")
            kategoriSecim = input("\nKullanmak istediğiniz menüyü seçiniz (üst menüye çıkmak için x giriniz) : ")
            if kategoriSecim == "1":
                kategori.kategoriEkle()
            elif kategoriSecim == "2":
                kategori.kategoriSil()
            elif kategoriSecim == "3":
                kategori.kategoriGuncelle()
            elif kategoriSecim == "4":
                kategori.tumKategoriGetir() 
            elif kategoriSecim == "x" or kategoriSecim == "X":
                break
            
    elif secim == "3":
        while True:
            urun = ed.Urunler()
            print("\n","-"*50)
            print("\n\t","1 => Ürün Ekle")
            print("\t","2 => Ürün Sil")
            print("\t","3 => Ürün Güncelle")
            print("\t","4 => Tüm Ürünleri Gör")
            print("\t","5 => Kategoriye Göre Ürün Gör")
            print("\t","6 => Fiyata Göre Ürün Gör")
            urunSecim = input("\nKullanmak istediğiniz menüyü seçiniz (üst menüye çıkmak için x giriniz) : ")
            if urunSecim == "1":
                urun.urunEkle()
            elif urunSecim == "2":
                urun.urunSil()
            elif urunSecim == "3":
                urun.urunGuncelle()
            elif urunSecim == "4":
                urun.tumUrunGetir()
            elif urunSecim == "5":
                urun.kategoriUrunGetir()
            elif urunSecim == "6":
                urun.fiyatUrunGetir()
            elif urunSecim == "x" or urunSecim == "X":
                break
            
    elif secim == "4":
        while True:
            siparis = ed.Siparisler()
            print("\n","-"*50)
            print("\n\t","1 => Sipariş Oluştur")
            print("\t","2 => Sipariş Sil")
            print("\t","3 => Sipariş Güncelle")
            print("\t","4 => Tüm Siparişleri Gör")
            print("\t","5 => İsme Göre Sipariş Gör")
            print("\t","6 => Sipariş Teslim Tarihi")
            print("\t","7 => Ödeme durumuna göre sipariş gör")
            siparisSecim = input("\nKullanmak istediğiniz menüyü seçiniz (üst menüye çıkmak için x giriniz) : ")
            if siparisSecim == "1":
                siparis.siparisOlustur()
            elif siparisSecim == "2":
                siparis.siparisSil()
            elif siparisSecim == "3":
                siparis.siparisGuncelle()
            elif siparisSecim == "4":
                siparis.tumSiparisGetir()
            elif siparisSecim == "5":
                siparis.isimSiparisGetir()
            elif siparisSecim == "6":
                siparis.siparisTeslim()
            elif siparisSecim == "7":
                siparis.odemeSiparisGetir()
            elif siparisSecim == "x" or siparisSecim == "X":
                break
            
    elif secim == "5":
        while True:
            sepet = ed.Sepet()
            print("\n","-"*50)
            print("\n\t","1 => İsme göre sepetteki ürünleri gör")
            print("\t","2 => Ürün adına göre sepetteki ürünleri gör")
            sepetSecim = input("\nKullanmak istediğiniz menüyü seçiniz (üst menüye çıkmak için x giriniz) : ")
            if sepetSecim == "1":
                sepet.sepetGor()
            elif sepetSecim == "2":
                sepet.urunSepetGetir()
            elif sepetSecim == "x" or siparisSecim == "X":
                break
        
    elif secim == "x" or secim == "X":
        print("\nUygulama Sonlandırıldı!\n")
        break