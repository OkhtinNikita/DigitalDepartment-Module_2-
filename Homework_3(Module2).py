import numpy as np
import sys
import array
import pandas as pd
import random
# Pandas - расширение NumPy (структурированные массивы). Строки и столбцы индексируются метками, а не только числовыми значениями

# Series, DataFrame, Index

## Series

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
# print(type(data))

# print(data.values)
# print(type(data.values))

# print(data.index)
# print(type(data.index))

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data[0])
# print(data[1:3])

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 10, 7, 'd'])
# print(data)

# print(data['1'])
# print(data[10:'d'])

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005

# }
# population = pd.Series(population_dict)
# print(population)

# print(population['city_4'])

# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значения
# - словари


### 1. Привести различные способы создания типа Series

# list_1 = [1, 2, 3, 4] # Списко Python 
# series_list_1 = pd.Series(list_1, index = ['a', 'b', 'c', 'd'])
# print(series_list_1)

# numpy_1 = [2, 3, 4, 5] # Массив NumPy
# series_numpy_1 = pd.Series(numpy_1, index = ['a', 'b', 'c', 'd'])
# print(series_numpy_1)

# scalar_1 = 18
# series_scalar_1 = pd.Series(scalar_1, index = ['a', 'b', 'c', 'd'])
# print(series_scalar_1)

# dict_1 = {'a': 3, 'b': 4, 'c': 5, 'd' : 6}
# series_dict_1 = pd.Series(dict_1)
# print(series_dict_1)


## DataFrame - двумерный массив с явно определенными индексами. Последовательность "согласованных" объектов Series

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005
# }

# area_dict = {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995
# }


# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# print(population)
# print(area_dict)

# states = pd.DataFrame({
#     'population1' : population, 
#     'area1': area
# })

# print(states)

# print(states.values)
# print(states.index)
# print(states.columns)

# print(type(states.values))
# print(type(states.index))
# print(type(states.columns))

# print(states['area1'])

# DataFrame. Способы создания
# - через объекты Series
# - спсики словарей
# - словари объектов Series
# - Двумерный массив NumPy
# - структурированный массив NumPy

### 2. Привести различные способы создания объектов DataFrame

# data_2_1 = {
#     'country' : ['England', 'France', 'Spain'],
#     'city' : ['London', 'Paris', 'Madrid'],
#     'population' : ['1', '2', '3']
# }
# df_2_1 = pd.DataFrame(data_2_1) # С помощью словаря списков
# print(df_2_1)

# data_2_2 = {
#     'country' : np.array(['England', 'France', 'Spain']),
#     'city' : np.array(['London', 'Paris', 'Madrid']),
#     'population' : np.array(['1', '2', '3'])
# }
# df_2_2 = pd.DataFrame(data_2_2) # С помощью словаря массивов
# print(df_2_2)

# data_2_3 = [
#     {'country': 'England', 'city': 'London', 'population': '1'},
#     {'country': 'France', 'city': 'Paris', 'population': '2'},
#     {'country': 'Spain', 'city': 'Madrid', 'population': '3'}
# ]
# df_2_3 = pd.DataFrame(data_2_3) # Список словарей
# print(df_2_3)

# data_2_4 = np.array([
#     ['England', 'London', '1'],
#     ['France', 'Paris', '2'],
#     ['Spain', 'Madrid', '3']
# ])
# df_2_4 = pd.DataFrame(data_2_4, columns=['country', 'city', 'population']) # Массив NumPy
# print(df_2_4)

# data_2_5 = {
#     'country' : pd.Series(['England', 'France', 'Spain']),
#     'city' : pd.Series(['London', 'Paris', 'Madrid']),
#     'population' : pd.Series(['1','2','3'])
# }
# df_2_5 = pd.DataFrame(data_2_5)
# print(df_2_5)


## Index - способ организации ссылки на данные объектов Series и DataFrame. Index - неизменяем, упорядочен, является мультимножеством (могут быть повторяющиеся значения)

# ind = pd.Index([2,3,5,7,11])
# print(ind[1])
# print(ind[::2])

# Index - следует соглашениям объекта set (pyrhon)

# indA = pd.Index([1, 2, 3, 4, 5])
# indB = pd.Index([2, 3, 4, 5, 6])

# print(indA.intersection(indB))

## Выборка данных из Series
# Похожа на словарь
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'b', 'd'])

# print('a' in data)

# print(data.keys())

# print(list(data.items()))

# data['a'] = 100
# data['z'] = 1000
# print(data)

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'b', 'd'])
# print(data['a':'c'])
# print(data[0:2])

# print(data[(data>  0.5)& (data < 1)])


# # Атрибуты индексации, говорят куда надо смотреть

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 2, 3, 4])

# print(data.loc[1])
# print(data.iloc[1])


## Выбираем данные из DataFrame

# population_dict = {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005
# }

# area_dict = {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995
# }

# pop = pd.Series(
#     {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }
# )

# area = pd.Series(
#     {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }
# )


# data = pd.DataFrame({'area1':area, 'pop1':pop, 'pop': pop})


