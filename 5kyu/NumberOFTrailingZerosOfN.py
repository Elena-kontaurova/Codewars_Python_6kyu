'''Напишите программу, которая вычислит количество завершающих нулей в факториале заданного числа.
N! = 1 * 2 * 3 *  ... * N
Будьте осторожны, 1000! состоит из 2568 цифр...'''
def zeros(n):
    k = 0
    while n:
        n //= 5
        k += n
    return k
