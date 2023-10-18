# ----------------------------------------Hello world------------------------------

# print("Hello Ahmed")

#------------------------------------------String-------------------------------------

# name = "Ahmed Raza"
# print(name)
# print(type(name))
# print(id(name))



# not recommended (error show nh kr raha hai)
# name = "Ahmed Raza"
# name = 786
# print(name)
# print(type(name))
# print(id(name))





# name : str = "Ahmed Raza"
# print(name)



# install mypy extension (phir apko erroe show hojayega)     (yeh error jupyter per nh ayega 'ipynb')

#name : str = 786                # (find error in terminal you can type  'mypy hello-world.py' on terminal phir apko error show hojaega)
#print(name)                     #(lekin yeh code run ho jayega)






# name : list[str] = ['Ahmed' ,'Raza' , 'Aemi']
# print(name) # print
# print(type(name)) # type
# print(id(name)) # physical address


# # yeh iski value ko consider kr raha hai

# print(( i for i in dir(name) if "__" not in i )) # methods and attributes





# error because type list is string
# name : list[str] = ['Ahmed' ,'Raza' , 'Aemi' , 786]
# print(name) # print
# print(type(name)) # type
# print(id(name)) # physical address


# # yeh iski value ko consider kr raha hai

# print(( i for i in dir(name) if "__" not in i )) # methods and attributes






# name : tuple[str,int,float] = ("Ahmed Raza" , 786 , 74.5)
# print(name) # print
# print(type(name)) # type
# print(id(name)) # physical address


# # yeh iski value ko consider kr raha hai

# print(( i for i in dir(name) if "__" not in i )) # methods and attributes






# name : any = ("Ahmed Raza")
# print(name) # print
# print(type(name)) # type
# print(id(name)) # physical address


# # yeh iski value ko consider kr raha hai

# print(( i for i in dir(name) if "__" not in i )) # methods and attributes