import sqlite3
import os

def Ana_Menu():
    print("1.) Öğrencileri Görüntüle")
    print("2.) Yeni Öğrenci Ekle")
    print("3.) Kayıtlı Öğrenci Sil")
    print("4.) ID'ye Göre Öğrenci Ara")
    print("5.) Programdan Çık")
    islem = input("Lütfen Yapacağınız İşlemi Yazınız (1,2,3,4,5) : ")
    print()
    return islem

while(True):
    if os.path.exists("IYTE.db"):
        with sqlite3.connect("IYTE.db") as IYTE:
            cursor = IYTE.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Students (Student_ID nvarchar(8) not null primary key , Name nvarchar(25), Surname nvarchar(50), Male_Female nvarchar(6), Age tinyint, Department nvarchar(25)) ")
            islem=Ana_Menu()
            if islem=="1":
                cursor.execute("SELECT *from Students")
                kayitlar=cursor.fetchall()
                print("*"*75)
                if len(kayitlar)==0:
                    print("Henüz Bir Kayıt Bulunmamakta")
                else:
                    counter=1
                    for kayit in kayitlar:
                        veriler=""
                        for veri in kayit:
                            if veriler=="":
                                veriler=veri
                            else:
                                veriler=veriler+", "+str(veri)
                        print(f"Kayıt {counter} => {veriler}")
                        counter+=1
                print("*"*75)
                print()
                os.startfile("IYTE.db")

            elif islem=="2":
                print("*"*50)
                print("YENİ ÖĞRENCİ KAYDI")
                student_id=input("Student ID : ")
                name=input("Name : ")
                surname=input("Surname : ")
                male_female=input("Male-Female : ")
                age=int(input("Age : "))
                department=input("Department : ")
                print("*"*50)
                print()
                datas=[student_id,name,surname,male_female,age,department]
                cursor.execute(f"INSERT INTO Students VALUES(?,?,?,?,?,?)",datas)
                os.startfile("IYTE.db")

            elif islem=="3":
                deleted_id=input("Silinecek Öğrencinin Numarası : ")
                print()
                cursor.execute("delete from Students WHERE Student_ID=?",deleted_id)
                os.startfile("IYTE.db")

            elif islem=="4":
                aranacak_id=input("Kayıt Kontrolü Yapılacak Öğrenci Numarası : ")
                cursor.execute(f"SELECT *FROM Students WHERE Student_ID={aranacak_id}")
                id=cursor.fetchall()
                if len(id)==0:
                    print("Aradığınız Numaraya Sahip Bir Öğrenci Bulunmamakta\n")
                else:
                    kayit=""
                    for item in id:
                        for veri in item:
                            if kayit=="":
                                kayit=veri
                            else:
                                kayit=kayit+", "+str(veri)
                    print(f"Kayıt Bulundu => {kayit}\n")

            else:
                break
    else:
        sqlite3.connect("IYTE.db")
        continue