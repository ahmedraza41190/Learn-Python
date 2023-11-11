# # Creating a Dictionary

# from typing import Dict

# my_dict: Dict[str, int] = {'apple': 5, 'banana': 3}
# print(my_dict)  # Output: {'apple': 5, 'banana': 3}





# Accessing Values

# value = my_dict['apple']
# print(value)  # Output: 5




# Adding Key-Value Pairs

# my_dict['cherry'] = 7
# print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}





#                                                            Dictionary Methods


# clear()   (Removes all the elements from the dictionary.)

# my_dict.clear()
# print(my_dict)  # Output: {}





# copy()   (Returns a shallow copy of the dictionary.)

# copy_dict = my_dict.copy()
# print(copy_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}






# fromkeys()     (Creates a new dictionary with keys from a sequence and values set to a specified value.)

# sequence = ('apple', 'banana', 'cherry')
# new_dict = dict.fromkeys(sequence, 0)
# print(new_dict)  # Output: {'apple': 0, 'banana': 0, 'cherry': 0}





# get()    (Returns the value for a specified key if the key is in the dictionary.)

#                     key      message
# value = my_dict.get('apple', 'Not Found')
# print(value)  # Output: 5





# items()   (Returns a view object that displays a list of dictionary's key-value tuple pairs.)

#              keys and value
# items = my_dict.items()
# print(items)  # Output: dict_items([('apple', 5), ('banana', 3), ('cherry', 7)])






# keys()    (Returns a view object that displays a list of all the keys in the dictionary.)

# keys = my_dict.keys()
# print(keys)  # Output: dict_keys(['apple', 'banana', 'cherry'])





# pop()    (Removes the element with the specified key.)

#              key
# my_dict.pop('apple')
# print(my_dict)  # Output: {'banana': 3, 'cherry': 7}





# popitem()    (Removes the last inserted key-value pair.)

# my_dict.popitem()
# print(my_dict)  # Output: {'banana': 3}





# setdefault()   (Returns the value of the specified key. If the key does not exist, insert the key, with the specified value.)

# my_dict: Dict[str, int] = {'apple': 5, 'banana': 3}
# value = my_dict.setdefault('banana', 6)
# print(value)  # Output: 3






# update()      (Updates the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.)

# my_dict.update({'banana': 4})
# print(my_dict)  # Output: {'banana': 4}






# values()      (Returns a view object that displays a list of all the values in the dictionary.)

# values = my_dict.values()
# print(values)  # Output: dict_values([4])