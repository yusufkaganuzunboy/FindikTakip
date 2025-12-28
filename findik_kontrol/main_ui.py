from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 729)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("/* 1. ANA ARKA PLAN VE GENEL AYARLAR */\n"
"QMainWindow, QStackedWidget, QWidget#page_giris, QWidget#page_kayit, QWidget#page_dashboard{\n"
"    background-color: #0d1b2a;\n"
"    border: none;\n"
"}\n"
"\n"
"/* 2. TÜM GİRİŞ KUTULARI (LineEdit) */\n"
"QLineEdit {\n"
"    background-color: #1b263b;\n"
"    border: 1px solid #415a77;\n"
"    border-radius: 10px;\n"
"    padding: 10px 15px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"}\n"
"\n"
"/* 3. ANA AKSİYON BUTONLARI (Giriş Yap, Kaydı Tamamla) */\n"
"QPushButton#login_button, QPushButton#signup_submit_button {\n"
"    background-color: #ffffff;\n"
"    color: #0d1b2a;\n"
"    border-radius: 25px; \n"
"    font-weight: bold;\n"
"    min-height: 50px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton#login_button:hover, QPushButton#signup_submit_button:hover {\n"
"    background-color: #f2f2f2;\n"
"}\n"
"\n"
"/* BASILMA HİSSİ (Dikey Çökme) */\n"
"QPushButton#login_button:pressed, QPushButton#signup_submit_button:pressed {\n"
"    background-color: #d1d1d1;\n"
"    padding-top: 15px; \n"
"    padding-bottom: 5px;\n"
"}\n"
"\n"
"/* 4. LİNK GÖRÜNÜMLÜ BUTONLAR (Üye Ol, Şifremi Unuttum, Geri Dön) */\n"
"QPushButton#forgot_button, QPushButton#signup_button, QPushButton#back_to_login_button {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #4a90e2;\n"
"    font-size: 13px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton#forgot_button:hover, QPushButton#signup_button:hover, QPushButton#back_to_login_button:hover {\n"
"    color: #63a4ff;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"/* 5. ANA MENÜ (page_dashboard) ÖZEL STİLLERİ */\n"
"\n"
"/* Üst Sekme Butonları */\n"
"#page_dashboard QPushButton {\n"
"    background-color: #1b263b;\n"
"    color: white;\n"
"    border: 1px solid #415a77;\n"
"    border-radius: 10px;\n"
"    min-height: 45px;\n"
"}\n"
"\n"
"#page_dashboard QPushButton:hover {\n"
"    background-color: #4a90e2;\n"
"}\n"
"\n"
"/* Tablo Tasarımı */\n"
"QTableWidget {\n"
"    background-color: #0d1b2a;\n"
"    alternate-background-color: #1b263b;\n"
"    gridline-color: #415a77;\n"
"    color: white;\n"
"    border: 1px solid #415a77;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1b263b;\n"
"    color: #4a90e2;\n"
"    padding: 8px;\n"
"    border: 1px solid #415a77;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* İşlem Butonları (Renkli) */\n"
"QPushButton#btn_delete { background-color: #e63946 !important; color: white !important; }\n"
"QPushButton#btn_update { background-color: #f39c12 !important; color: white !important; }\n"
"QPushButton#btn_save   { background-color: #3498db !important; color: white !important; }\n"
"\n"
"/* Çıkış Yap Butonu */\n"
"QPushButton#btn_logout {\n"
"    background-color: #e63946;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* SADECE TABLO KÖŞESİNDEKİ BEYAZLIĞI YOK EDER */\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #0d1b2a !important; /* Arka plan renginle aynı yaptık */\n"
"    border: none !important;\n"
"}\n"
"\n"
"/* Tablonun başlık alanındaki boşlukları da arka plana uydurur */\n"
"QHeaderView {\n"
"    background-color: transparent !important;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1b263b !important;\n"
"}\n"
"\n"
"/* 1. ÇIKIŞ YAP BUTONU (btn_logout) - KIRMIZI VE BASILMA EFEKTİ */\n"
"QPushButton#btn_logout:hover {\n"
"    background-color: #ff4d4d !important;\n"
"}\n"
"\n"
"QPushButton#btn_logout:pressed {\n"
"    background-color: #b32d2d !important;\n"
"    padding-top: 5px; /* Yazıyı aşağı iterek çökme hissi verir */\n"
"    padding-bottom: 2px;\n"
"}\n"
"\n"
"/* 2. ANA İŞLEM BUTONLARI (Sil, Güncelle, Kaydet) BASILMA EFEKTİ */\n"
"QPushButton#btn_delete:pressed, \n"
"QPushButton#btn_update:pressed, \n"
"QPushButton#btn_save:pressed {\n"
"    padding-top: 5px;\n"
"    padding-bottom: 2px;\n"
"    /* Hafif koyulaşma efekti */\n"
"    background-color: rgba(0, 0, 0, 0.2); \n"
"}\n"
"\n"
"/* 3. ÜST SEKME BUTONLARI (btn_tab_...) BASILMA EFEKTİ */\n"
"\n"
"QPushButton#btn_tab_customer:pressed,\n"
"\n"
"QPushButton#btn_tab_yield:pressed,\n"
"\n"
"QPushButton#btn_tab_price:pressed {\n"
"\n"
"background-color: #0d1b2a !important; /* Basılınca daha koyu olur */\n"
"\n"
"padding-top: 3px;\n"
"\n"
"} \n"
"\n"
"/* 4. TABLO KÖŞESİNDEKİ O BEYAZLIĞI YOK EDEN KESİN KOD */\n"
"/* Bu kod tablonun sağındaki o beyaz kareyi arka plana gömer */\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #0d1b2a !important; \n"
"    border: none !important;\n"
"}\n"
"\n"
"/* Tablonun boş kalan alanlarını da lacivert yapalım */\n"
"QTableWidget {\n"
"    background-color: #0d1b2a !important;\n"
"    outline: none !important;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: #0d1b2a !important;\n"
"}\n"
"\n"
"/* 1. SEÇİLİ SATIRIN BEYAZ OLMASINI ENGELLER */\n"
"QTableWidget::item:selected {\n"
"    background-color: #4a90e2 !important; /* Seçince şık bir mavi olur */\n"
"    color: white !important;              /* Yazı beyaz kalır */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* 2. YAZILARIN HÜCRE İÇİNDE DÜZGÜN DURMASI */\n"
"QTableWidget::item {\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* 3. TÜM BUTONLARA BASILMA EFEKTİ (GENEL) */\n"
"QPushButton:pressed {\n"
"    padding-top: 5px !important;\n"
"    padding-bottom: 2px !important;\n"
"}\n"
"\n"
"/* 4. TABLO KÖŞESİ VE GENEL KARANLIKLIK */\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #0d1b2a !important;\n"
"}\n"
"\n"
"/* 1. SEÇİM RENGİNİ SABİTLE (TIKLAYINCA MAVİ) */\n"
"QTableWidget::item:selected {\n"
"    background-color: #4a90e2 !important; \n"
"    color: white !important;\n"
"}\n"
"\n"
"/* 2. TABLO ODAKTA DEĞİLKEN SEÇİMİ SÖNDÜR (BURASI KRİTİK) */\n"
"/* Boşluğa veya başka yere tıkladığında tablonun \"seçili\" görüntüsünü griye çeker veya siler */\n"
"QTableWidget:focus {\n"
"    border: 1px solid #4a90e2 !important; /* Tablo seçiliyken kenarı parlasın */\n"
"}\n"
"\n"
"/* 3. TIKLAMA HİSSİNİN TAKILI KALMAMASI İÇİN */\n"
"QTableWidget {\n"
"    selection-background-color: #4a90e2;\n"
"    selection-color: white;\n"
"    show-decoration-selected: 1;\n"
"    outline: 0; /* Kenardaki kesikli çizgiyi yok eder */\n"
"}\n"
"\n"
"/* Genel Sayfa Arka Planı (page_randiman) */\n"
"#page_randiman {\n"
"    background-color: #0d1b2a;\n"
"}\n"
"\n"
"/* Randıman Başlığı */\n"
"QLabel#randiman_hesaplama_baslik_label {\n"
"    color: #ffffff;\n"
"    font-size: 32px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignCenter\';\n"
"    margin-bottom: 20px;\n"
"}\n"
"\n"
"/* Çıkış Yap Butonu (Kırmızı ve Köşede) */\n"
"QPushButton#randiman_cikis_button {\n"
"    background-color: #e63946;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"    padding: 5px 15px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton#randiman_cikis_button:hover {\n"
"    background-color: #ff4d4d;\n"
"}\n"
"\n"
"/* Giriş Kutuları (LineEdit) */\n"
"QLineEdit#ic_findik_input, QLineEdit#saglam_findik_input {\n"
"    background-color: #1b263b;\n"
"    border: 2px solid #415a77;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    min-height: 35px;\n"
"}\n"
"\n"
"QLineEdit#ic_findik_input:focus, QLineEdit#saglam_findik_input:focus {\n"
"    border: 2px solid #4a90e2;\n"
"}\n"
"\n"
"/* Randıman Hesapla Butonu */\n"
"QPushButton#randiman_hesapla_button {\n"
"    background-color: #ffffff;\n"
"    color: #0d1b2a;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    padding: 10px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QPushButton#randiman_hesapla_button:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"/* Sonuç Etiketi (Büyük ve Yeşil Yazı) */\n"
"QLabel#randiman_sonuc_label {\n"
"    color: #2ecc71;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignCenter\';\n"
"    margin-top: 15px;\n"
"}\n"
"\n"
"/* Eğer çerçeve içindeki GroupBox\'ı isimlendirdiysen (Örn: groupBox) */\n"
"QGroupBox {\n"
"    border: 1px solid #415a77;\n"
"    border-radius: 15px;\n"
"    margin-top: 20px;\n"
"    background-color: rgba(27, 38, 59, 0.5); /* Hafif şeffaf iç panel */\n"
"}\n"
"\n"
"/* ÇIKIŞ YAP BUTONU BASILMA EFEKTİ */\n"
"QPushButton#randiman_cikis_button:pressed {\n"
"    background-color: #b32d2d !important; /* Daha koyu kırmızı olur */\n"
"    padding-top: 5px !important;           /* Yazıyı aşağı iterek çökme hissi verir */\n"
"    padding-bottom: 2px !important;\n"
"}\n"
"\n"
"/* RANDIMAN HESAPLA BUTONU BASILMA EFEKTİ */\n"
"QPushButton#randiman_hesapla_button:pressed {\n"
"    background-color: #d1d1d1 !important; /* Basılınca hafif grileşir */\n"
"    padding-top: 15px !important;          /* Yazıyı aşağı iterek çökme hissi verir */\n"
"    padding-bottom: 5px !important;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* ÜST NAVİGASYON BUTONLARINI DÜZENLE */\n"
"#page_randiman QPushButton#anasayfa_button, \n"
"#page_randiman QPushButton#fiyathesaplama_sayfa_button, \n"
"#page_randiman QPushButton#randiman_cikis_button {\n"
"    min-height: 45px;          /* Hafif büyüttük */\n"
"    border-radius: 12px;       /* Köşeleri yuvarladık */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    margin: 5px;               /* Birbirlerine yapışmasınlar */\n"
"}\n"
"\n"
"/* Çıkış butonuna özel basılma hissi (sadece hafif çökme) */\n"
"#page_randiman QPushButton:pressed {\n"
"    padding-top: 4px;\n"
"    background-color: #e0e0e0; /* Hafif bir renk değişimi yeter */\n"
"}\n"
"\n"
"#page_randiman QPushButton#randiman_cikis_button:pressed {\n"
"    background-color: #c0392b; /* Kırmızının basılmış hali */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* --- page_fiyat: ÜST NAVİGASYON (OKUNAKLI VE OVAL) --- */\n"
"#page_fiyat QPushButton#anasayfa_button_fiyat_hesaplamadan, \n"
"#page_fiyat QPushButton#randiman_hesaplama_button_fiyattan, \n"
"#page_fiyat QPushButton#cikisyap_button_fiyat {\n"
"    min-height: 50px;           /* Butonları dikeyde büyüttük */\n"
"    border-radius: 20px;        /* Köşeleri ovalleştirdik */\n"
"    font-size: 14px;            /* Yazı boyutunu okunur yaptık */\n"
"    font-weight: bold;\n"
"    color: white !important;    /* Yazı rengini beyaz yaptık */\n"
"    padding: 0 20px;            /* Yazı etrafına genişlik verdik */\n"
"}\n"
"\n"
"/* Üst Butonlar Basılma Hissi */\n"
"#page_fiyat QPushButton#anasayfa_button_fiyat_hesaplamadan:pressed, \n"
"#page_fiyat QPushButton#randiman_hesaplama_button_fiyattan:pressed {\n"
"    background-color: #2c3e50;  /* Basılınca hafif koyulaşır */\n"
"    padding-top: 6px;           /* Çökme efekti */\n"
"}\n"
"\n"
"/* Çıkış Butonuna Özel Kırmızı (page_fiyat) */\n"
"#page_fiyat QPushButton#cikisyap_button_fiyat {\n"
"    background-color: #e63946 !important;\n"
"}\n"
"\n"
"#page_fiyat QPushButton#cikisyap_button_fiyat:pressed {\n"
"    background-color: #b32d2d !important;\n"
"    padding-top: 6px;\n"
"}\n"
"\n"
"/* --- PAGE 5: ANA HESAPLA BUTONU (EN ALTTAKI) --- */\n"
"#page_fiyat QPushButton#fiyathesapla_button {\n"
"    min-height: 70px;           /* Diğerlerinden daha büyük */\n"
"    border-radius: 35px;        /* Tam oval / Stadyum tipi */\n"
"    font-size: 20px;            /* Yazı devleşti */\n"
"    font-weight: bold;\n"
"    background-color: #ffffff !important; /* Beyaz gövde */\n"
"    color: #0d1b2a !important;   /* Koyu yazı */\n"
"    margin: 20px;\n"
"}\n"
"\n"
"/* Ana Buton Basılma Hissi */\n"
"#page_fiyat QPushButton#fiyathesapla_button:pressed {\n"
"    background-color: #d1d1d1 !important;\n"
"    padding-top: 10px;          /* Daha derin çökme efekti */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* --- ŞİFREYİ GÜNCELLE (BÜYÜK BEYAZ OVAL BUTON) --- */\n"
"QPushButton#sifreyi_guncelle_button {\n"
"    background-color: #ffffff;    /* Beyaz gövde */\n"
"    color: #0d1b2a;               /* Koyu yazı */\n"
"    border-radius: 28px;          /* Tam oval / Stadyum tipi */\n"
"    min-height: 56px;             /* İri ve güven veren boyut */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    margin-top: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#sifreyi_guncelle_button:pressed {\n"
"    background-color: #d1d1d1;    /* Basılma rengi */\n"
"    padding-top: 8px;             /* Çökme efekti */\n"
"}\n"
"\n"
"/* --- GİRİŞ EKRANINA DÖN (MAVİ YAZI - ÇİZGİSİZ) --- */\n"
"QPushButton#giris_ekrana_don_button {\n"
"    background: transparent;      /* Arka plan yok */\n"
"    border: none;                 /* Çerçeve yok */\n"
"    color: #4a90e2;               /* İstediğin mavi tonu */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-decoration: none;        /* Alt çizgiyi kaldırdık */\n"
"    min-height: 30px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"/* Üzerine gelince beyaz olmasın, sadece hafif parlasın (isteğe bağlı) */\n"
"QPushButton#giris_ekrana_don_button:hover {\n"
"    color: #5dade2;               /* Mavinin bir tık açığı (beyaz değil) */\n"
"}\n"
"\n"
"QPushButton#giris_ekrana_don_button:pressed {\n"
"    color: #2e86de;               /* Basınca mavinin bir tık koyusu */\n"
"    padding-top: 2px;             /* Çok hafif tıklama hissi */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_giris = QtWidgets.QWidget()
        self.page_giris.setObjectName("page_giris")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_giris)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_logo = QtWidgets.QLabel(self.page_giris)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setMaximumSize(QtCore.QSize(150, 150))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("FındıkKontrolKapak.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_8.addWidget(self.label_logo)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.input_username = QtWidgets.QLineEdit(self.page_giris)
        self.input_username.setObjectName("input_username")
        self.gridLayout_4.addWidget(self.input_username, 1, 0, 1, 1)
        self.forgot_button = QtWidgets.QPushButton(self.page_giris)
        self.forgot_button.setObjectName("forgot_button")
        self.gridLayout_4.addWidget(self.forgot_button, 5, 0, 1, 1)
        self.input_password = QtWidgets.QLineEdit(self.page_giris)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.gridLayout_4.addWidget(self.input_password, 2, 0, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.page_giris)
        self.login_button.setObjectName("login_button")
        self.gridLayout_4.addWidget(self.login_button, 4, 0, 1, 1)
        self.checkbox_password = QtWidgets.QCheckBox(self.page_giris)
        self.checkbox_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkbox_password.setObjectName("checkbox_password")
        self.gridLayout_4.addWidget(self.checkbox_password, 3, 0, 1, 1)
        self.signup_button = QtWidgets.QPushButton(self.page_giris)
        self.signup_button.setObjectName("signup_button")
        self.gridLayout_4.addWidget(self.signup_button, 6, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_giris)
        self.page_kayit = QtWidgets.QWidget()
        self.page_kayit.setObjectName("page_kayit")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_kayit)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uye_ol_baslik_label = QtWidgets.QLabel(self.page_kayit)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.uye_ol_baslik_label.setFont(font)
        self.uye_ol_baslik_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.uye_ol_baslik_label.setAlignment(QtCore.Qt.AlignCenter)
        self.uye_ol_baslik_label.setObjectName("uye_ol_baslik_label")
        self.verticalLayout_3.addWidget(self.uye_ol_baslik_label)
        self.input_company = QtWidgets.QLineEdit(self.page_kayit)
        self.input_company.setObjectName("input_company")
        self.verticalLayout_3.addWidget(self.input_company)
        self.input_new_username = QtWidgets.QLineEdit(self.page_kayit)
        self.input_new_username.setObjectName("input_new_username")
        self.verticalLayout_3.addWidget(self.input_new_username)
        self.input_email = QtWidgets.QLineEdit(self.page_kayit)
        self.input_email.setObjectName("input_email")
        self.verticalLayout_3.addWidget(self.input_email)
        self.input_new_password = QtWidgets.QLineEdit(self.page_kayit)
        self.input_new_password.setObjectName("input_new_password")
        self.verticalLayout_3.addWidget(self.input_new_password)
        self.input_security_key = QtWidgets.QLineEdit(self.page_kayit)
        self.input_security_key.setObjectName("input_security_key")
        self.verticalLayout_3.addWidget(self.input_security_key)
        self.check_kvkk = QtWidgets.QCheckBox(self.page_kayit)
        self.check_kvkk.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_kvkk.setObjectName("check_kvkk")
        self.verticalLayout_3.addWidget(self.check_kvkk)
        self.signup_submit_button = QtWidgets.QPushButton(self.page_kayit)
        self.signup_submit_button.setObjectName("signup_submit_button")
        self.verticalLayout_3.addWidget(self.signup_submit_button)
        self.back_to_login_button = QtWidgets.QPushButton(self.page_kayit)
        self.back_to_login_button.setObjectName("back_to_login_button")
        self.verticalLayout_3.addWidget(self.back_to_login_button)
        self.stackedWidget.addWidget(self.page_kayit)
        self.page_dashboard = QtWidgets.QWidget()
        self.page_dashboard.setObjectName("page_dashboard")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_dashboard)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_welcome = QtWidgets.QLabel(self.page_dashboard)
        self.lbl_welcome.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_welcome.setObjectName("lbl_welcome")
        self.horizontalLayout.addWidget(self.lbl_welcome)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_logout = QtWidgets.QPushButton(self.page_dashboard)
        self.btn_logout.setStyleSheet("background-color: rgb(238, 0, 0);")
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout.addWidget(self.btn_logout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_tab_customer = QtWidgets.QPushButton(self.page_dashboard)
        self.btn_tab_customer.setObjectName("btn_tab_customer")
        self.horizontalLayout_2.addWidget(self.btn_tab_customer)
        self.btn_tab_yield = QtWidgets.QPushButton(self.page_dashboard)
        self.btn_tab_yield.setObjectName("btn_tab_yield")
        self.horizontalLayout_2.addWidget(self.btn_tab_yield)
        self.btn_tab_price = QtWidgets.QPushButton(self.page_dashboard)
        self.btn_tab_price.setObjectName("btn_tab_price")
        self.horizontalLayout_2.addWidget(self.btn_tab_price)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_paid_amount = QtWidgets.QLineEdit(self.page_dashboard)
        self.input_paid_amount.setObjectName("input_paid_amount")
        self.gridLayout_2.addWidget(self.input_paid_amount, 1, 1, 1, 1)
        self.input_total_kg = QtWidgets.QLineEdit(self.page_dashboard)
        self.input_total_kg.setObjectName("input_total_kg")
        self.gridLayout_2.addWidget(self.input_total_kg, 0, 1, 1, 1)
        self.input_customer_name = QtWidgets.QLineEdit(self.page_dashboard)
        self.input_customer_name.setObjectName("input_customer_name")
        self.gridLayout_2.addWidget(self.input_customer_name, 0, 0, 1, 1)
        self.input_paid_kg = QtWidgets.QLineEdit(self.page_dashboard)
        self.input_paid_kg.setObjectName("input_paid_kg")
        self.gridLayout_2.addWidget(self.input_paid_kg, 1, 0, 1, 1)
        self.input_yield = QtWidgets.QLineEdit(self.page_dashboard)
        self.input_yield.setObjectName("input_yield")
        self.gridLayout_2.addWidget(self.input_yield, 0, 2, 1, 1)
        self.input_date = QtWidgets.QLineEdit(self.page_dashboard)
        self.input_date.setObjectName("input_date")
        self.gridLayout_2.addWidget(self.input_date, 1, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_delete = QtWidgets.QPushButton(self.page_dashboard)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_3.addWidget(self.btn_delete)
        self.btn_update = QtWidgets.QPushButton(self.page_dashboard)
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_3.addWidget(self.btn_update)
        self.btn_save = QtWidgets.QPushButton(self.page_dashboard)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_3.addWidget(self.btn_save)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.table_data = QtWidgets.QTableWidget(self.page_dashboard)
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(8)
        self.table_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(7, item)
        self.table_data.horizontalHeader().setDefaultSectionSize(100)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.table_data)
        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_randiman = QtWidgets.QWidget()
        self.page_randiman.setObjectName("page_randiman")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_randiman)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.anasayfa_button = QtWidgets.QPushButton(self.page_randiman)
        self.anasayfa_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.anasayfa_button.setObjectName("anasayfa_button")
        self.horizontalLayout_6.addWidget(self.anasayfa_button)
        self.fiyathesaplama_sayfa_button = QtWidgets.QPushButton(self.page_randiman)
        self.fiyathesaplama_sayfa_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.fiyathesaplama_sayfa_button.setObjectName("fiyathesaplama_sayfa_button")
        self.horizontalLayout_6.addWidget(self.fiyathesaplama_sayfa_button)
        self.randiman_cikis_button = QtWidgets.QPushButton(self.page_randiman)
        self.randiman_cikis_button.setStyleSheet("background-color: rgb(238, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.randiman_cikis_button.setObjectName("randiman_cikis_button")
        self.horizontalLayout_6.addWidget(self.randiman_cikis_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.randiman_hesaplama_baslik_label = QtWidgets.QLabel(self.page_randiman)
        self.randiman_hesaplama_baslik_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.randiman_hesaplama_baslik_label.setAlignment(QtCore.Qt.AlignCenter)
        self.randiman_hesaplama_baslik_label.setObjectName("randiman_hesaplama_baslik_label")
        self.gridLayout_3.addWidget(self.randiman_hesaplama_baslik_label, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page_randiman)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_numune = QtWidgets.QLabel(self.groupBox)
        self.label_numune.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_numune.setObjectName("label_numune")
        self.verticalLayout_7.addWidget(self.label_numune)
        self.ic_findik_input = QtWidgets.QLineEdit(self.groupBox)
        self.ic_findik_input.setObjectName("ic_findik_input")
        self.verticalLayout_7.addWidget(self.ic_findik_input)
        self.saglam_findik_input = QtWidgets.QLineEdit(self.groupBox)
        self.saglam_findik_input.setObjectName("saglam_findik_input")
        self.verticalLayout_7.addWidget(self.saglam_findik_input)
        self.randiman_hesapla_button = QtWidgets.QPushButton(self.groupBox)
        self.randiman_hesapla_button.setObjectName("randiman_hesapla_button")
        self.verticalLayout_7.addWidget(self.randiman_hesapla_button)
        self.randiman_sonuc_label = QtWidgets.QLabel(self.groupBox)
        self.randiman_sonuc_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.randiman_sonuc_label.setObjectName("randiman_sonuc_label")
        self.verticalLayout_7.addWidget(self.randiman_sonuc_label)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_randiman)
        self.page_fiyat = QtWidgets.QWidget()
        self.page_fiyat.setObjectName("page_fiyat")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_fiyat)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.anasayfa_button_fiyat_hesaplamadan = QtWidgets.QPushButton(self.page_fiyat)
        self.anasayfa_button_fiyat_hesaplamadan.setStyleSheet("color: rgb(255, 255, 255);")
        self.anasayfa_button_fiyat_hesaplamadan.setObjectName("anasayfa_button_fiyat_hesaplamadan")
        self.horizontalLayout_7.addWidget(self.anasayfa_button_fiyat_hesaplamadan)
        self.randiman_hesaplama_button_fiyattan = QtWidgets.QPushButton(self.page_fiyat)
        self.randiman_hesaplama_button_fiyattan.setStyleSheet("color: rgb(255, 255, 255);")
        self.randiman_hesaplama_button_fiyattan.setObjectName("randiman_hesaplama_button_fiyattan")
        self.horizontalLayout_7.addWidget(self.randiman_hesaplama_button_fiyattan)
        self.cikisyap_button_fiyat = QtWidgets.QPushButton(self.page_fiyat)
        self.cikisyap_button_fiyat.setStyleSheet("background-color: rgb(238, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.cikisyap_button_fiyat.setObjectName("cikisyap_button_fiyat")
        self.horizontalLayout_7.addWidget(self.cikisyap_button_fiyat)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.fiyat_hesaplama_baslik_label = QtWidgets.QLabel(self.page_fiyat)
        self.fiyat_hesaplama_baslik_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.fiyat_hesaplama_baslik_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fiyat_hesaplama_baslik_label.setObjectName("fiyat_hesaplama_baslik_label")
        self.gridLayout_5.addWidget(self.fiyat_hesaplama_baslik_label, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_fiyat)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.randiman_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.randiman_input.setObjectName("randiman_input")
        self.verticalLayout_8.addWidget(self.randiman_input)
        self.fiyat_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.fiyat_input.setObjectName("fiyat_input")
        self.verticalLayout_8.addWidget(self.fiyat_input)
        self.kg_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.kg_input.setObjectName("kg_input")
        self.verticalLayout_8.addWidget(self.kg_input)
        self.fiyathesapla_button = QtWidgets.QPushButton(self.groupBox_2)
        self.fiyathesapla_button.setObjectName("fiyathesapla_button")
        self.verticalLayout_8.addWidget(self.fiyathesapla_button)
        self.fiyat_sonuc_label = QtWidgets.QLabel(self.groupBox_2)
        self.fiyat_sonuc_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.fiyat_sonuc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fiyat_sonuc_label.setObjectName("fiyat_sonuc_label")
        self.verticalLayout_8.addWidget(self.fiyat_sonuc_label)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_fiyat)
        self.page_sifre_sifirlama = QtWidgets.QWidget()
        self.page_sifre_sifirlama.setObjectName("page_sifre_sifirlama")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_sifre_sifirlama)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.sifre_yenileme_baslik_label = QtWidgets.QLabel(self.page_sifre_sifirlama)
        self.sifre_yenileme_baslik_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.sifre_yenileme_baslik_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sifre_yenileme_baslik_label.setObjectName("sifre_yenileme_baslik_label")
        self.verticalLayout_9.addWidget(self.sifre_yenileme_baslik_label)
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_sifre_sifirlama)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kullanici_adi_input = QtWidgets.QLineEdit(self.groupBox_3)
        self.kullanici_adi_input.setObjectName("kullanici_adi_input")
        self.verticalLayout_2.addWidget(self.kullanici_adi_input)
        self.guvenlik_kelimesi_input = QtWidgets.QLineEdit(self.groupBox_3)
        self.guvenlik_kelimesi_input.setObjectName("guvenlik_kelimesi_input")
        self.verticalLayout_2.addWidget(self.guvenlik_kelimesi_input)
        self.yeni_sifre_input = QtWidgets.QLineEdit(self.groupBox_3)
        self.yeni_sifre_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.yeni_sifre_input.setObjectName("yeni_sifre_input")
        self.verticalLayout_2.addWidget(self.yeni_sifre_input)
        self.sifreyi_guncelle_button = QtWidgets.QPushButton(self.groupBox_3)
        self.sifreyi_guncelle_button.setObjectName("sifreyi_guncelle_button")
        self.verticalLayout_2.addWidget(self.sifreyi_guncelle_button)
        self.giris_ekrana_don_button = QtWidgets.QPushButton(self.groupBox_3)
        self.giris_ekrana_don_button.setObjectName("giris_ekrana_don_button")
        self.verticalLayout_2.addWidget(self.giris_ekrana_don_button)
        self.verticalLayout_9.addWidget(self.groupBox_3)
        self.stackedWidget.addWidget(self.page_sifre_sifirlama)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FındıkKontrol"))
        self.input_username.setPlaceholderText(_translate("MainWindow", "Kullanıcı adı"))
        self.forgot_button.setText(_translate("MainWindow", "Şifreni mi unuttun?"))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Şifre"))
        self.login_button.setText(_translate("MainWindow", "Giriş yap"))
        self.checkbox_password.setText(_translate("MainWindow", "Şifreyi göster"))
        self.signup_button.setText(_translate("MainWindow", "Üye ol"))
        self.uye_ol_baslik_label.setText(_translate("MainWindow", "ÜYE OL"))
        self.input_company.setPlaceholderText(_translate("MainWindow", "Şirket adı"))
        self.input_new_username.setPlaceholderText(_translate("MainWindow", "Kullanıcı adı"))
        self.input_email.setPlaceholderText(_translate("MainWindow", "E-posta"))
        self.input_new_password.setPlaceholderText(_translate("MainWindow", "Şifre "))
        self.input_security_key.setPlaceholderText(_translate("MainWindow", "Güvenlik kelimesi ( Şifre sıfırlama için)"))
        self.check_kvkk.setText(_translate("MainWindow", "Kişisel verilerimin işlenmesini kabul ediyorum.(KVKK)"))
        self.signup_submit_button.setText(_translate("MainWindow", "Kaydı Tamamla"))
        self.back_to_login_button.setText(_translate("MainWindow", "Giriş Ekranına Dön"))
        self.lbl_welcome.setText(_translate("MainWindow", "        HOŞGELDİN,[KULLANICI ADI]     "))
        self.btn_logout.setText(_translate("MainWindow", "     Çıkış Yap  "))
        self.btn_tab_customer.setText(_translate("MainWindow", "Tüccar / Müşteri İşlemleri"))
        self.btn_tab_yield.setText(_translate("MainWindow", "Randıman Hesaplama"))
        self.btn_tab_price.setText(_translate("MainWindow", "Fiyat Hesaplama"))
        self.input_paid_amount.setPlaceholderText(_translate("MainWindow", "Ödenen Tutar(₺)"))
        self.input_total_kg.setPlaceholderText(_translate("MainWindow", "Toplam Kg"))
        self.input_customer_name.setPlaceholderText(_translate("MainWindow", "Müşteri Adı , Soyadı"))
        self.input_paid_kg.setPlaceholderText(_translate("MainWindow", "Ödenen Kg"))
        self.input_yield.setPlaceholderText(_translate("MainWindow", "Randıman"))
        self.input_date.setPlaceholderText(_translate("MainWindow", "Tarih (GG.AA.YYYY)"))
        self.btn_delete.setText(_translate("MainWindow", "Kaydı Sil"))
        self.btn_update.setText(_translate("MainWindow", "Güncelle"))
        self.btn_save.setText(_translate("MainWindow", "Kaydet (Yeni)"))
        item = self.table_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Müşteri Adı"))
        item = self.table_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Soyadı"))
        item = self.table_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Toplam Kg"))
        item = self.table_data.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Randıman"))
        item = self.table_data.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ödenen Kg"))
        item = self.table_data.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Kalan Kg"))
        item = self.table_data.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ödenen Tutar"))
        item = self.table_data.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Tarih"))
        self.anasayfa_button.setText(_translate("MainWindow", "Ana Sayfa"))
        self.fiyathesaplama_sayfa_button.setText(_translate("MainWindow", "Fiyat Hesaplama"))
        self.randiman_cikis_button.setText(_translate("MainWindow", "Çıkış Yap"))
        self.randiman_hesaplama_baslik_label.setText(_translate("MainWindow", "RANDIMAN HESAPLAMA"))
        self.label_numune.setText(_translate("MainWindow", "Numune : 250 gr "))
        self.ic_findik_input.setPlaceholderText(_translate("MainWindow", "İç Fındık Miktarı (gr):"))
        self.saglam_findik_input.setPlaceholderText(_translate("MainWindow", "Sağlam Fındık Miktarı (gr):"))
        self.randiman_hesapla_button.setText(_translate("MainWindow", "Randıman Hesapla"))
        self.randiman_sonuc_label.setText(_translate("MainWindow", "Sonuç:"))
        self.anasayfa_button_fiyat_hesaplamadan.setText(_translate("MainWindow", "Ana Sayfa"))
        self.randiman_hesaplama_button_fiyattan.setText(_translate("MainWindow", "Randıman Hesaplama"))
        self.cikisyap_button_fiyat.setText(_translate("MainWindow", "Çıkış Yap"))
        self.fiyat_hesaplama_baslik_label.setText(_translate("MainWindow", "FİYAT HESAPLAMA"))
        self.randiman_input.setPlaceholderText(_translate("MainWindow", "Randıman:"))
        self.fiyat_input.setPlaceholderText(_translate("MainWindow", "50 Randıman Baz Fiyatı (₺):"))
        self.kg_input.setPlaceholderText(_translate("MainWindow", "Miktar (Kg):"))
        self.fiyathesapla_button.setText(_translate("MainWindow", "Fiyat Hesapla"))
        self.fiyat_sonuc_label.setText(_translate("MainWindow", "Sonuç:"))
        self.sifre_yenileme_baslik_label.setText(_translate("MainWindow", "ŞİFRE YENİLEME"))
        self.kullanici_adi_input.setPlaceholderText(_translate("MainWindow", "Kullanıcı Adı"))
        self.guvenlik_kelimesi_input.setPlaceholderText(_translate("MainWindow", "Güvenlik Kelimesi"))
        self.yeni_sifre_input.setPlaceholderText(_translate("MainWindow", "Yeni Şifre"))
        self.sifreyi_guncelle_button.setText(_translate("MainWindow", "Şifreyi Güncelle"))
        self.giris_ekrana_don_button.setText(_translate("MainWindow", "Giriş ekranına dön"))
