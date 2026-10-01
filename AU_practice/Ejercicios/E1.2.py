"""
Kullanıcıdan öğrenci adlarının tutulduğu bir liste ile bu öğrencilere ait ara sınav ve final
notlarının tutulduğu iki ayrı liste daha alan ve genel not ortalamalarını hesaplayarak öğrenci
adlarıyla beraber bir demet (tuple) içerisine ekleyen bir fonksiyon yazınız. Üç listenin
uzunluğunun eşit olduğu varsayılacaktır. Genel not ortalaması 50 ve üzeri olan öğrenci bilgileri
sadece tuple içerisine eklenecektir. Genel not ortalaması ikinci listede tutulan ara sınavların
0.3’ü ile üçüncü listede tutulan final notlarının 0.8’inin toplamından hesaplanacaktır.
Genel Not Ortalaması = (liste2’den bir değer)*0.3 + (liste3’ten bir değer)*0.8
Program çıktısı aşağıdaki gibi olmalıdır.
Örnek:
Input:
James Mary Robert Patricia John Jennifer Michael Linda William Elizabeth
63 34 19 76 19 54 71 92 0 84
34 2 57 39 98 12 56 28 23 24
Output:
('Robert', 51.3, 'Patricia', 54.0, 'John', 84.1, 'Michael', 66.1, 'Linda', 50.0)
Not: Program çıktısındaki sayısal değerler virgülden sonra 2 basamak olacak şekilde
ayarlanmalıdır.

"""


def gecmisler():
    ogrenciler = input("Lutfen, ogrencileriniz yazabilirsin: ").split()
    ara_sinav = input("Ogrencilerin ara sinavi yaz: ").split()
    final_sinav = input("Ogrencilerin final sinavi yaz: ").split()

    res = calculo(ogrenciler, ara_sinav, final_sinav)

    return res


def calculo(ogrenciler, ara_sinav, final_sinav):
    aux = ()
    res = ()
    for i in range(len(ogrenciler)):
        prom_actual = float(ara_sinav[i]) * 0.3 + float(final_sinav[i]) * 0.8
        aux = (ogrenciler[i], prom_actual)
        if prom_actual >= 50:
            res = res + aux

    return res


print(gecmisler())
