"""1.	Kullanıcıdan alınan 10 sayı için aşağıdaki işlemleri gerçekleştiren python kodunu yazınız:

a.	En büyük sayıyı bulup ekrana bastırın
b.	En küçük sayıyı bulup ekrana bastırın
c.	Negatif, 0 ve pozitif adedini bulup; sırasıyla ekrana bastırın
"""

print("Welcome , please enter 10 numbers:")

for i in range(10):
    number = int(input("Enter a number: "))
    mayor = 0
    if mayor < number:
        mayor = number

    menor = 0
    if menor > number:
        menor = number

    c_positive = 0
    c_negative = 0
    c_zero = 0

    if number > 0:
        c_positive += 1
    elif number < 0:
        c_negative += 1
    else:
        c_zero += 1

print("The largest number is: ", mayor)
print("The smallest number is: ", menor)
print("The number of positive numbers is: ", c_positive)
print("The number of negative numbers is: ", c_negative)
print("The number of zeros is: ", c_zero)
