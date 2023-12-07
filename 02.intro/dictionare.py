my_dict = {
    "key_1": 1,
    "key_2": 2,
    "key_3": 1,
    "key_1": 4
}
print(type(my_dict))
print(my_dict['key_2'])
print(my_dict.get('key_4', "Nu exista"))
my_dict.update({"key_5": 5})
print(my_dict)