# print(data)

# print(data.pop1 is data['pop1'])
# print(data.pop is data['pop'])


# Двумерный NumPy - массив

# data = pd.DataFrame({'area1':area, 'pop1':pop, 'pop': pop})

# print(data)

# print(data.values)

# print(data.T)

# print(data['area1'])

# print(data.values[0]) #легко работаем со столбцами, но если работаем со строками, то переходим во внутренний массив

# атрибуты-индексаторы

# print(data)
# print(data.iloc[:3, 1:2]) # Здесь обращаемся именно по индексу
# print(data.loc[:'city_3', 'pop1':'pop']) # Здесь включая границы и обращаемся по имени
# print(data.loc[data['pop'] > 1002, ['area1','pop']])

# data.iloc[0,2] = 99999

# print(data)

## Про универсальные функции

# rng = np.random.default_rng()
# s = pd.Series(rng.integers(0,10,3))

# print(s)

# print(np.exp(s)) # exp для каждого числа s

# pop = pd.Series(
#     {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_41': 1004,
#     'city_51': 1005,
# }
# )

# area = pd.Series(
#     {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_42': 9994,
#     'city_52': 9995,
# }
# )

# data = pd.DataFrame({'area1':area, 'pop1':pop})
# data = data.fillna(1)
# print(data)

### 3. Объединить два объекта Series с неодинаковыми множествами ключей(индекс), так чтобы, вместо NaN было установлено значение 1
# pop = pd.Series(
#     {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_41': 1004,
#     'city_51': 1005,
# }
# )
# area = pd.Series(
#     {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_42': 9994,
#     'city_52': 9995,
# }
# )
# data_3 = pd.DataFrame({'area1':area, 'pop1':pop})
# data_3 = data_3.fillna(1)
# print(data_3)

# dfA = pd.DataFrame(rng.integers(0, 10, (2,2)), columns=['a','b'])
# dfB = pd.DataFrame(rng.integers(0, 10, (3,3)), columns=['a','b','c'])

# print(dfA)
# print(dfB)

# rng = np.random.default_rng(1)

# A = rng.integers(0, 10, (3,4))
# print(A)

# print(A[0])
# print(A - A[0])

# df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
# print(df)

# print(df.iloc[0])

# print(df - df.iloc[0])

# print(df.iloc[0, ::2])

# print(df - df.iloc[0, ::2])

### 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило не по строкам, а по столбцам
# rng = np.random.default_rng(1)
# A_4 = rng.integers(0, 10, (3,4))
# df_4 = pd.DataFrame(A_4, columns=['a', 'b', 'c', 'd'])
# print(df_4)
# print(df_4.sub(df_4.iloc[:, 0], axis=0))

# NaN = not a number - отсутствующее значение
# NA - значения: NaN, null, -99999

# Pandas. Два способа хранения отсутсвующих значений
# индикаторы NaN, None
# null

# None - объект, его использование может привести к накладным расходом. Не работает с sum, min и другими агрегирующими операторами

# val1 = np.array([1, 2, 3]) #Если подставить None, то работать не будет
# print(val1.sum())

# val1 = np.array([1, np.nan, 2, 3]) #Если подставить None, то работать не будет
# print(val1.sum())
# print(np.sum(val1))
# print(np.nansum(val1))


# x = pd.Series(range(10), dtype=int)
# print(x)

# x[0] = None
# x[1] = np.nan

# print(x)

# x1 = pd.Series(['a', 'b', 'c'])

# x1[0] = None
# x1[1] = np.nan

# print(x1)

# x2 = pd.Series([1, 2, 3, np.nan, None, pd.NA])
# print(x2)


# x3 = pd.Series([1, 2, 3, np.nan, None, pd.NA], dtype='Int32')
# print(x3)


# Для работы с пустыми значениями есть следующее

# print(x3.isnull())
# print(x3[x3.isnull()])
# print(x3[x3.notnull()])

# print(x3.dropna())

# df = pd.DataFrame(
#     [
#         [1,2,3,np.nan,None, pd.NA],
#         [1,2,3,4,5,6],
#         [1,np.nan,3,4,np.nan,6]
#     ]
# )

# print(df)
# print(df.dropna())
# print('dddddd')
# print(df.dropna(axis=0))
# print(df.dropna(axis=1))


# how
# - all - все значения NA
# - any - хотя бы одно значение
# - thresh = x, остается, если присутсвует МИНИМУМ х НЕПУСТЫХ значений
# print(df.dropna(axis=1, how='all'))
# print(df.dropna(axis=1, how='any'))
# print(df.dropna(axis=1, thresh=2))


### 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

# data_5 = {
#     'A': [1, np.nan, 3, np.nan, 5],
#     'B': [np.nan, 2, np.nan, 4, np.nan]
# }

# df_5 = pd.DataFrame(data_5)
# print("Исходный DataFrame:")
# print(df_5)

# df_ffill = df_5.ffill()
# print("\nПосле ffill():")
# print(df_ffill)

# df_bfill = df_5.bfill()
# print("\nПосле bfill():")
# print(df_bfill)