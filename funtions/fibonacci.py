# Haciendo la funcion fibonacci
deger = int(input("Hangi fibonacci'nin degeri istiyor: "))


def fibonacci(deger):
    x = 1
    y = 1
    c = 2

    while c != deger and deger >= 2:
        ext = x
        x = y
        y = y + ext
        c += 1

    print("Senin numaran : ", y)

    if deger == 1 or deger == 2:
        print("Senin numaran : ", x)


print("cevap ", fibonacci(deger))
