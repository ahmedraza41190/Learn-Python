from typing import Dict, Union, Optional
import pprint


# Key = Union[int,str] # create custom type
# Value = Union[int, str, list, dict, tuple, set]

# #          key , value
# data : Dict[Key,Value] = {#key : value
#                         "fname":"Muhammad Aslam",
#                         "name":"Muhammad Qasim",
#                         "education": "MSDS"
#                         }

# pprint.pprint(data)







# Setting up Static Typing

from typing import Any, Optional, Union






# Creating Dictionaries

# from typing import Dict

# #           key : value
# my_dict: Dict[Any, Any] = {
#     1: "one",
#     "two": 2,
#     (3, 4): [3, 4]
# }






# Using Optional Type

# from typing import Dict

# my_optional_dict: Dict[Any, Optional[int]] = {
#     1: 10,
#     "two": None,
#     (3, 4): 34
# }







# Using Union Type

# from typing import Dict

# my_union_dict: Dict[Any, Union[int, str]] = {
#     1: "one",
#     "two": 2,
#     (3, 4): "three-four"
# }






# Dictionary Comprehensions

# squared_numbers = {i: i**2 for i in range(5)}





# Swapping Keys and Values

# swapped_dict = {v: k for k, v in my_dict.items()}