#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ana_pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_init()
        self.show()
        
    def main_init(self):
        self.setWindowTitle("E-Ticaret Siteleri İçin Analiz Programı")
        
        self.ortalama_sepet = QPushButton("Ortalama Sepet Değeri",self)
        self.ortalama_sepet.clicked.connect(self.bir)
        self.ortalama_sepet.setGeometry(100,100,175,50)
        
        
        self.ortalama_siparis = QPushButton("Ortalama Sipariş Değeri",self)
        self.ortalama_siparis.clicked.connect(self.iki)
        self.ortalama_siparis.setGeometry(300,100,175,50)
        
        
        self.donusum_oranı = QPushButton("Dönüşüm Oranı",self)
        self.donusum_oranı.clicked.connect(self.uc)
        self.donusum_oranı.setGeometry(500,100,175,50)
        
        
        self.setGeometry(100, 100, 800, 350)
    def bir(self):
        self.birinci = ortSep()
        self.birinci.show()
    def iki(self):
        self.ikinci = ortSip()
        self.ikinci.show()
    def uc(self):
        self.ucuncu = donusOran()
        self.ucuncu.show()
    
class ortSep(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
    def init_ui(self):
        grid = QGridLayout()
        self.toplam_hasilat = QLineEdit()
        grid.addWidget(QLabel("Toplam Hasılatı Giriniz:"),1,0)
        grid.addWidget(self.toplam_hasilat,1,1)
        grid.addWidget(QLabel("Sipariş Sayısını Giriniz:"),2,0)
        self.siparis_sayisi = QLineEdit()
        grid.addWidget(self.siparis_sayisi,2,1)
        self.hesaplama_butonu = QPushButton("Hesapla")
        self.hesaplama_butonu.clicked.connect(self.hesapla)
        grid.addWidget(self.hesaplama_butonu,3,1)
        grid.addWidget(QLabel("Ortalama Sepet Değeri:"),4,0)
        self.sonuc = QLabel("")
        grid.addWidget(self.sonuc,4,1)
        self.setLayout(grid)
        self.setWindowTitle("Ortalama Sepet Değeri")
        self.show()
    def hesapla(self):
        topHasilat=0
        try:topHasilat=int(self.toplam_hasilat.text())
        except:pass
        sipSayisi=0
        try:sipSayisi= int(self.siparis_sayisi.text())
        except:pass
        toplamMaliyet=topHasilat/sipSayisi
        self.sonuc.setText('%0.1f' % toplamMaliyet)
    
class ortSip(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("Müşteri Sayısını Giriniz:"),1,0)
        self.musteri_sayisi = QLineEdit()
        grid.addWidget(self.musteri_sayisi,1,1)
        grid.addWidget(QLabel("Ortalama Sipariş Tutarını Giriniz:"),2,0)
        self.ortalama_siparis = QLineEdit()
        grid.addWidget(self.ortalama_siparis,2,1)
        self.hesaplama_butonu = QPushButton("Hesapla")
        self.hesaplama_butonu.clicked.connect(self.hesapla)
        grid.addWidget(self.hesaplama_butonu,3,1)
        grid.addWidget(QLabel("Ortalama Sipariş Değeri:"),4,0)
        self.sonuc = QLabel("")
        grid.addWidget(self.sonuc,4,1)
        self.setWindowTitle("Ortalama Sipariş Değeri")
        self.setLayout(grid)
        self.show()
    def hesapla(self):
        musSayisi=0
        try:musSayisi=int(self.musteri_sayisi.text())
        except:pass
        ortalamaSiparis=0
        try:ortalamaSiparis=int(self.ortalama_siparis.text())
        except:pass
        toplamMaliyet=ortalamaSiparis/musSayisi
        self.sonuc.setText('%0.1f' % toplamMaliyet)
    
class donusOran(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("Ziyaretçi Sayısını Giriniz:"),1,0)
        self.ziyaretci_sayisi = QLineEdit()
        grid.addWidget(self.ziyaretci_sayisi,1,1)
        grid.addWidget(QLabel("Müşteri Sayısını Giriniz:"),2,0)
        self.musteri_sayisi = QLineEdit()
        grid.addWidget(self.musteri_sayisi,2,1)
        self.hesaplama_butonu = QPushButton("Hesapla")
        self.hesaplama_butonu.clicked.connect(self.hesapla)
        grid.addWidget(self.hesaplama_butonu,3,1)
        grid.addWidget(QLabel("Dönüşüm Oranı:"),4,0)
        self.sonuc = QLabel("")
        grid.addWidget(self.sonuc,4,1)
        self.setLayout(grid)
        self.setWindowTitle("Dönüşüm Oranı")
        self.show()
    def hesapla(self):
        ziySayisi=0
        try:ziySayisi=int(self.ziyaretci_sayisi.text())
        except:pass
        musSayisi=0
        try:musSayisi=int(self.musteri_sayisi.text())
        except:pass
        toplamMaliyet=ziySayisi/musSayisi
        self.sonuc.setText('%0.1f'%toplamMaliyet)
uygulama = QApplication(sys.argv)
pencere = ana_pencere()
sys.exit(uygulama.exec_())


# In[ ]:




