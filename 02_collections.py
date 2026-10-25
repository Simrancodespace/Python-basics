# a) List, Tuple, and Dictionary Data Types
# Creating a list

my_list = [1, 2, 3, "apple", True]
print(my_list[0])
print(my_list[-1])
my_list[0] = 100
my_list.append("new")
my_list.insert(1, "orange")
my_list.remove("apple")
my_list.pop()
print(my_list)
print("Length:", len(my_list))

# Creating a tuple

my_tuple = (10, 20, 30, "apple", True)
print(my_tuple[0])
print(my_tuple[-1])
print("Count:", my_tuple.count(20))
print("Index:", my_tuple.index("apple"))
print("Length:", len(my_tuple))

# Creating a dictionary

my_dict = {
"name": "Simran",
"age": 19,
"city": " Navi Mumbai"
}
print(my_dict["name"])
my_dict["course"] = "B.Tech"
my_dict["age"] = 19
my_dict.pop("city")
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# b) Set and String Data Types
# Creating a set

my_set = {10, 20, 30, 40}
my_set.add(50)
my_set.remove(20)
my_set.discard(100)
print(my_set)
another_set = {40, 50, 60}
print("Union:", my_set.union(another_set))
print("Intersection:", my_set.intersection(another_set))
print("Length:", len(my_set))

# Creating a string

my_string = "Hello Python"
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.replace("Python", "World"))
print(my_string.split())
print(my_string.startswith("Hello"))
print(my_string.endswith("Python"))
print(len(my_string))

