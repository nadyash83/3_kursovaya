from pprint import pprint

from config import OPERATION_PATH
from src.utils import load_operation, get_instances, sort_operation_by_date, get_executed_operations


def main():
    operations = load_operation(OPERATION_PATH)
    instances = get_instances(operations)
    executed_operation = get_executed_operations(instances)
    sort_operation = sort_operation_by_date(executed_operation)
    for operations in sort_operation[:5]:
        print(operations)


if __name__ == '__main__':
    main()
