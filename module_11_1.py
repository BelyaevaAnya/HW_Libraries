import numpy as np
import pandas as pd

# Создание серии(серия-одномерный массив, который может хранить значения любого типа данных)
series = pd.Series([1, 2, 3], index=["a", "b", "c"], dtype=np.uint8)
print(series)
# Создание DataFrame — это двумерная структура данных, представляющая собой таблицу с метками для строк и столбцов.
dataframe = pd.DataFrame([[1, "Ivan", 5.0], [2, "Sergey", 4.3], [3, "Dmitry", 4.5]], columns=["#", "Name", "Score"])
print(dataframe)
# Чтение csv-файла
anime = pd.read_csv("./DatasetAnimeStatistic/anime.csv")
print(anime)
# Объединение данных
df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": [1, 2, 3, 4]})
df2 = pd.DataFrame({"key": ["B", "D", "E", "F"], "value": [5, 6, 7, 8]})
df3 = pd.merge(df1, df2, on="key", how="inner")
print(df3)
# отображение 5 строк данных
print(anime.head)
# Вывод статистических сведений о датафрейме]
print(anime.describe())
# Создание списка или объекта Series на основе значений столбца
anime_lst = anime['genre'].tolist()
print(anime_lst)
anime_modified = anime.set_index('name')
# Получение списка значений из индекса
anime_modified = anime_modified.index.tolist()
print(anime_modified)
# Получение списка значений столбцов
anime_colounms = anime.columns.tolist()
print(anime_colounms)
# Присоединение к датафрейму нового столбца с заданным значением
anime['train set'] = True
print(anime)
# Создание нового датафрейма из подмножества столбцов
df = anime[['name', 'episodes']]
print(df)
# Удаление заданных столбцов
anime = anime.drop(['anime_id', 'genre', 'members'], axis=1).head()
# Получение строк по числовым индексам
anime_modified_1 = anime.iloc[0:3]
print(anime_modified_1)
# Получение строк по заданным значениям столбцов
print(anime[anime['type'].isin(['TV', 'Movie'])])
# для 1 значения
print(anime[anime['type'] == 'TV'])
# Фильтрация по значению
print(anime[anime['rating'] > 8])
#  Сортировка
print(anime.sort_values('rating', ascending=False))
# Агрегирование. Функция df.groupby и подсчёт количества записей
print(anime.groupby('type').count())
# Функция df.groupby и агрегирование столбцов различными способами
print(anime.groupby(["type"]).agg({
  "rating": "sum",
  "episodes": "count",
  "name": "last"
}).reset_index())
# Отбор случайных образцов из набора данных
print(anime.sample(frac=0.25))