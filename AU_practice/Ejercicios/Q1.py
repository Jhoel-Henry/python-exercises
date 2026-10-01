"""Kullanıcıdan girilen değere kadar olan sayıların faktöriyellerini hesaplayıp ekrana yazdıran
Python programı yazınız.
Örneğin, size verilen ilk input 5 değeridir. Çıktınız, 1’den 5’e kadar olan sayıların
faktoriyelleri yani 5! = 5.4.3.2.1! = 120 olacaktır."""

deger = int(input("Bir deger yazabilirsin: "))


def faktoriyel(deger):

    sonuc = 1

    for i in range(deger, 1, -1):
        sonuc = sonuc * i

    return sonuc


print("El resultado es: ", faktoriyel(deger))
