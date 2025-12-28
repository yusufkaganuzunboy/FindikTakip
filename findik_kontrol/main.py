import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime


from main_ui import Ui_MainWindow

from veritabani import MongoDB


class FindikTakip(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = MongoDB()
       
        
        self.setWindowIcon(QIcon("FındıkKontrolKapak.png"))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.table_data.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris)
        self.baglantilari_kur()
        self.guncelleme_modu = False
        


    def baglantilari_kur(self):
        self.ui.login_button.clicked.connect(self.giris_kontrol)
        self.ui.forgot_button.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_sifre_sifirlama))
        self.ui.signup_button.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_kayit))
        self.ui.giris_ekrana_don_button.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris))
        self.ui.back_to_login_button.clicked.connect(self.uyeOldanGirisEkraninaDon)
        self.ui.btn_logout.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris))
        self.ui.btn_tab_customer.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard))
        self.ui.btn_tab_yield.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_randiman))
        self.ui.btn_tab_price.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.page_fiyat))
        self.ui.anasayfa_button.clicked.connect(self.randimanHesaplamadanAnaSayfayaGec)
        self.ui.fiyathesaplama_sayfa_button.clicked.connect(self.randimanHesaplamadanFiyatHesaplamayaGec)
        self.ui.randiman_cikis_button.clicked.connect(self.randimanHesaplamadanGirisYapaGec)
        self.ui.anasayfa_button_fiyat_hesaplamadan.clicked.connect(self.fiyatHesaplamadanAnaSayfayaGec)
        self.ui.randiman_hesaplama_button_fiyattan.clicked.connect(self.fiyatHesaplamadanRandimanHesaplamayaGec)
        self.ui.cikisyap_button_fiyat.clicked.connect(self.fiyatHesaplamadanGirisYapaGec)
        self.ui.randiman_hesapla_button.clicked.connect(self.randiman_hesapla)
        self.ui.fiyathesapla_button.clicked.connect(self.fiyat_hesapla)  
                                    

        self.ui.checkbox_password.clicked.connect(self.sifreyi_goster)



        self.ui.signup_submit_button.clicked.connect(self.uyeOl)
        self.ui.sifreyi_guncelle_button.clicked.connect(self.sifreYenile)
        self.ui.btn_save.clicked.connect(self.musteriyiTabloyaEkle)
        self.ui.btn_update.clicked.connect(self.musteri_verilerini_guncelle)
        self.ui.btn_delete.clicked.connect(self.musteriyi_sil)



    def giris_kontrol(self):
        
         girilen_kullanici_adi = self.ui.input_username.text()
         girilen_sifre = self.ui.input_password.text()


         kullanici_kontrolu = self.db.users.find_one({
                "kullanici_adi":girilen_kullanici_adi,
                "sifre":girilen_sifre
         })


         if kullanici_kontrolu:
          self.aktif_kullanici = girilen_kullanici_adi
          self.ui.lbl_welcome.setText(f"Hoşgeldin, {self.aktif_kullanici.upper()}")
          self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
          self.musterileri_veritabanindan_yukle()
         
          self.ui.checkbox_password.setChecked(False)
          self.ui.input_username.clear()
          self.ui.input_password.clear()
          

         elif girilen_kullanici_adi == "" or girilen_sifre == "":
             QMessageBox.warning(self,"Hata","Kullanıcı adı veya şifre boş girilemez!")
         else:
             QMessageBox.warning(self,"Hata","Kullanıcı adı veya şifre yanlış!")     

         
            
            
    

    def sifreyi_goster(self):
        if self.ui.checkbox_password.isChecked():
            self.ui.input_password.setEchoMode(QLineEdit.Normal)
        else:
               self.ui.input_password.setEchoMode(QLineEdit.Password) 
   


    def randiman_hesapla(self):
        try:
            icFindik = float(self.ui.ic_findik_input.text())
            saglamFindik = float(self.ui.saglam_findik_input.text())

            randiman = ((icFindik + saglamFindik)*2) /10
       
            self.ui.randiman_sonuc_label.setText(f"Sonuç: {randiman:.2f}")
        except ValueError:
            QMessageBox.warning(self,"Giriş Hatası","Lütfen sadece sayı giriniz!")  
            self.ui.randiman_sonuc_label.setText("Hatalı Giriş")



    def fiyat_hesapla(self):
        try:
            randiman = float(self.ui.randiman_input.text())
            baz_fiyat = float(self.ui.fiyat_input.text())
            kg = float(self.ui.kg_input.text())
            
            randiman_basi_fiyat = baz_fiyat / 50
            kg_basi_fiyat = randiman_basi_fiyat*randiman

            total_fiyat = kg_basi_fiyat*kg

            self.ui.fiyat_sonuc_label.setText(f"Sonuç: {total_fiyat:.2f} TL")


        except ValueError:
            QMessageBox.warning(self,"Giriş Hatası","Lütfen sadece sayı giriniz!")  
            self.ui.fiyat_sonuc_label.setText("Hatalı Giriş")  



    def randimanHesaplamadanAnaSayfayaGec(self):
      self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
      self.ui.ic_findik_input.clear()
      self.ui.saglam_findik_input.clear()
      self.ui.randiman_sonuc_label.setText("Sonuç:")



    def randimanHesaplamadanFiyatHesaplamayaGec(self): 
          self.ui.stackedWidget.setCurrentWidget(self.ui.page_fiyat)
          self.ui.ic_findik_input.clear()
          self.ui.saglam_findik_input.clear()
          self.ui.randiman_sonuc_label.setText("Sonuç:")



    def randimanHesaplamadanGirisYapaGec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris)
        self.ui.ic_findik_input.clear()
        self.ui.saglam_findik_input.clear()
        self.ui.randiman_sonuc_label.setText("Sonuç:")
    


    def fiyatHesaplamadanAnaSayfayaGec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
        self.ui.randiman_input.clear()
        self.ui.fiyat_input.clear()
        self.ui.kg_input.clear()
        self.ui.fiyat_sonuc_label.setText("Sonuç:")
    


    def fiyatHesaplamadanRandimanHesaplamayaGec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_randiman)
        self.ui.randiman_input.clear()
        self.ui.fiyat_input.clear()
        self.ui.kg_input.clear()
        self.ui.fiyat_sonuc_label.setText("Sonuç:")


    def fiyatHesaplamadanGirisYapaGec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris)
        self.ui.randiman_input.clear()
        self.ui.fiyat_input.clear()
        self.ui.kg_input.clear()
        self.ui.fiyat_sonuc_label.setText("Sonuç:")


    def uyeOldanGirisEkraninaDon(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris)
        self.ui.input_company.clear()
        self.ui.input_new_username.clear()
        self.ui.input_email.clear()
        self.ui.input_new_password.clear()
        self.ui.input_security_key.clear()
        self.ui.check_kvkk.setChecked(False)

   

    def uyeOl(self):
        
                sirket_adi = self.ui.input_company.text()
                kullanici_adi = self.ui.input_new_username.text()
                e_posta = self.ui.input_email.text()
                sifre =   self.ui.input_new_password.text()
                guvenlik_kelimesi = self.ui.input_security_key.text()


                

                if sirket_adi.strip() == "" or kullanici_adi == "" or e_posta == "" or sifre == "" or guvenlik_kelimesi=="":
                    QMessageBox.warning(self,"Hata","Tüm alanları eksiksiz doldurun!")
                    return
                
                if  not(self.ui.check_kvkk.isChecked()):
                        QMessageBox.warning(self,"Hata","Kvkk onayı zorunludur!") 
                        return

                if "@" not in e_posta  :
                    QMessageBox.warning(self,"Hata","Geçersiz e-posta biçimi !")
                    return
                
                if sifre.strip().isalpha():
                    QMessageBox.warning(self,"Hata","Şifre en az 1 tane rakam veya özel karakter içermelidir!")
                    return   

                

                

                kullanici_kontrolu = self.db.users.find_one({
                    "$or":[
                        {"kullanici_adi":kullanici_adi},
                        {"e-posta":e_posta}
                    ]
                })

                if kullanici_kontrolu:
                    QMessageBox.warning(self,"Hata","Bu kullanıcı adı veya e-posta  zaten kayıtlı!")
                    return

                

                

                yeni_kullanici={"sirket_adi":sirket_adi,
                              "kullanici_adi":kullanici_adi,
                              "e-posta":e_posta,
                              "sifre":sifre,
                               "guvenlik_kelimesi":guvenlik_kelimesi}
                    
                
                self.db.users.insert_one(yeni_kullanici)
                  

                QMessageBox.information(self,"Bilgi","Kayıt başarılı , giriş yapabilirsiniz!")
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris)
                self.ui.input_company.clear()
                self.ui.input_new_username.clear()
                self.ui.input_email.clear()
                self.ui.input_new_password.clear()
                self.ui.input_security_key.clear()
                self.ui.check_kvkk.setChecked(False)
    



    def sifreYenile(self):
        kullanici_adi = self.ui.kullanici_adi_input.text()
        guvenlik_kelimesi = self.ui.guvenlik_kelimesi_input.text()

        yeni_sifre = self.ui.yeni_sifre_input.text()


        if kullanici_adi.strip() == "" or guvenlik_kelimesi == "" or yeni_sifre=="":
                    QMessageBox.warning(self,"Hata","Tüm alanları eksiksiz doldurun!")
                    return
        
        if yeni_sifre.strip().isalpha():
                    QMessageBox.warning(self,"Hata","Şifre en az 1 tane rakam veya özel karakter içermelidir!")
                    return 



        kullanici_kontrolu = self.db.users.find_one({
            "kullanici_adi":kullanici_adi,
            "guvenlik_kelimesi":guvenlik_kelimesi
        })


        if kullanici_kontrolu:
            self.db.users.update_one({"kullanici_adi":kullanici_adi},{"$set": {"sifre":yeni_sifre}})
            QMessageBox.information(self,"Bilgi","Şifreniz başarıyla değiştirilmiştir , giriş yapabilirsiniz!")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_giris)

            self.ui.kullanici_adi_input.clear()    
            self.ui.guvenlik_kelimesi_input.clear()  
            self.ui.yeni_sifre_input.clear()

        else:
            QMessageBox.warning(self,"Hata","Böyle bir kullanıcı yok!")  




    def musteriyiTabloyaEkle(self):
        
        asıl_isim = self.ui.input_customer_name.text().strip()
        kontrol_ismi = asıl_isim.replace(" ", "") 

     
        if not kontrol_ismi.isalpha() or asıl_isim == "":
          QMessageBox.warning(self, "Hata", "İsim sadece harf içermelidir!")
          return 
        

        try:
            alinan_toplam_kg = float(self.ui.input_total_kg.text()) 
            randiman = float(self.ui.input_yield.text())
            odenen_kg = float(self.ui.input_paid_kg.text())
            odenen_tutar = float(self.ui.input_paid_amount.text())


            if odenen_kg > alinan_toplam_kg:
                QMessageBox.warning(self,"Hata","Ödenen kg , alınan kg'dan büyük olamaz!")
                return
            

            kalan_kg = alinan_toplam_kg - odenen_kg

           
        except ValueError:
            QMessageBox.warning(self, "Hata", "Sayısal alanlara sadece rakam giriniz!")
            return 

        
        try:
            tarih_string = self.ui.input_date.text()
            tarih = datetime.strptime(tarih_string, "%d.%m.%Y")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Tarih formatı hatalı! (GG.AY.YYYY)")
            return

        
        
        isim_parcalari = asıl_isim.split()

        if len(isim_parcalari) >= 2:
            
            soyad = isim_parcalari[-1]
            
            ad = " ".join(isim_parcalari[:-1])
        else:
            
            ad = asıl_isim
            soyad = ""


        yeni_kayit = {
             "ad":ad,
             "soyad":soyad,
             "toplam_kg":alinan_toplam_kg,
             "randiman":randiman,
             "odenen_kg":odenen_kg,
             "odenen_tutar":odenen_tutar,
             "tarih":tarih,
             "kullanici":self.aktif_kullanici
        }

        self.db.customers.insert_one(yeni_kayit)


        satir = self.ui.table_data.rowCount()
        self.ui.table_data.insertRow(satir)

        self.ui.table_data.setItem(satir,0,QTableWidgetItem(ad))
        self.ui.table_data.setItem(satir,1,QTableWidgetItem(soyad))
        self.ui.table_data.setItem(satir,2,QTableWidgetItem(str(alinan_toplam_kg)))
        self.ui.table_data.setItem(satir,3,QTableWidgetItem(str(randiman)))
        self.ui.table_data.setItem(satir,4,QTableWidgetItem(str(odenen_kg)))
        self.ui.table_data.setItem(satir,5,QTableWidgetItem(str(kalan_kg)))
        self.ui.table_data.setItem(satir,6,QTableWidgetItem(str(odenen_tutar)))
        self.ui.table_data.setItem(satir,7,QTableWidgetItem(tarih_string))

        QMessageBox.information(self, "Başarılı", f"{ad} {soyad} başarıyla eklendi.")

        self.ui.input_customer_name.clear()
        self.ui.input_total_kg.clear()
        self.ui.input_paid_kg.clear()
        self.ui.input_yield.clear()
        self.ui.input_paid_amount.clear()
        self.ui.input_date.clear()



    def musterileri_veritabanindan_yukle(self):
        
        self.ui.table_data.setRowCount(0)  

        
        sorgu = {"kullanici": self.aktif_kullanici}
        veriler = self.db.customers.find(sorgu)

        for veri in veriler:
            satir = self.ui.table_data.rowCount() 
            self.ui.table_data.insertRow(satir) 
            
            
            self.ui.table_data.setItem(satir, 0, QTableWidgetItem(veri.get("ad", "")))
            self.ui.table_data.setItem(satir, 1, QTableWidgetItem(veri.get("soyad", "")))
            self.ui.table_data.setItem(satir, 2, QTableWidgetItem(str(veri.get("toplam_kg", 0))))
            self.ui.table_data.setItem(satir, 3, QTableWidgetItem(str(veri.get("randiman", 0))))
            self.ui.table_data.setItem(satir, 4, QTableWidgetItem(str(veri.get("odenen_kg", 0))))
            
           
            kalan_kg = veri.get("toplam_kg", 0) - veri.get("odenen_kg", 0)
            self.ui.table_data.setItem(satir, 5, QTableWidgetItem(str(kalan_kg)))
            
            self.ui.table_data.setItem(satir, 6, QTableWidgetItem(str(veri.get("odenen_tutar", 0))))
            
            
            tarih  = veri.get("tarih")
            if tarih:
                t_metin = tarih.strftime("%d.%m.%Y")  
                self.ui.table_data.setItem(satir, 7, QTableWidgetItem(t_metin))




    
    def musteri_verilerini_guncelle(self):
       
        if self.guncelleme_modu == False:
            secili_satir = self.ui.table_data.currentRow()

            if secili_satir == -1:
                QMessageBox.warning(self, "Hata", "Lütfen önce tablodan güncellenecek satırı seçin!")
                return

            
            ad = self.ui.table_data.item(secili_satir, 0).text()
            soyad = self.ui.table_data.item(secili_satir, 1).text()
            self.ui.input_customer_name.setText(f"{ad} {soyad}")
            self.ui.input_total_kg.setText(self.ui.table_data.item(secili_satir, 2).text())
            self.ui.input_yield.setText(self.ui.table_data.item(secili_satir, 3).text())
            self.ui.input_paid_kg.setText(self.ui.table_data.item(secili_satir, 4).text())
            self.ui.input_paid_amount.setText(self.ui.table_data.item(secili_satir, 6).text())
            self.ui.input_date.setText(self.ui.table_data.item(secili_satir, 7).text())

            
            self.eski_ad = ad
            self.eski_soyad = soyad
            
           
            self.guncelleme_modu = True
            self.ui.btn_update.setText("Değişikliği Onayla") 
            QMessageBox.information(self, "Bilgi", "Düzenleme yapıp tekrar butona basın.")

       
        else:
            
            if float(self.ui.input_paid_kg.text()) > float(self.ui.input_total_kg.text()):
                QMessageBox.warning(self,"Hata","Ödenen kg , alınan kg'dan büyük olamaz!")
                return
            
            try:
                tam_isim = self.ui.input_customer_name.text().strip().split()
                yeni_soyad = tam_isim[-1] if len(tam_isim) >= 2 else ""
                yeni_ad = " ".join(tam_isim[:-1]) if len(tam_isim) >= 2 else tam_isim[0]

                sorgu = {"ad": self.eski_ad, "soyad": self.eski_soyad, "kullanici": self.aktif_kullanici}
                
                yeni_degerler = {"$set": {
                    "ad": yeni_ad,
                    "soyad": yeni_soyad,
                    "toplam_kg": float(self.ui.input_total_kg.text()),
                    "randiman": float(self.ui.input_yield.text()),
                    "odenen_kg": float(self.ui.input_paid_kg.text()),
                    "odenen_tutar": float(self.ui.input_paid_amount.text()),
                    "tarih": datetime.strptime(self.ui.input_date.text(), "%d.%m.%Y"),
                    "kullanici":self.aktif_kullanici
                }}

                self.db.customers.update_one(sorgu, yeni_degerler)
                
                
                self.guncelleme_modu = False
                self.ui.btn_update.setText("Güncelle")
                self.musterileri_veritabanindan_yukle() 
                self.ui.input_customer_name.clear() 
                self.ui.input_total_kg.clear()
                self.ui.input_yield.clear()
                self.ui.input_paid_kg.clear()
                self.ui.input_paid_amount.clear()
                self.ui.input_date.clear()
                
                QMessageBox.information(self, "Başarılı", "Kayıt güncellendi!")

            except Exception as e:
                QMessageBox.warning(self, "Hata", "Güncelleme sırasında hata oluştu!")



    def musteriyi_sil(self):
        secili_satir = self.ui.table_data.currentRow()

        if secili_satir == -1:
            QMessageBox.warning(self,"Hata","Lütfen önce silinecek müşteriyi seçiniz!")
            return
        
        try : 
               ad = self.ui.table_data.item(secili_satir,0).text()
               soyad = self.ui.table_data.item(secili_satir,1).text()

               onay = QMessageBox.question(self,"Silme Onayı",f"{ad} {soyad} isimli müşteriyi silmek istediğinize emin misiniz?",QMessageBox.Yes | QMessageBox.No)

               if onay == QMessageBox.Yes:
            
                self.db.customers.delete_one(
                {"ad":ad,
                "soyad":soyad,
                "kullanici":self.aktif_kullanici
                 }
                 )

                self.ui.table_data.removeRow(secili_satir)
                QMessageBox.information(self,"Başarılı",f"{ad} {soyad} kaydı sistemden silindi.")    
        
        except Exception as e:
            QMessageBox.critical(self, "Veritabanı Hatası", f"İşlem başarısız oldu! Hata: {str(e)}")
             
         


        
    
    
    def closeEvent(self,event):
        cevap = QMessageBox.question(self,"Çıkış","Çıkılsın mı?",QMessageBox.Yes | QMessageBox.No)
        

        if cevap == QMessageBox.Yes:
            self.db.close_connection() 
            event.accept() 

        else:
            event.ignore() 

        

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = FindikTakip()
    win.show()
    sys.exit(app.exec_())
    
