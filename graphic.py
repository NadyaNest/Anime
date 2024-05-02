import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла в DataFrame
data = pd.read_csv("anime_with_ratings.csv")

# Подсчет количества аниме для каждого жанра
genre_counts = data['genre'].value_counts()

# Определение порога для группировки редких жанров
threshold = 100

# Сгруппировать редкие жанры в категорию "Другие"
other_genres = genre_counts[genre_counts < threshold]
genre_counts = genre_counts.drop(other_genres.index)
genre_counts['Другие'] = other_genres.sum()

# Построение круговой диаграммы
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Распределение аниме по жанрам")
plt.axis('equal')  # Сделать круг кругом
plt.legend(title="Жанры", loc="best")  # Добавление легенды
plt.show()

# Преобразовать значения количества эпизодов в числовой формат
data['episodes'] = pd.to_numeric(data['episodes'], errors='coerce')

# Удалить строки с пропущенными значениями в колонке эпизодов
data = data.dropna(subset=['episodes'])

# Отсортировать данные по количеству эпизодов
data_sorted = data.sort_values(by='episodes')

# Построение графика зависимости рейтинга от количества эпизодов
plt.figure(figsize=(10, 6))
plt.scatter(data_sorted['episodes'], data_sorted['rating'], alpha=0.5)
plt.title("Зависимость рейтинга от количества эпизодов")
plt.xlabel("Количество эпизодов")
plt.ylabel("Рейтинг")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Увеличение количества корзин (bins) и добавление прозрачности
plt.figure(figsize=(10, 6))
plt.hist(data['rating'], bins=40, alpha=0.7, color='blue', edgecolor='black', linewidth=1.2)
plt.title("Распределение рейтингов аниме")
plt.xlabel("Рейтинг")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['average_rating'], bins=40, alpha=0.7, color='green', edgecolor='black', linewidth=1.2)
plt.title("Распределение средних рейтингов аниме")
plt.xlabel("Средний рейтинг")
plt.ylabel("Частота")
plt.grid(True)
plt.show()


