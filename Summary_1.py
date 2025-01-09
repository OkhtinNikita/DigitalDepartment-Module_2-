import numpy as np
import sys
import array
# Типы данных Python

# x = 1
# print(type(x))
# print(sys.getsizeof(x)) # Сколько места занимает x

# x = 'hello'
# print(type(x))

# x = True
# print(type(x))

# l1 = list([])
# print(sys.getsizeof(l1))

# l2 = list([1, 2, 3])
#print(sys.getsizeof(l2)) # Проблема списков в том, что они израсходуют очень много памяти, особенно с увеличением количества элементов.
# Поэтому используют такую структуру, как массив

# a1 = array.array('i', [1,2,3]) # 'i' указывает тип данных, которые будут в массиве (i - целые числа)
# print(sys.getsizeof(a1))
# print(type(a1))
# array делает фокусировку на способе хранени элементов, а в numpy array позволяет не просто эффективно хранить данные, но и производить с ними различные операции

# a = np.array([1,2,3,4,5])
# print(type(a), a)

# "повышающее" приведение типов
# a = np.array([1.23, 2, 3, 4, 5])
# print(type(a), a)

# a = np.array([1.23, 2, 3, 4, 5], dtype=int)
# print(type(a), a)

# a = np.array([range(i, i+3) for i in [2, 4, 6]])
# print(a, type(a))

# a = np.zeros(10, dtype=int)
# print(a, type(a))

# print(np.ones((3,5), dtype=float))

# print(np.full((4,5), 3.1415))

# print(np.arange(0, 20, 2))

# print(np.eye(4))

### МАССИВЫ

#np.random.seed(1) # начальное состояние определяет все последующие случайные числа

#x1 = np.random.randint(10, size=3)
#print(x1)

#x2 = np.random.randint(10, size=(3,2))
#print(x2)

#x3 = np.random.randint(10, size=(3,2,1))
#print(x3)

# print(x1.ndim, x1.shape, x1.size) # ndim - Число размерностей, shape - размер каждой размерности, size - общий размер массива
# print(x2.ndim, x2.shape, x2.size)
# print(x3.ndim, x3.shape, x3.size)

# Доступ к элементам массива осуществляется по индексам (начинаются с нуля)

# a = np.array([1,2,3,4,5])
# print(a[0])
# print(a[-2])

# a[1] = 20
# print(a)

# a = np.array([[1, 2], [3, 4]])
# print(a)
# print(a[0,0])
# print(a[0,-1])

# a[1,0] = 100
# print(a)

# a = np.array([1, 2, 3, 4, 5])
# b = np.array([1.2, 2, 3, 4])

# print(a)
# print(b)

# a[0] = 10
# print(a)

# a[1] = 21.186 # После создания массива измения типа не происходит
# print(a)

## Срезы [старт: конечный элемент: шаг], по умолчанию: начинается с 0, конец - размер нашего измерения (shape), шаг 1

# a = np.array([1, 2, 3, 4, 5, 6])

# print(a[:3])
# print(a[3:])
# print(a[1:-1])
# print(a[1::2])

# print(a[::1])
# print(a[::-1])

# a = np.arange(1,13)

# print(a)

# print(a.reshape(2, 6)) # Изменение размерности
# print(a.reshape(3, 4))

# x = np.array([1, 2, 3])
# y = np.array([4, 5])
# z = np.array ([6])

#print(np.concatenate([x,y,z])) # Массивы можно объединять, склеивать

# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])

# r1 = np.vstack([x,y]) # Скеиваем вертикально
# print(r1)

# print(np.hstack([r1,r1])) # Склеиваем горизонтально

### Вычисления с массивами 

# Векторизированная операция - независимо к каждому элементу массива

# x = np.arange(10)
# print(x)

# print(x * 2 + 1)

# Универсальные функции

# print(np.add(np.multiply(x,2),1))

# Примеры универсальных функций: вышеупомянутые *, +,  -(как вычитание), - (как отрицание), /, //(деление с округление в меньшую сторону), ** (возведение в степень), % (остаток)

## np.abs, sim/cos/tan и обратные к ним, exp, log, гипорболические синусы и косинусы

# x = np. arange(5)

# y = np.zeros(10)
# print(np.multiply(x, 10, out=y[::2]))

# print(y)

# Свертка массива к единственному элементу

# x = np. arange(1, 5)

# print(x)
# print(np.add.reduce(x))
# print(np.add.accumulate(x))

# Векторные произведения

# x = np. arange(1, 10)
# print(np.add.outer(x,x))
# print(np.multiply.outer(x,x))