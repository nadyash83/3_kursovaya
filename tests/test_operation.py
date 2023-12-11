from datetime import datetime

from src.models import Operations

def test_operation_convert_date():
    operation = Operations(
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
    expected_date = datetime(2019, 8, 26, 10, 50, 58, 294041)
    assert operation.convert_data("2019-08-26T10:50:58.294041") == expected_date
