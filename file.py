# file = open("sample.txt","r")
# #write = tamamen sıfırdan yazma
# #append = üzerine ekleme
# #read = okuma

# print(file.read())
# file.close()


#! pair konusu
#! bir şirket çalışanları verilerini tutan dosya oluşturulacak
#! Kullanıcıdan çalışan sayısı alınacak
#! Çalışan sayısı kadar isim,soyisim,maaş bilgisi alınacak
#! Dosyadaki her satıra "Ad Soyad - Maaş" kalıbında çalışan bilgileri eklenecek.
#! Programın sonunda bu dosyada bilgileri satır satır okuyup listeleyecek kod yazılacak.
#! Eklenen çalışanlar mevcut çalışanları silmeyecek, üzerine yazılacak.
#! Hata yakalama işlemlerini unutmayalım. (Try / except kullan)
#! şirket çalışanları input ile kullanıcıdan alacağız.


try:
    workerCount = int(input("Çalışan sayısı giriniz"))
except:
    print("Düzgün sayı girilmedi..")
    exit()
file = open("employees.txt", "a+")
for i in range(workerCount):
    name = input(f"{i+1}. çalışanın adını giriniz: ")
    lastName = input(f"{i+1}. çalışanın soyadını giriniz:")
    salary = input(f"{i+1}. çalışanın maaşını giriniz:")
    file.write(f"{name} {lastName} - {salary}\n")
file.seek(0)            #önemli
print(file.read())
file.read(0)
file.close()