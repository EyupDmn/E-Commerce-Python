create database e_ticaret_platformu;
use e_ticaret_platformu;

create table kullanicilar
(
	kullaniciID int auto_increment primary key,
    ad		varchar(25)		not null,
    soyad	varchar(25)		not null,
    eposta	varchar(100)	not null,
    sifre	varchar(25)		not null,
    adres	varchar(255)	not null,
    telefon	char(11)		not null
)Engine=InnoDB;

create table kategoriler
(
	kategoriID int auto_increment primary key,
    kategoriAdi VARCHAR(25)	not null
)Engine=InnoDB;

CREATE TABLE urunler 
(
    urunID INT AUTO_INCREMENT PRIMARY KEY,
    urunAdi 	VARCHAR(100)	not null,
    kategoriID 	INT,
    fiyat 		DECIMAL(10, 2)	not null,
    stokDurumu 	INT				not null,
    aciklama	TEXT			not null,
    FOREIGN KEY (kategoriID) REFERENCES kategoriler(kategoriID)
)Engine=InnoDB;

CREATE TABLE siparisler 
(
    siparisID INT AUTO_INCREMENT PRIMARY KEY,
    kullaniciID 	INT,
    tarih 			DATETIME,
    odemeDurumu 	varchar(50),
    teslimatAdresi 	VARCHAR(255)	not null,
    FOREIGN KEY (kullaniciID) REFERENCES kullanicilar(kullaniciID)
)Engine=InnoDB;

CREATE TABLE siparisDetaylari 
(
    detayID INT AUTO_INCREMENT PRIMARY KEY,
    siparisID INT,
    urunID INT,
    miktar INT	not null,
    birimFiyat DECIMAL(10, 2)	not null,
    toplamFiyat DECIMAL(10, 2)	not null,
    FOREIGN KEY (siparisID) REFERENCES siparisler(siparisID),
    FOREIGN KEY (urunID) REFERENCES urunler(urunID)
)Engine=InnoDB;

CREATE TABLE Sepet 
(
    sepetID INT AUTO_INCREMENT PRIMARY KEY,
    kullaniciID INT,
    urunID INT,
    miktar INT,
    FOREIGN KEY (kullaniciID) REFERENCES kullanicilar(kullaniciID),
    FOREIGN KEY (urunID) REFERENCES urunler(UrunID)
)Engine=InnoDB;