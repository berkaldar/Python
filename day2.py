#! kullanıcıdan girdi almak
#! karar blokları
#! döngüler
print("2. gün başlangıç")

userInput = input()
print(f"Girilen değer: {userInput}")

#! type conversion
numberStr = "10";
print(type(numberStr))
number = int(numberStr);
print(number + 10);
print(type(number))

userInput = input();
lessonNote = float(userInput)
print(f"Ders notunuz: {lessonNote}")

# karar yapıları / şart blokları
#indent
#n adet conditiona bağlı karar bloğu oluşturabilirsiniz




#! karar blokları ile işlem yapma
if lessonNote>50:
    print("Geçtiniz")
elif lessonNote == 50: #istediğin kadar ekleyebilirsin else if demek
    print("Sınırda geçtiniz") 
elif lessonNote == 49:
    print("Sınırda kaldınız")
else:
    print("Kaldınız")

#! kullanıcıdan vize ve final notları alacak.
#! vize %40 final %60 etkili olacak
#! uygulama ortalamayı hesaplayacak ve ortalamaya göre
#! 0-49 FF
#! 50-60 DD
#! 60-70 CC
#! 70-80 BB
#! 80-100 AA
#! not ortalamasını ve not harfini kullanıcıya gösterecek programı kodlayınız.






students = [Zafer, Berk, Özlem, Nilüfer]
for i in students: 

    print(i)


#! infinite loop
# while True:
#   print("I am infinite!")

    i = 0
    while i < 10:
        print(i)
        i+=1
