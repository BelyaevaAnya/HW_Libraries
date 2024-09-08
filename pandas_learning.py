# 1. импорт pandas
import numpy as np
import pandas as pd

# 2. Импорт данных
anime = pd.read_csv('./DatasetAnimeStatistic/anime.csv')
rating = pd.read_csv('./DatasetAnimeStatistic/rating.csv')

# index
anime_modified = anime.set_index('name')
print(anime_modified)
print()

# Cоздание датафрейма из данных, введённых вручную
df = pd.DataFrame([[1, 'Bob', 'Builder'],
                   [2, 'Sally', 'Baker'],
                   [3, 'Scott', 'Candle Stick Maker']],
                  columns=['id', 'name', 'occupation'])
print(df)
print()

# Копирование датафрейма
anime_copy = anime.copy(deep=True)
print(anime_copy)
print()

# 3. Экспорт данных
rating[:10].to_csv('./DatasetAnimeStatistic/saved_ratings.csv', index=False)

# 4. Просмотр и исследование данных
# Получение n записей из начала или конца датафрейма
print(anime.head(3))
print(rating.tail(1))
print()

# Подсчёт количества строк в датафрейме
print(len(df))
print()

# Подсчёт количества уникальных значений в столбце
print(len(rating['user_id'].unique()))
print()

# Получение сведений о датафрейме
print(anime.info())
print()

# Вывод статистических сведений о датафрейме
print(anime.describe())
print()

# Подсчёт количества значений
print(anime.type.value_counts())
print()

# 5. Извлечение информации из датафреймов
# Создание списка или объекта Series на основе значений столбца
print(anime['genre'].tolist())
print()
print(anime['genre'])
print()

# Получение списка значений из индекса
print(anime_modified.index.tolist())
print()

# Получение списка значений столбцов
print(anime.columns.tolist())
print()

# 6. Добавление данных в датафрейм и удаление их из него
# Присоединение к датафрейму нового столбца с заданным значением
# anime['train set'] = True

# Создание нового датафрейма из подмножества столбцов
# print(anime[['name','episodes']])

# Удаление заданных столбцов
# anime = anime.drop(['anime_id', 'genre', 'members'], axis=1).head()
# print(anime)

# Добавление в датафрейм строки с суммой значений из других строк
# Для демонстрации этого примера самостоятельно создадим небольшой датафрейм,
# с которым удобно работать. Самое интересное здесь — это конструкция df.sum(axis=0),
# которая позволяет получать суммы значений из различных строк.
# df = pd.DataFrame([[1,'Bob', 8000],
#                   [2,'Sally', 9000],
#                   [3,'Scott', 20]], columns=['id','name', 'power level'])
# df.append(df.sum(axis=0), ignore_index=True)
# Команда вида df.sum(axis=1) позволяет суммировать значения в столбцах.
# Похожий механизм применим и для расчёта средних значений. Например — df.mean(axis=0).

# 7. Комбинирование датафреймов
# Конкатенация двух датафреймов
# Эта методика применима в ситуациях, когда имеются два датафрейма с одинаковыми столбцами, которые нужно скомбинировать.
df1 = anime[0:2]
df2 = anime[2:4]
print(df1)
print(df2)
print(pd.concat([df1, df2], ignore_index=True))

# Слияние датафреймов
print(rating.merge(anime, left_on='anime_id', right_on='anime_id', suffixes=('_left', '_right')))

# 8. Фильтрация
# Получение строк с нужными индексными значениями
print(anime_modified.loc[['Haikyuu!! Second Season', 'Gintama']])
# Получение строк по числовым индексам
print(anime_modified.iloc[0:3])
# Получение строк по заданным значениям столбцов
print(anime[anime['type'].isin(['TV', 'Movie'])])
# Получение среза датафрейма
print(anime[1:3])
# Фильтрация по значению
print(anime[anime['rating'] > 8])

# 9. Сортировка
# Для сортировки датафреймов по значениям столбцов можно воспользоваться функцией df.sort_values:
anime1 = anime.sort_values('rating', ascending=False)
print(anime1)

# 10. Агрегирование
# Функция df.groupby и подсчёт количества записей
# Вот как подсчитать количество записей с различными значениями в столбцах:
print(anime.groupby('type').count())

# Функция df.groupby и агрегирование столбцов различными способами
# Обратите внимание на то, что здесь используется reset_index().
# В противном случае столбец type становится индексным столбцом.
# В большинстве случаев я рекомендую делать то же самое.
print(anime.groupby(["type"]).agg({
    "rating": "sum",
    "episodes": "count",
    "name": "last"
}).reset_index())

# Создание сводной таблицы
# Для того чтобы извлечь из датафрейма некие данные,
# нет ничего лучше, чем сводная таблица.
# Обратите внимание на то, что здесь я серьёзно отфильтровал датафрейм,
# что ускорило создание сводной таблицы.
tmp_df = rating.copy()
tmp_df.sort_values('user_id', ascending=True, inplace=True)
tmp_df = tmp_df[tmp_df.user_id < 10]
tmp_df = tmp_df[tmp_df.anime_id < 30]
tmp_df = tmp_df[tmp_df.rating != -1]
print(pd.pivot_table(tmp_df, values='rating', index=['user_id'], columns=['anime_id'], aggfunc=np.sum, fill_value=0))

# 11. Очистка данных
# Запись в ячейки, содержащие значение NaN, какого-то другого значения
# Здесь мы поговорим о записи значения 0 в ячейки, содержащие значение NaN.
# В этом примере мы создаём такую же сводную таблицу, как и ранее, но без использования fill_value=0.
# А затем используем функцию fillna(0) для замены значений NaN на 0.
pivot = pd.pivot_table(tmp_df, values='rating', index=['user_id'], columns=['anime_id'], aggfunc=np.sum)
pivot.fillna(0)

# 12. Другие полезные возможности
# Отбор случайных образцов из набора данных
# Я использую функцию df.sample каждый раз, когда мне нужно получить
# небольшой случайный набор строк из большого датафрейма. Если используется параметр frac=1,
# то функция позволяет получить аналог исходного датафрейма, строки которого будут перемешаны.
print(anime.sample(frac=0.25))

# Перебор строк датафрейма
# Следующая конструкция позволяет перебирать строки датафрейма:
for idx, row in anime[:2].iterrows():
    print(idx, row)
