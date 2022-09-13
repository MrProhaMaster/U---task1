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