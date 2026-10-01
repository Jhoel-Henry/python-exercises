"""SORU:
Kullanıcıdan şehir adlarının ve bu şehirlere ait hava sıcaklıklarının tutulduğu iki liste alan ve
hava sıcaklıklarının küçükten büyüğe doğru sıralanarak şehir adlarıyla beraber bir demet (tuple)
içerisine eklendiği bir fonksiyon yazınız. İki listenin uzunluğunun eşit olduğu varsayılacaktır.
En soğuk 3 şehre ait bilginin döndürülmesi yeterlidir. Program çıktısı aşağıdaki gibi olmalıdır.
Örnek:
Input:
Ankara İzmir İstanbul Bursa Antalya Adana Gaziantep Antakya Muğla Denizli
0 9 -1 7 -3 5 7 12 0 22
Output:
('Antalya', -3, 'İstanbul', -1, 'Ankara', 0)"""

sehirler = input("Sehirler yaz").split()
sicakliklar = input("Bu sehirleri hangi derece gosteriyor, yaz:").split()


def unir(sehirler, sicakliklar):
    list = ()
    for i in range(len(sehirler)):
        list = list + ((sehirler[i], sicakliklar[i]),)

    res = sonunda(list)
    return res


# Basicamente aca se aplico el algoritmo bubble sort aplicado, teniendo en cuenta que son li


def sonunda(lista):
    res = list(lista)
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            aux = res[j]
            if res[j][1] > res[j + 1][1]:
                res[j] = res[j + 1]
                res[j + 1] = aux
    result = ()
    for i in range(0, 3):
        result = result + res[i]

    return result


print(unir(sehirler, sicakliklar))
