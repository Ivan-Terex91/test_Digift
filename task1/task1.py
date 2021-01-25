
def test_decode_data(prepare_data):
    """Декодируем данные string через dictionary"""
    dictionary, string, expected_result = prepare_data
    received_result = list()
    while string:
        temp = string[:2]
        received_result.append(dictionary.get(int(temp[0])))
        if len(temp) == 2:
            received_result.append(dictionary.get(int(temp))) if int(temp) in dictionary else None
        string = string[1:]

    assert received_result == expected_result, f"Expected {expected_result} \n got {received_result} "
