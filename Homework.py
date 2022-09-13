from pprint import pprint

def task1():
    A, B, C = (list() for i in range(3))
    A = input('Введите через пробел числа массива А: ').split(' ')
    for i in A:
        if int(i) % 2 == 0:
            B.append(int(i))
        else:
            C.append(int(i))
    print(f'B: {B}')
    print(f'C: {C}')

def task2():
    A = []
    n, m = input('Введите размеры матрицы А(m, n) через пробел: ').split(' ')
    n, m = int(n), int(m)
    for i in range(m):
        s = input(f'Введите элементы {i+1} строки через пробел: ').split(' ')
        s = [int(i) for i in s]
        A.append(s)
    mx = 0
    mn = 10000000000000
    for i in A:
        if sum(i) > mx:
            mx = sum(i)
        if sum(i)<mn:
            mn = sum(i)
    print(mx, mn)


#task1()
task2()