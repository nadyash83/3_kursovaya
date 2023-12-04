import json


def load_operation(path:str) ->list[]:
    """
    функция для чтения файла json operation
    :param path: путь
    :return: список
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)