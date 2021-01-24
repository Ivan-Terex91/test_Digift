import psycopg2
import pytest

from datasets import first_dataset, second_dataset


@pytest.fixture(scope="function", params=[first_dataset, second_dataset])
def prepare_data(request):
    """Фикстура подготовки и очистки данных"""
    code_table_data, status_table_data, expected_result = request.param
    con = psycopg2.connect(
        database="digiftDB",
        user="ivan",
        password="undead",
        host="127.0.0.1",
        port="5432"
    )

    cur = con.cursor()
    for code in code_table_data:
        cur.execute(
            f"INSERT INTO code VALUES({code})"
        )

    for status_string in status_table_data:
        cur.execute(
            f"INSERT INTO status VALUES({status_string[0]}, '{status_string[1]}', '{status_string[2]}', {status_string[3]})"
        )
    con.commit()

    yield con, expected_result
    print("\nCleaning prepared data")

    cur = con.cursor()
    cur.execute(
        f"DELETE FROM code"
    )
    con.commit()
    con.close()
