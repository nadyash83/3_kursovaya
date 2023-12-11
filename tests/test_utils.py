from src.models import Operations
from src.utils import get_instances, get_executed_operations, sort_operation_by_date


def test_get_instances(operation_dict):
    operations = get_instances(operation_dict)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operations)
    assert len(operations) == 1
    assert operations[0].pk == 441945886

def test_get_executed_operations(operation_instances):
    operations = get_executed_operations(operation_instances)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operations)
    assert len(operations) == 1
    assert operations[0].state == "EXECUTED"

def test_sort_operation_by_date(operation_instances):
    operations = sort_operation_by_date(operation_instances)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operations)
    assert len(operations) == 2
    assert operations[0].date > operations[1].date


