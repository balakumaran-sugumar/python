# unordered key value pair similar to map in java
# e.g. {'key1':'value', 'key2':'value2'}
# Objects that are retried by key

my_dict = {'key1': 'value1', "key2": "value2"}
print(my_dict)

print(my_dict["key1"])

# multi dimensional dict
my_dict = {"key1": "value1", "key2": ["1", "2", 3], "key3": {"key4": "value4"}}

print(my_dict["key2"])

print(my_dict["key3"]["key4"])

# adding a new key value pair to the dict
my_dict["key5"] = "key5"

# getting the keys
print(my_dict.keys())

# getting the values
print(my_dict.values())

# getting the dict itself
# dict_items([('key1', 'value1'), ('key2', ['1', '2', 3]), ('key3', {'key4': 'value4'}), ('key5', 'key5')])
# values within the parenthesis are tuples
print(my_dict.items())





