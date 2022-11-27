lessonCount = int(input("Kaç adet ders notu gireceksiniz?"))

passedExams = 0
failedExams = 0


for i in range(lessonCount):
    lessonExam1 = float(input(f"{i+1}. ders için vize notu giriniz."))
    lessonExam2 = float(input(f"{i+1}. ders için final notu giriniz."))
    totalExamNote = (lessonExam1 * 0.4) + (lessonExam2 * 0.6)

    
    if totalExamNote >= 50:
        passedExams += 1
        print(f"{i+1}. dersten geçtiniz.")
    else:
        failedExams += 1
print(f"{passedExams} adet dersten geçtiniz. {failedExams} adet dersten kaldınız.")
