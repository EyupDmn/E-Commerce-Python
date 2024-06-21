import mysql.connector
import random



class VT_Olustur():
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="Tester_74"
        )
        self.cursor = self.mydb.cursor()
        vt_adi = "eyüp_safa"
        print("\n\n---KURULUM İŞLEMLERİ BAŞLATILDI---\n")
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {vt_adi};")
        self.cursor.execute(f"USE {vt_adi}")
        self.mydb.commit()
    
    def tablolariOlustur(self):
        self.cursor.execute("""create table IF NOT EXISTS kullanicilar
                                (
                                    kullaniciID int auto_increment primary key,
                                    ad		varchar(25)		not null,
                                    soyad	varchar(25)		not null,
                                    eposta	varchar(100)	not null,
                                    sifre	varchar(25)		not null,
                                    adres	varchar(255)	not null,
                                    telefon	char(11)		not null
                                )Engine=InnoDB;
                            """)
        self.mydb.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS kategoriler
                                (
                                    kategoriID int auto_increment primary key,
                                    kategoriAdi VARCHAR(25)	not null
                                )Engine=InnoDB;
                            """)
        self.mydb.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS urunler 
                                (
                                    urunID INT AUTO_INCREMENT PRIMARY KEY,
                                    urunAdi 	VARCHAR(100)	not null,
                                    kategoriID 	INT,
                                    fiyat 		DECIMAL(10, 2)	not null,
                                    stokDurumu 	INT				not null,
                                    aciklama	TEXT			not null,
                                    FOREIGN KEY (kategoriID) REFERENCES kategoriler(kategoriID)
                                    on delete cascade on update cascade
                                )Engine=InnoDB;
                            """)
        self.mydb.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS siparisler 
                                (
                                    siparisID INT AUTO_INCREMENT PRIMARY KEY,
                                    kullaniciID 	INT,
                                    tarih 			DATETIME,
                                    OdemeDurumu VARCHAR(50),
                                    teslimatAdresi 	VARCHAR(255)	not null,
                                    FOREIGN KEY (kullaniciID) REFERENCES kullanicilar(kullaniciID)
                                    on delete cascade on update cascade
                                )Engine=InnoDB;
                            """)
        self.mydb.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS siparisDetaylari 
                                (
                                    detayID INT AUTO_INCREMENT PRIMARY KEY,
                                    siparisID INT,
                                    urunID INT,
                                    miktar INT	not null,
                                    birimFiyat DECIMAL(10, 2)	not null,
                                    toplamFiyat DECIMAL(10, 2)	not null,
                                    FOREIGN KEY (siparisID) REFERENCES siparisler(siparisID)
                                    on delete cascade on update cascade,
                                    FOREIGN KEY (urunID) REFERENCES urunler(urunID)
                                    on delete cascade on update cascade
                                )Engine=InnoDB;
                            """)
        self.mydb.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Sepet 
                                (
                                    sepetID INT AUTO_INCREMENT PRIMARY KEY,
                                    kullaniciID INT,
                                    urunID INT,
                                    miktar INT,
                                    FOREIGN KEY (kullaniciID) REFERENCES kullanicilar(kullaniciID)
                                    on delete cascade on update cascade,
                                    FOREIGN KEY (urunID) REFERENCES urunler(UrunID)
                                    on delete cascade on update cascade
                                )Engine=InnoDB;""")
        self.mydb.commit()
        self.cursor.execute("""CREATE VIEW KullaniciSiparisView AS
                                SELECT
                                s.siparisID,
                                k.ad,
                                k.soyad,
                                s.tarih,
                                s.odemeDurumu,
                                s.teslimatAdresi
                                FROM
                                siparisler as s
                                JOIN kullanicilar as k ON s.kullaniciID = k.kullaniciID;""")
        self.mydb.commit()
        self.cursor.execute("""CREATE VIEW UrunStokView AS
                                SELECT
                                u.urunID,
                                u.urunAdi,
                                k.kategoriAdi,
                                u.fiyat,
                                u.stokDurumu
                                FROM
                                urunler as u
                                JOIN kategoriler as k ON u.kategoriID = k.kategoriID;""")
        self.mydb.commit()
        self.cursor.execute("""CREATE VIEW SiparisDetayView AS
                                SELECT
                                sd.detayID,
                                s.siparisID,
                                u.urunAdi,
                                sd.miktar,
                                sd.birimFiyat,
                                sd.toplamFiyat
                                FROM
                                siparisDetaylari as sd
                                JOIN siparisler as s ON sd.siparisID = s.siparisID
                                JOIN urunler as u ON sd.urunID = u.urunID;""")
        self.mydb.commit()
        self.cursor.execute("""CREATE VIEW KategoriUrunSayisiView AS
                                SELECT
                                k.kategoriAdi,
                                COUNT(u.urunID) AS urunSayisi
                                FROM
                                kategoriler as k
                                LEFT JOIN urunler as u ON k.kategoriID = u.kategoriID
                                GROUP BY
                                k.kategoriID;""")
        self.mydb.commit()
        self.cursor.execute("""CREATE VIEW KullaniciSepetView AS
                                SELECT
                                s.sepetID,
                                k.ad,
                                k.soyad,
                                u.urunAdi,
                                s.miktar
                                FROM
                                Sepet as s
                                JOIN kullanicilar as k ON s.kullaniciID = k.kullaniciID
                                JOIN urunler as u ON s.urunID = u.urunID;""")
        self.mydb.commit()

        print("\nTablolar Oluşturuldu\n")
        
    def verileriGir(self):
        self.cursor.execute("""INSERT INTO Kullanicilar (Ad, Soyad, Eposta, Sifre, Adres, Telefon)
                            VALUES 
                                ('Ahmet', 'Yılmaz', 'ahmet.yilmaz@email.com', 'ahmetyilmaz123', 'Bartın', '12345678901'),
                                ('Ayşe', 'Demir', 'ayse.demir@email.com', 'aysedemir123', 'İstanbul', '12345678902'),
                                ('Mehmet', 'Kara', 'mehmet.kara@email.com', 'mehmetkara123', 'Ankara', '12345678903'),
                                ('Zeynep', 'Beyaz', 'zeynep.beyaz@email.com', 'zeynepbeyaz123', 'Ankara', '12345678904'),
                                ('Can', 'Aksoy', 'can.aksoy@email.com', 'canaksoy123', 'Bartın', '12345678905'),
                                ('Elif', 'Yıldız', 'elif.yildiz@email.com', 'elifyildiz123', 'Eskişehir', '12345678906'),
                                ('Ahmet', 'Tekin', 'ahmet.tekin@email.com', 'ahmettekin123', 'İzmir', '12345678907'),
                                ('Ece', 'Aydın', 'ece.aydin@email.com', 'eceaydin123', 'İstanbul', '12345678908'),
                                ('Cem', 'Güneş', 'cem.gunes@email.com', 'cemgünes123', 'İzmir', '12345678909'),
                                ('Gizem', 'Kurt', 'gizem.kurt@email.com', 'gizemkurt123', 'Bursa', '12345678910'),
                                ('Efe', 'Çetin', 'efe.cetin@email.com', 'efecetin123', 'Konya', '12345678911'),
                                ('Aslı', 'Koç', 'asli.koc@email.com', 'aslikoc123', 'Aydın', '12345678912'),
                                ('Tolga', 'Yılmaz', 'tolga.yilmaz@email.com', 'tolgayilmaz123', 'Muğla', '12345678913'),
                                ('Deniz', 'Acar', 'deniz.acar@email.com', 'denizacar123', 'Antalya', '12345678914'),
                                ('Elif', 'Demir', 'elif.demir@email.com', 'elifdemir123', 'Trabzon', '12345678915');""")
        self.mydb.commit()
        self.cursor.execute("""INSERT INTO Kategoriler (KategoriAdi)
                            VALUES 
                                ('Bilgisayarlar'),
                                ('Ev Elektroniği'),
                                ('Giyim'),
                                ('Ayakkabılar'),
                                ('Ev & Yaşam'),
                                ('Kozmetik'),
                                ('Kitaplar'),
                                ('Oyuncaklar'),
                                ('Spor Malzemeleri'),
                                ('Mobilya'),
                                ('Mücevherat'),
                                ('Aksesuarlar'),
                                ('Araba Aksesuarları'),
                                ('Bahçe & Outdoor'),
                                ('Sağlık & Fitness');""")
        self.mydb.commit()
        self.cursor.execute("""INSERT INTO Urunler (UrunAdi, KategoriID, Fiyat, StokDurumu, Aciklama)
                            VALUES 
                                ('Laptop', 1, 1500.00, 50, 'Güçlü bir bilgisayar'),
                                ('T-Shirt', 2, 20.00, 100, 'Rahat pamuklu t-shirt'),
                                ('Akıllı Telefon', 1, 800.00, 30, 'Yüksek performanslı akıllı telefon'),
                                ('Spor Ayakkabı', 4, 50.00, 80, 'Konforlu spor ayakkabı'),
                                ('Mikrodalga Fırın', 5, 120.00, 25, 'Hızlı ve etkili mikrodalga fırın'),
                                ('Parfüm', 6, 30.00, 50, 'Özel koku notalarına sahip parfüm'),
                                ('Roman Kitabı', 7, 15.00, 120, 'Heyecan verici bir roman'),
                                ('Oyuncak Araba', 8, 10.00, 200, 'Çocuklar için eğlenceli oyuncak araba'),
                                ('Yoga Matı', 9, 25.00, 40, 'Konforlu ve kaymaz yoga matı'),
                                ('Çalışma Masası', 10, 100.00, 15, 'Modern tasarımlı çalışma masası'),
                                ('Altın Kolye', 11, 200.00, 10, 'Elegant altın kolye'),
                                ('Güneş Gözlüğü', 12, 40.00, 30, 'Şık güneş gözlüğü'),
                                ('Araba Şarj Cihazı', 13, 15.00, 50, 'Hızlı şarj özellikli araba şarj cihazı'),
                                ('Bahçe Sandalyesi', 14, 35.00, 20, 'Rahat bahçe sandalyesi'),
                                ('Pilates Topu', 15, 12.00, 60, 'Pilates ve egzersiz için top');""")
        self.mydb.commit()
        self.cursor.execute("""INSERT INTO Siparisler (KullaniciID, Tarih, OdemeDurumu, TeslimatAdresi)
                            VALUES 
                                (1, '2023-01-01 12:00:00', 'Ödendi', 'Bartın'),
                                (2, '2023-02-01 14:30:00', 'Ödendi', 'İstanbul'),
                                (4, '2023-03-01 15:45:00', 'Beklemede', 'Trabzon'),
                                (5, '2023-04-01 16:30:00', 'Ödendi', 'Konya'),
                                (6, '2023-05-01 18:15:00', 'Beklemede', 'Antalya'),
                                (7, '2023-06-01 19:20:00', 'Ödendi', 'Eskişehir'),
                                (8, '2023-07-01 20:45:00', 'Ödendi', 'Ankara'),
                                (9, '2023-08-01 22:00:00', 'Beklemede', 'İstanbul'),
                                (3, '2023-09-01 23:10:00', 'Ödendi', 'Bursa'),
                                (4, '2023-10-01 01:30:00', 'Beklemede', 'Bartın'),
                                (8, '2023-11-01 02:45:00', 'Ödendi', 'İstanbul'),
                                (11, '2023-12-01 04:00:00', 'Ödendi', 'Konya'),
                                (9, '2024-01-01 05:15:00', 'Beklemede', 'Muğla'),
                                (2, '2024-02-01 06:30:00', 'Ödendi', 'Trabzon'),
                                (1, '2024-03-01 07:45:00', 'Ödendi', 'Ankara');""")
        self.mydb.commit()
        self.cursor.execute("""INSERT INTO SiparisDetaylari (SiparisID, UrunID, Miktar, BirimFiyat, ToplamFiyat)
                            VALUES 
                                (1, 1, 1, 1500.00, 1500.00),
                                (2, 2, 2, 20.00, 40.00),
                                (3, 3, 1, 800.00, 800.00),
                                (4, 4, 5, 10.00, 50.00),
                                (5, 5, 2, 60.00, 120.00),
                                (6, 6, 1, 30.00, 30.00),
                                (7, 7, 3, 5.00, 15.00),
                                (8, 8, 2, 25.00, 50.00),
                                (9, 9, 1, 25.00, 25.00),
                                (10, 10, 4, 25.00, 100.00),
                                (11, 11, 2, 100.00, 200.00),
                                (12, 12, 1, 40.00, 40.00),
                                (13, 13, 3, 5.00, 15.00),
                                (14, 14, 2, 17.50, 35.00),
                                (15, 15, 1, 12.00, 12.00);""")
        self.mydb.commit()
        self.cursor.execute("""INSERT INTO Sepet (KullaniciID, UrunID, Miktar)
                            VALUES 
                                (1, 1, 1),
                                (2, 2, 2),
                                (3, 9, 1),
                                (1, 15, 1),
                                (2, 9, 2),
                                (3, 11, 1),
                                (1, 13, 4),
                                (2, 15, 2),
                                (3, 2, 1), 
                                (1, 4, 3),
                                (2, 6, 2),
                                (3, 8, 1),
                                (1, 10, 5),
                                (2, 12, 2),
                                (3, 14, 1);""")
        self.mydb.commit()
        print("Örnek Veriler Girildi\n")
        
    def baglantiyiKapat(self):
        self.mydb.close()
        print("Bağlantı kapatıltı\n\n---KURULUM İŞLEMLERİ TAMAMLANDI---\n")

   

class Kullanicilar():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="Tester_74"
        )
        self.cursor = self.mydb.cursor()
        self.cursor.execute("use eyüp_safa")
        self.mydb.commit()
        
    def kullaniciEkle(self):
        try:
            ad = input("\nAd Giriniz: ").capitalize()
            soyad = input("Soyad Giriniz: ").upper()
            eposta = input("E-posta Giriniz: ")
            sifre = input("Şifre Giriniz: ")
            adres = input("Adres Giriniz: ")
            while (True):
                telefon =input("Telefon Giriniz (11 Karakter): ")
                if(len(telefon)==11):
                    break
            self.cursor.execute(f"insert into kullanicilar(ad,soyad,eposta,sifre,adres,telefon) values ('{ad}','{soyad}','{eposta}','{sifre}','{adres}','{int(telefon)}')")
            self.mydb.commit()
            print("\nKullanıcı Eklendi!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def kullaniciSil(self):
        try:
            kullanici = Kullanicilar()
            id_ = int(input("\nSilmek istediğiniz kullanıcının ID'sini giriniz: "))
            sonuc = kullanici.kullaniciVarMi(id_)
            if sonuc:
                self.cursor.execute(f"delete from kullanicilar where kullaniciID = {id_}")
                self.mydb.commit()
                print("\nKullanıcı Silindi!")
            else:
                print("\nKullanıcı Bulunamadı!")
        except:
            print("Hata Oluştu")
        finally:
            self.mydb.close()

    def kullaniciGuncelle(self):
        try:
            kullanici = Kullanicilar()
            id_ = int(input("\nGüncellemek istediğiniz kullanıcının ID'sini giriniz: "))
            sonuc = kullanici.kullaniciVarMi(id_)
            if sonuc:
                ad = input("Ad Giriniz: ")
                soyad = input("Soyad Giriniz: ")
                eposta = input("E-posta Giriniz: ")
                sifre = input("Şifre Giriniz: ")
                adres = input("Adres Giriniz: ")
                while True:
                    telefon =input("Telefon Giriniz (11 Karakter): ")
                    if(len(telefon)==11):
                        break
                self.cursor.execute(f"update kullanicilar set ad = '{ad}', soyad = '{soyad}', eposta = '{eposta}', sifre = '{sifre}', adres = '{adres}', telefon = '{telefon}' where kullaniciID = {id_}")
                self.mydb.commit()
                print("\nKullanıcı Güncellendi!")
            else:
                print("\nKullanıcı Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()

    def tumKullaniciGetir(self):
        try:
            self.cursor.execute("select * from kullanicilar")
            sonuc = self.cursor.fetchall()
            for row in sonuc:
                print("\n\tKullanıcı ID:",row[0],
                      "\n\tAdı:",row[1],
                      "\n\tSoyadı:",row[2],
                      "\n\tE-Posta:",row[3],
                      "\n\tŞifre:",row[4],
                      "\n\tAdres:",row[5],
                      "\n\tTelefon:",row[6])
            self.mydb.commit()
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()

    def isimKullaniciGetir(self):
        try:
            isim = input("Kullanıcı Adı: ").capitalize()
            self.cursor.execute(f"select * from kullanicilar where ad = '{isim}'")
            print("asd")
            sonuc = self.cursor.fetchall()
            if sonuc:
                for row in sonuc:
                    print("\n\tKullanıcı ID:",row[0],
                      "\n\tAdı:",row[1],
                      "\n\tSoyadı:",row[2],
                      "\n\tE-Posta:",row[3],
                      "\n\tŞifre:",row[4],
                      "\n\tAdres:",row[5],
                      "\n\tTelefon:",row[6])
                self.mydb.commit()
            else:
                print("\nKullanıcı Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def alanGetir(self):
        try:
            alan = input("Görmek İstediğiniz Alan: ")
            self.cursor.execute(f"select {alan} from kullanicilar")
            sonuc = self.cursor.fetchall()
            for row in sonuc:
                print("\n\t",f"{alan}: {row[0]}")
            self.mydb.commit()
        except:
            print("\nAlan Bulunamadı!")
            print("Kullanılabilir Alanlar : kullaniciID,ad,soyad,eposta,sifre,adres,telefon")
        finally:
            self.mydb.close()
            
    def kullaniciVarMi(self,id_):
        try: 
            self.cursor.execute(f"select * from kullanicilar where kullaniciID = {id_}")
            sonuc = self.cursor.fetchone()
            return sonuc
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
    


class Kategoriler():
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="Tester_74"
        )
        self.cursor = self.mydb.cursor()
        self.cursor.execute("use eyüp_safa")
        self.mydb.commit()
    
    def kategoriEkle(self):
        try:
            kategori = Kategoriler()
            deger = input("\nKategori Adı Giriniz: ").capitalize()
            sonuc = kategori.kategoriVarMi()
            varMi = False
            for row in sonuc:
                if deger == row[1].capitalize():
                    varMi = True
                    break
            if not varMi:
                    self.cursor.execute(f"insert into Kategoriler(kategoriAdi) values ('{deger}')")
                    self.mydb.commit()
                    print("\nKategori Eklendi!")
            else:
                print("\nKategori Mevcut!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def kategoriSil(self):
        try:
            kategori = Kategoriler()
            sonuc = kategori.kategoriVarMi()
            varMi = False
            id_ = int(input("\nSilmek istediğiniz kategorinin ID'sini giriniz : "))
            for row in sonuc:
                if id_ == row[0]:
                    varMi = True
                    break
            if varMi:
                self.cursor.execute(f"delete from kategoriler where kategoriID = '{id_}'")
                self.mydb.commit()
                print("\nKategori Silindi!")
            else:
                print("\nKategori Bulunamadı")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def kategoriGuncelle(self):
        try:
            kategori = Kategoriler()
            sonuc = kategori.kategoriVarMi()
            varMi = False
            id_ = int(input("\nGüncellemek istediğiniz kategorinin ID'sini giriniz : "))
            for row in sonuc:
                if id_ == row[0]:
                    varMi = True
                    break
            if varMi:
                ad = input("Kategori Adı: ")
                self.cursor.execute(f"update kategoriler set kategoriAdi = '{ad}' where kategoriID = '{id_}'")
                self.mydb.commit()
                print("\nKategori Güncellendi!")
            else:
                print("\nKategori Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def tumKategoriGetir(self):
        try:
            self.cursor.execute("select * from kategoriler")
            sonuc = self.cursor.fetchall()
            for row in sonuc:
                print("\n\tKategori ID:",row[0],
                      "\n\tAdı:",row[1],)
            self.mydb.commit()
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()            
            
    def kategoriVarMi(self):
        try:
            self.cursor.execute("select * from kategoriler")
            sonuc = self.cursor.fetchall()
            return sonuc
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close() 
        
    
        
class Urunler():
            
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="Tester_74"
        )
        self.cursor = self.mydb.cursor()
        self.cursor.execute("use eyüp_safa")
        self.mydb.commit()
        
    def urunEkle(self):
        try:
            kategori = Kategoriler()
            sonuc = kategori.kategoriVarMi()
            kategoriAdi = input("Ürün kategorisini giriniz : ").capitalize()
            varMi = False
            for row in sonuc:
                if kategoriAdi == row[1]:
                    varMi = True
                    kategoriID = row[0]
                    break
            if varMi: 
                ad = input("Ad Giriniz: ")
                fiyat = int(input("Fiyat Giriniz: "))
                stokDurumu = int(input("Stok Durumu Giriniz: "))
                aciklama = input("Açıklama Giriniz: ")
                self.cursor.execute(f"insert into urunler(urunAdi,kategoriID,fiyat,stokDurumu,aciklama) values ('{ad}','{kategoriID}','{fiyat}','{stokDurumu}','{aciklama}')")
                self.mydb.commit()
                print("\nÜrün Eklendi!")
            else:
                print("\nKategori Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def urunSil(self):
        try:
            urun = Urunler()
            id_ = int(input("\nSilmek istediğiniz ürün ID'sini girinizi: "))
            sonuc = urun.urunVarMi(id_)
            if sonuc:
                self.cursor.execute(f"delete from urunler where urunID = '{id_}'")
                self.mydb.commit()
                print("\nÜrün Silindi!")
            else:
                print("\nÜrün Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def urunGuncelle(self):
        try:
            urun = Urunler()
            kategori = Kategoriler()
            id_ = int(input("\nGüncellemek istediğiniz ürünün ID'sini giriniz: "))
            sonuc = urun.urunVarMi(id_)
            kategoriAdi = input("\nÜrün kategorisini giriniz: ").capitalize()
            varMi = False
            kSonuc = kategori.kategoriVarMi()
            for row in kSonuc:
                if kategoriAdi == row[1].capitalize():
                    kategoriID = row[0]
                    varMi = True
                    break
            if varMi and sonuc:
                ad = input("\nAd Giriniz: ")
                fiyat = int(input("Fiyat Giriniz: "))
                stokDurumu = int(input("Stok Durumu Giriniz: "))
                aciklama = input("Açıklama Giriniz: ")
                self.cursor.execute(f"update urunler set urunAdi = '{ad}', kategoriID = '{kategoriID}', fiyat = '{fiyat}', stokDurumu = '{stokDurumu}', aciklama = '{aciklama}' where urunID = '{id_}'")
                self.mydb.commit()
                print("\nÜrün Güncellendi!")
            else:
                print("\nKategori veya Ürün Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def tumUrunGetir(self):
        try:
            self.cursor.execute("select * from urunler")
            sonuc = self.cursor.fetchall()
            for row in sonuc:
                print("\n\tÜrün ID:",row[0],
                      "\n\tÜrün Adı:",row[1],
                      "\n\tKategori ID:",row[2],
                      "\n\tFiyat:",row[3],
                      "\n\tStok Durumu:",row[4],
                      "\n\tAçıklama:",row[5])
            self.mydb.commit()
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def fiyatUrunGetir(self):
        try:
            min_ = int(input("Minimum tutarı giriniz: "))
            max_ = int(input("Maximum tutarı giriniz: "))
            self.cursor.execute(f"select * from urunler where fiyat between {min_} and {max_};")
            sonuc = self.cursor.fetchall()
            for row in sonuc:
                print("\n\tÜrün ID:",row[0],
                      "\n\tÜrün Adı:",row[1],
                      "\n\tKategori ID:",row[2],
                      "\n\tFiyat:",row[3],
                      "\n\tStok Durumu:",row[4],
                      "\n\tAçıklama:",row[5])
            self.mydb.commit()
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def kategoriUrunGetir(self):
        try:
            kategori = Kategoriler()
            ad = input("\nKategori Adını giriniz: ").capitalize()
            sonuc = kategori.kategoriVarMi()
            varMi = False
            for row in sonuc:
                if ad == row[1].capitalize():
                    varMi = True
                    id_ = row[0]
                    break
            if varMi:
                self.cursor.execute(f"select * from urunler where kategoriID = '{id_}'")
                urun = self.cursor.fetchall()
                for row in urun:
                    print("\n\tÜrün ID:",row[0],
                      "\n\tÜrün Adı:",row[1],
                      "\n\tKategori ID:",row[2],
                      "\n\tFiyat:",row[3],
                      "\n\tStok Durumu:",row[4],
                      "\n\tAçıklama:",row[5])
                self.mydb.commit()
            else:
                print("\nKategori Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()

    def urunVarMi(self,id_):
        try: 
            self.cursor.execute(f"select * from urunler where urunID = {id_}")
            sonuc = self.cursor.fetchone()
            return sonuc
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()



class Siparisler():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="Tester_74"
        )
        self.cursor = self.mydb.cursor()
        self.cursor.execute("use eyüp_safa")
        self.mydb.commit()
        
    def siparisOlustur(self):
        try:
            kullanici = Kullanicilar()
            id_ = int(input("\nKullanıcı ID'nizi giriniz: "))
            sonucID = kullanici.kullaniciVarMi(id_)
            varMiID = False
            if sonucID is not None:
                for row in sonucID:
                    if id_ == row:
                        varMiID = True
                        break
                if varMiID:
                    tarih = input("Sipariş verildiği tarih (örnek:2023-01-01): ")
                    odemeDurumu = input("Ödeme Yapıldı Mı?(evet : hayır): ").lower()
                    if odemeDurumu == "evet":
                        odeme = "Ödendi"
                    else:
                        odeme = "Beklemede"
                    teslimatAdresi = input("Teslimat adresi giriniz: ")
                    self.cursor.execute(f"insert into siparisler(kullaniciID,tarih,odemeDurumu,teslimatAdresi) values ({id_}, '{tarih}', '{odeme}', '{teslimatAdresi}')")
                    siparisID = self.cursor.lastrowid   
                    self.mydb.commit()
                    urun = input("\nÜrün adını giriniz: ").capitalize()
                    self.cursor.execute(f"select * from urunler where urunAdi = '{urun}'")
                    sonucUrun = self.cursor.fetchone()
                    if sonucUrun:
                        miktar = int(input("Adet giriniz: "))
                        fiyatSonuc = sonucUrun[3]
                        self.cursor.execute(f"insert into siparisDetaylari(siparisID,urunID,miktar,birimFiyat,toplamFiyat) values ({siparisID},{sonucUrun[0]},{miktar},{fiyatSonuc},{fiyatSonuc*miktar})")
                        self.cursor.execute(f"insert into sepet(kullaniciID,urunID,miktar) values ({id_},{sonucUrun[0]},{miktar})")
                        self.mydb.commit()
                        print("\nSipariş Oluşturuldu!")
                    else:
                        print("\nÜrün Bulunamadı!")
                        self.cursor.execute(f"delete from siparisler where siparisID = {int(siparisID)}")
                        self.mydb.commit()
                        print("Sipariş Oluşturulamadı!")
            else:
                print("\nKullanıcı Bulunamadı!")
        except Exception as e:
            print(f"Hata Oluştu: {str(e)}")
        finally:
            self.mydb.close()
            
    def siparisSil(self):
        try:
            id_ = int(input("\nSilmek istediğiniz siparişin ID'sini girin: "))
            self.cursor.execute(f"select * from siparisler where siparisID = {id_}")
            sonuc = self.cursor.fetchone()
            if sonuc:
                self.cursor.execute(f"delete from siparisler where siparisID = {id_}")
                self.mydb.commit()
                print("\nSipariş Silindi!")
            else:
                print("\nSipariş Bulunamadı!")
        except:
            print("Hata")
        finally:
            self.mydb.close()
            
    def siparisGuncelle(self):
        try:
            siparis = Siparisler()
            sonuc = siparis.siparisVarMi()
            varMiSiparis = False
            id_ = int(input("Güncellemek istediğiniz sipariş ID'si: "))
            for row in sonuc:
                if id_ == row[0]:
                    varMiSiparis = True
                    break
            if varMiSiparis:
                kullanici = Kullanicilar()
                kID = int(input("\nKullanıcı ID'nizi giriniz: "))
                sonucID = kullanici.kullaniciVarMi(kID)
                varMiID = False
                if sonucID is not None:
                    for row in sonucID:
                        if kID == row:
                            varMiID = True
                            break
                    if varMiID:
                        tarih = input("Sipariş verildiği tarih (örnek:2023-01-01): ")
                        odemeDurumu = input("Ödeme Yapıldı Mı?(evet : hayır): ").lower()
                        if odemeDurumu == "evet":
                            odeme = "Ödendi"
                        else:
                            odeme = "Beklemede"
                        teslimatAdresi = input("Teslimat adresi giriniz: ")
                        self.cursor.execute(f"update siparisler set kullaniciID = {kID}, tarih = '{tarih}', odemeDurumu = '{odeme}', teslimatAdresi = '{teslimatAdresi}'")
                        siparisID = self.cursor.lastrowid
                        urun = input("\nÜrün adını giriniz: ").capitalize()
                        self.cursor.execute(f"select * from urunler where urunAdi = '{urun}'")
                        sonucUrun = self.cursor.fetchone()
                        if sonucUrun:
                            miktar = int(input("Adet giriniz: "))
                            fiyatSonuc = sonucUrun[3]
                            self.cursor.execute(f"update siparisDetaylari set urunID = {sonucUrun[0]}, miktar = {miktar}, birimFiyat = {fiyatSonuc}, toplamFiyat = {fiyatSonuc*miktar}")
                            self.mydb.commit()
                            print("\nSipariş Güncellendi!")
                        else:
                            print("\nÜrün Bulunamadı!")
                            self.cursor.execute(f"delete from siparisler where siparisID = {int(siparisID)}")
                            self.mydb.commit()
                            print("Sipariş Oluşturulamadı!")
                else:
                    print("\nKullanıcı Bulunamadı!")
            else:
                print("\nSipariş Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
        
    def tumSiparisGetir(self):
        try:
            self.cursor.execute("select * from siparisler")
            siparisSonuc = self.cursor.fetchall()
            for row in siparisSonuc:
                self.cursor.execute(f"select * from siparisDetaylari where siparisID = {row[0]}")
                detaySonuc = self.cursor.fetchone()
                self.cursor.execute(f"select * from kullanicilar where kullaniciID = {row[1]}")
                kullaniciSonuc = self.cursor.fetchone()
                self.cursor.execute(f"select * from urunler where urunID = {detaySonuc[2]}")
                urunSonuc = self.cursor.fetchone()
                print("\n\tSipariş ID:",row[0],
                "\n\tKullanıcı Adı Soyadı:",kullaniciSonuc[1]+ " " +kullaniciSonuc[2],
                "\n\tÜrün Adı:",urunSonuc[1],
                "\n\tBirim Fiyat:",detaySonuc[4],
                "\n\tToplam Fiyat:",detaySonuc[5],
                "\n\tTarih:",row[2],
                "\n\tÖdeme Durumu:",row[3],
                "\n\tTeslimat Adresi:",row[4])
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def isimSiparisGetir(self):
        try:
            kullanici = Kullanicilar()
            id_ = int(input("\nKullanıcı ID'si giriniz: "))
            sonucKullanici = kullanici.kullaniciVarMi(id_)
            if sonucKullanici:
                self.cursor.execute(f"select * from siparisler where kullaniciID = {id_}")
                siparisSonuc = self.cursor.fetchall()
                for row in siparisSonuc:
                    self.cursor.execute(f"select * from siparisDetaylari where siparisID = {row[0]}")
                    detaySonuc = self.cursor.fetchone()
                    self.cursor.execute(f"select * from kullanicilar where kullaniciID = {row[1]}")
                    kullaniciSonuc = self.cursor.fetchone()
                    self.cursor.execute(f"select * from urunler where urunID = {detaySonuc[2]}")
                    urunSonuc = self.cursor.fetchone()
                    print("\n\tSipariş ID:",row[0],
                    "\n\tKullanıcı Adı Soyadı:",kullaniciSonuc[1]+ " " +kullaniciSonuc[2],
                    "\n\tÜrün Adı:",urunSonuc[1],
                    "\n\tBirim Fiyat:",detaySonuc[4],
                    "\n\tToplam Fiyat:",detaySonuc[5],
                    "\n\tTarih:",row[2],
                    "\n\tÖdeme Durumu:",row[3],
                    "\n\tTeslimat Adresi:",row[4])
            else:
                print("Kullanıcı Bulunamadı!")
        except Exception as e:
            print(f"Hata Oluştu: {str(e)}")
        finally:
            self.mydb.close()
            
    def siparisTeslim(self):
        try:
            siparis = Siparisler()
            id_ = int(input("\nSiparis ID'si giriniz: "))
            sonucSiparis = siparis.siparisVarMi()
            varMiSiparis = False
            for row in sonucSiparis:
                if id_ == row[0]:
                    varMiSiparis = True
                    break
            if varMiSiparis:
                teslim = random.randint(3,10)
                print(f"Tahmini Teslim Tarihi: {teslim} iş günü")
            else:
                print("Sipariş Bulunamadı!")
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()
            
    def odemeSiparisGetir(self):
        try:
            sorgu = input("\n(Ödenen : Beklemede) :").capitalize()
            if sorgu == "Ödenen" or sorgu == "Odenen":
                odeme = "Ödendi"
            else:
                odeme = "Beklemede"
            self.cursor.execute(f"select * from siparisler where OdemeDurumu = '{odeme}'")
            siparisSonuc = self.cursor.fetchall()
            for row in siparisSonuc:
                self.cursor.execute(f"select * from siparisDetaylari where siparisID = {row[0]}")
                detaySonuc = self.cursor.fetchone()
                self.cursor.execute(f"select * from kullanicilar where kullaniciID = {row[1]}")
                kullaniciSonuc = self.cursor.fetchone()
                self.cursor.execute(f"select * from urunler where urunID = {detaySonuc[2]}")
                urunSonuc = self.cursor.fetchone()
                print("\n\tSipariş ID:",row[0],
                "\n\tKullanıcı Adı Soyadı:",kullaniciSonuc[1]+ " " +kullaniciSonuc[2],
                "\n\tÜrün Adı:",urunSonuc[1],
                "\n\tBirim Fiyat:",detaySonuc[4],
                "\n\tToplam Fiyat:",detaySonuc[5],
                "\n\tTarih:",row[2],
                "\n\tÖdeme Durumu:",row[3],
                "\n\tTeslimat Adresi:",row[4])
        except Exception as e:
            print(str(e))
        finally:
            self.mydb.close()
            
    def siparisVarMi(self):
        try:
            self.cursor.execute("select * from siparisler")
            sonuc = self.cursor.fetchall()
            return sonuc
        except:
            print("Hata Oluştu!")
        finally:
            self.mydb.close()



class Sepet():
        
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="tester",
            password="Tester_74"
        )
        self.cursor = self.mydb.cursor()
        self.cursor.execute("use eyüp_safa")
        self.mydb.commit()
        
    def sepetGor(self):
        try:
            kullanici = Kullanicilar()
            id_ = int(input("\nKullanıcı ID'nizi giriniz: "))
            varMiKullanici = False
            sonucKullanici = kullanici.kullaniciVarMi(id_)
            if sonucKullanici is not None:
                for row in sonucKullanici:
                    if id_ == row:
                        varMiKullanici = True
                        break
                if varMiKullanici:
                    self.cursor.execute(f"select * from sepet where kullaniciID = {id_}")
                    sonucSepet = self.cursor.fetchall()
                    liste = {}
                    tutar = 0
                    print("\n\tAdı Soyadı:",sonucKullanici[1]+" "+sonucKullanici[2])
                    for row in sonucSepet:
                        self.cursor.execute(f"select * from urunler where urunID = {row[2]}")
                        sonucUrun = self.cursor.fetchone()
                        tutar += sonucUrun[3] * row[3]
                        liste[f"{sonucUrun[1]}"] = row[3]
                    for anahtar, deger in liste.items():
                        print(f"\tÜrün: {anahtar} - {deger} Adet")
                    print("\tToplam Tutar: ",tutar)
            else:
                print("Kullanıcı Bulunamadı!")
        except Exception as e:
            print(f"Hata Oluştu: {str(e)}")
        finally:
            self.mydb.close()
            
    def urunSepetGetir(self):
        try:
            urunAdi = input("Ürün adını giriniz: ").capitalize()
            self.cursor.execute(f"select * from urunler where urunAdi = '{urunAdi}'")
            urunSonuc = self.cursor.fetchall()
            if len(urunSonuc) > 0:
                for urun in urunSonuc:
                    self.cursor.execute(f"select * from sepet where urunID = {urun[0]}")
                    sepetSonuc = self.cursor.fetchall()
                    liste = {}
                    tutar = 0
                    for sepet in sepetSonuc:
                        self.cursor.execute(f"select * from kullanicilar where kullaniciID = {sepet[1]}")
                        kullaniciSonuc = self.cursor.fetchone()
                        tutar += urun[3] * sepet[3]
                        liste[f"{urun[1]}"] = sepet[3]
                    print("\n\tAdı Soyadı:",kullaniciSonuc[1]+" "+kullaniciSonuc[2])
                    for anahtar, deger in liste.items():
                        print(f"\tÜrün: {anahtar} - {deger} Adet")
                    print("\tToplam Tutar: ",tutar)
            else:
                print("Ürün Bulunamadı!")
        except Exception as e:
            print(f"Hata Oluştu: {str(e)}")
        finally:
            self.mydb.close()
                
            
            
    