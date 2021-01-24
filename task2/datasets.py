from datetime import datetime

# Первый тестовый набор данных
code_table_data1 = [1, 2, 3]
status_table_data1 = [
    (1, '2020-01-25 10:00:00', 'INFO', 1),
    (2, '2020-01-23 10:00:00', 'WARNING', 1),
    (3, '2020-01-25 10:01:00', 'ERROR', 1),
    (4, '2020-01-21 20:00:00', 'WARNING', 2),
    (5, '2020-01-19 23:00:00', 'ERROR', 2),
    (6, '2020-01-25 13:00:00', 'INFO', 2),
]
expected_result1 = [(1, 'ERROR', datetime(2020, 1, 25, 10, 1)), (2, 'INFO', datetime(2020, 1, 25, 13, 0))]

first_dataset = (code_table_data1, status_table_data1, expected_result1)

# Второй тестовый набор данных
code_table_data2 = [1, 2, 3]
status_table_data2 = [
    (1, '2020-01-15 10:00:00', 'INFO', 1),
    (2, '2020-01-13 11:00:00', 'WARNING', 1),
    (3, '2020-01-24 20:01:00', 'ERROR', 2),
    (4, '2020-01-24 20:00:00', 'WARNING', 2),
    (5, '2020-01-11 23:00:00', 'ERROR', 3),
    (6, '2020-01-23 13:00:00', 'INFO', 3),
]
expected_result2 = [(1, 'INFO', datetime(2020, 1, 15, 10, 0)), (2, 'ERROR', datetime(2020, 1, 24, 20, 1)), (3, 'INFO', datetime(2020, 1, 23, 13, 0))]

second_dataset = (code_table_data2, status_table_data2, expected_result2)
