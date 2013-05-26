# encoding: utf-8

"""
Решение 6-й задачи.

http://projecteuler.net/problem=6

Использовать sum нельзя, для больших чисел будет слишком долго работать.
Математика приходит на помощь. Есть формулы для суммы последовательности
натуральных чисел и их квадратов.
"""

from math import ceil

def sum_range(start, stop, step=1):
    """
    ru.wikipedia.org/wiki/Арифметическая_прогрессия
    """
    
    # Количество элементов в прогрессии
    n = ceil((stop - start + 1) / step)
    
    if step != 1:
        return n * (2*start + (n - 1)*step) / 2
    else:
        return n * (start + stop) / 2
    
def sum_square_range(start, stop):
    """
    ru.wikipedia.org/wiki/Квадрат_(алгебра)
    http://mmmf.msu.ru/lect/spivak/summa_sq.pdf
    """
    
    if start != 1:
        raise NotImplementedError

    return (2*stop + 1)*(stop + 1)*stop / 6
    
if __name__ == '__main__':
    start = 1
    stop = 100
    print(sum_range(start, stop) ** 2 - sum_square_range(start, stop))
