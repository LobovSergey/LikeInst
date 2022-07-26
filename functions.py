import json
from json import JSONDecodeError

extensions = ['jpg', 'png', 'jpeg', 'gif']


def load_json():
    """Загрузка постов"""
    try:
        with open('static/posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Файл не удается преобразовать'


def add_post(post) -> dict:
    """Добавляет новый пост ко всем постам"""
    posts = load_json()
    posts.append(post)
    with open('static/posts.json', 'w', encoding='UTF-8') as file:
        json.dump(posts, file)
    return post


def save_picture(picture):
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def check_file(picture):
    if picture:
        filename = picture.filename
        extension_file = filename.split('.')[-1]
        if extension_file in extensions:
            return {True, None}
        return {False, "Неверное расширение файла"}
    return {False, "Файл не был загружен"}
