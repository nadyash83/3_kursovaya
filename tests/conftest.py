from datetime import datetime

import pytest
from src.models import Operations


@pytest.fixture
def operation_instances():
    operation_EXECUTED = Operations(
        pk=123,
        date="2019-08-26T10:50:58.294041",
        state="EXECUTED",
        operation_amount={
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="Перевод организации",
        from_="Счет 75106830613657916952",
        to="MasterCard 7158300734726758"
    )
    operation_CANCELED = Operations(
        pk=594226727,
        date="2020-08-26T10:50:58.294041",
        state="CANCELED",
        operation_amount={
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="Перевод организации",
        from_="Visa Platinum 1246377376343588",
        to="Счет 14211924144426031657"
    )
    return [operation_EXECUTED, operation_CANCELED]

@pytest.fixture
def operation_dict():
    return [
        {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
        },
        {}]
