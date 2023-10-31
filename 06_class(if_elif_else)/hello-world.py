# from typing import Union
# PerType = Union[float, int]

# percentages : list[PerType] = [88, 99.9, 50, 51,65,70]

# grades : list[str] = []

# for per in percentages:
#     grade : str = ""

#     if (per >= 0) and (per < 33):
#         grade = "Fail"
#     elif (per >= 33) and (per < 40):
#         grade = "E"
#     elif (per >= 40) and (per < 50):
#         grade = "D"
#     elif (per >= 50) and (per < 60):
#         grade = "C"
#     elif (per >= 60) and (per <70) :
#         grade = "B"
#     elif (per >= 70) and (per <80) :
#         grade = "A"
#     elif (per >=80) and (per <= 100):
#         grade = "A+"

#     grades.append(grade)

# print(percentages)
# print(grade)








# If Statement

# x: int = 10
# if x > 5:
#     print("x is greater than 5")




# If-Else Statement

# x: int = 4
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")





# If-Elif-Else Statement

# x: int = 5
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")




# Nested If-Else-Elif

# x: int = 10
# y: int = 5
# if x > 5:
#     if y > 5:
#         print("x and y are both greater than 5")
#     else:
#         print("x is greater than 5 but y is not")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")






# Static Type Variables

# x: int = 10
# y: str = "Hello"
# z: float = 3.14





# Union and Optional Types

# from typing import Union, Optional

# def greet(name: Optional[str] = None) -> str:
#     if name is None:
#         return "Hello, Guest!"
#     else:
#         return f"Hello, {name}!"

# age: Union[int, str] = "Twenty"
# print(greet())
# print(greet("John"))






# Zip Function with Lists

# names: list[str] = ["Alice", "Bob", "Charlie"]
# ages: list[int] = [25, 30, 35]

# zipped = zip(names, ages)
# for name, age in zipped:
#     print(f"{name} is {age} years old")






# Sorting a List of Tuples

# tuples: list[tuple[str, int]] = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
# sorted_tuples = sorted(tuples, key=lambda x: x[1])
# print(sorted_tuples)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]