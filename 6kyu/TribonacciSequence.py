'''Хорошо познакомился со старшим братом Фибоначчи, ОН ЖЕ Tribonacci.
Как уже видно из названия, он работает в основном как Фибоначчи, но суммируя последние 3 (вместо 2) чисел последовательности,
генерируется следующее. Итак, если мы хотим начать нашу последовательность Tribonacci с [1, 1, 1] 
в качестве начального ввода (ОН ЖЕ сигнатура), 
у нас есть эта последовательность:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
Но что, если мы начнем с [0, 0, 1] в качестве подписи? Начиная с [0, 1] вместо [1, 1] основного сдвига обычной последовательности
Фибоначчи на одно место, у вас может возникнуть соблазн подумать, что мы получим ту же последовательность, 
сдвинутую на 2 места, но это не так, и мы получим:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Что ж, возможно, вы уже догадались об этом, но для ясности: вам нужно создать функцию фибоначчи, которая, 
учитывая массив / список с подписью, возвращает первые n элементов - включая подпись- из заданной таким образом последовательности.
Подпись всегда будет содержать 3 числа; n всегда будет неотрицательным числом; если n == 0, 
то верните пустой массив (за исключением того, что в C возвращает NULL) и будьте готовы ко всему остальному, что четко не указано ;)'''
def tribonacci(signature, n):
    for i in range(3, n):
        signature.append(signature[i-1] + signature[i-2] + signature[i-3])
    return signature[:n]
