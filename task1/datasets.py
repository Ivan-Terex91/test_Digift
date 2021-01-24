dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
              13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
              24: 'x', 25: 'y', 26: 'z'}

string1 = "12314"
expected_result1 = ['a', 'l', 'b', 'w', 'c', 'a', 'n', 'd', 'd']

string2 = "12314123"
expected_result2 = ['a', 'l', 'b', 'w', 'c', 'a', 'n', 'd', 'a', 'l', 'b', 'w', 'c', 'c']

first_dataset = (dictionary, string1, expected_result1)
second_dataset = (dictionary, string2, expected_result2)
