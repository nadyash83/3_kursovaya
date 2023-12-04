from datetime import datetime


class Operations:
    def __init__(
            self,
            pk: int,
            date: str,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str):
        self.pk = pk
        self.date = self.convert_data(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.convert_pay_info(from_)
        self.to = self.convert_pay_info(to)

    def convert_data(self, date: str) -> datetime.date:
        """
        Функция конвертирует формат даты
        :param date: дату
        :return: дату в нужном нам формате
        """
        con_date = datetime.fromisoformat(date)
        str_date = datetime.strftime(con_date, "%d.%m.%Y")
        return datetime.strptime(str_date, "%d.%m.%Y")

    def convert_pay_info(self, payment: str) -> str:
        """
        Функция конвертирует данные о платежах в формат для вывода на экран
        :param payment: payment
        :return: payment счет **1111
        """
        if payment:
            pay_list = payment.split()
            if payment.startswith("Счет"):
                num_pay = pay_list.pop()
                num_pay = f"**{num_pay[-4:]}"
                pay_list.append(num_pay)
            else:
                num_pay = pay_list.pop()
                num_pay = f"{num_pay[:4]} {num_pay[5:7]}** **** {num_pay[-4:]}"
                pay_list.append(num_pay)
                #pay_list = ["bhbhbh", "bjbbhj"]
            return " ".join(pay_list)
        return ""

    def __str__(self):
        return f"""
{self.date} {self.description}
{self.from_} -> {self.to}
{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}
                """
