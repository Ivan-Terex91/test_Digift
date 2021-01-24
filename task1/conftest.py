import pytest
from datasets import first_dataset, second_dataset


@pytest.fixture(scope="function", params=[first_dataset, second_dataset])
def prepare_data(request):
    """Фикстура подготовки и очистки данных"""
    dictionary, string, expected_result = request.param
    yield dictionary, string, expected_result
    print("\nCleaning prepared data")
    del dictionary
