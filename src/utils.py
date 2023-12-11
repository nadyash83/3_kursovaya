import json

from src.models import Operations


def load_operation(path:str) -> list[dict]:
    """
    функция для чтения файла json operation
    :param path: путь
    :return: список
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_instances(operations:list[dict]) -> list[Operations]:
    """
    Функция расскладывает экземпляры класса
    :param operations: список операций
    :return: список экземпляров
    """
    operation_instansices = []
    for operation in operations:
        if operation:
            operation_instansice = Operations(
                pk=operation["id"],
                state = operation["state"],
                date = operation["date"],
                operation_amount=operation["operationAmount"],
                description = operation["description"],
                from_ = operation.get("from", ""),
                to = operation["to"]
            )
            operation_instansices.append(operation_instansice)
    return operation_instansices

def get_executed_operations(operations:list[Operations]) -> list[Operations]:
    """
    Функция отфильтровывает операции из списка с признаком EXECUTED (только выполненные операции)
    :param operations: список операций
    :return: отфильтрованный список
    """
    executed_operation =[]
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation

def sort_operation_by_date(operations:list[Operations]) -> list[Operations]:
    """
    Функция сортирует по дате в порядке убывания
    :param operations: список операций
    :return: отсортированный список операций в порядке убывания
    """
    return sorted(operations, key=lambda operation: operation.date, reverse=True)




