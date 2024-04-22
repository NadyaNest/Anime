import pandas as pd
import random

data = pd.read_csv("anime_with_ratings.csv")

# Удаляем записи без жанров перед формированием списка жанров
cleaned_data = data.dropna(subset=['genre'])

# Подготовка списка уникальных жанров
genres = set()
cleaned_data['genre'].str.split(', ').apply(genres.update)
genres = sorted(genres)

def get_random_anime(genre=None):
    """Возвращает случайную запись из DataFrame, фильтруя по жанру, если он указан."""
    if genre == "all" or genre is None:
        sample = cleaned_data
    else:
        sample = cleaned_data[cleaned_data['genre'].str.contains(genre, na=False)]
    if sample.empty:
        return None  # Возвращает None, если нет данных по запрошенному жанру
    random_entry = sample.sample().iloc[0]
    return {
        'name': random_entry['name'],
        'genre': random_entry['genre'],
        'type': random_entry['type'],
        'episodes': parse_int(random_entry['episodes']),
        'rating': parse_float(random_entry['rating']),
        'members': parse_int(random_entry['members']),
        'average_rating': parse_float(random_entry['average_rating']),
        'rating_count': parse_int(random_entry['rating_count'])
    }

def parse_int(value):
    """Пытается преобразовать значение в int, возвращает None при неудаче."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def parse_float(value):
    """Пытается преобразовать значение в float, возвращает None при неудаче."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
