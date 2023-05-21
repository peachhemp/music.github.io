"""Даны натуральное число n и целые числа a1, a2, …, an,n = int(input('Введите количество элементов a для ввода: '))
for i in range(1,n+1):
    print("Введите элемент A",i,": ")
    a = int(input())
    if a == 10:
        countA = i
        break #break для буквы б)
print(countA)
