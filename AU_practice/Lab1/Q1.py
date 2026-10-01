"""Question:Write a Pythonprogramthat askstheuser to enter three examgrades.
The programshould:
1. Calculatetheaverage score.
2. Determinetheletter gradebasedontheaverage(usingthegradingtable
below).
3. Display whetherthestudent passedorfailed.
4. Ifanygradeisoutsidetherange 0–100,displayanerror message:
"Invalid grade entered!"
AverageRange LetterGrade
90–100 AA
80–89  BA
70–79 BB
60–69 CB
50–59 CC
40–49 DC
30–39 DD
0–29 FF
"""

not_bir = int(input("Birinci notu giriniz:"))
not_iki = int(input("Ikinci notu giriniz:"))
not_uc = int(input("Ucuncu notu giriniz:"))

ortalama = (not_bir + not_iki + not_uc) / 3

if (
    not_bir < 0
    or not_bir > 100
    or not_iki < 0
    or not_iki > 100
    or not_uc < 0
    or not_uc > 100
):
    print("Yanlis not girildi!")
else:
    print("Ortalama: ", ortalama)
    if ortalama >= 90:
        print("Harf notu: AA")
    elif ortalama >= 80:
        print("Harf notu: BA")
    elif ortalama >= 70:
        print("Harf notu: BB")
    elif ortalama >= 60:
        print("Harf notu: CB")
    elif ortalama >= 50:
        print("Harf notu: CC")
    elif ortalama >= 40:
        print("Harf notu: DC")
    elif ortalama >= 30:
        print("Harf notu: DD")
    else:
        print("Harf notu: FF")

    if ortalama >= 50:
        print("Gectiniz")
    else:
        print("Kaldiniz")
