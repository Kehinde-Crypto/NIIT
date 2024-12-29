text = "Hello"
print(len(text))  # Output: 5

text = "hello"
print(text.upper())  # Output: "HELLO"

text = "HELLO"
print(text.lower())  # Output: "hello"

text = "   Hello   "
print(text.strip())  # Output: "Hello"

text = "Hello World"
print(text.replace("World", "Python"))  # Output: "Hello Python"

text = "apple,banana,cherry"
fruits = text.split(",")  # Output: ['apple', 'banana', 'cherry']

fruits = ['apple', 'banana', 'cherry']
text = ", ".join(fruits)
print(text)  # Output: "apple, banana, cherry"

text = "Hello World"
print(text.find("World"))  # Output: 6

text = "Hello"
print(text.startswith("He"))  # Output: True

text = "Hello"
print(text.endswith("lo"))  # Output: True

#List Methods in Python


fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ["apple", "banana", "cherry"]

fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Output: ["apple", "cherry", "banana"]

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry"]

fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(1)
print(removed_item)  # Output: "banana"
print(fruits)  # Output: ["apple", "cherry"]

#NOTE THE DIFFERENCE BETWEEN THE REMOVE KEY WORD AND THE POP KEYWORD IS THAT ,  THAT REMOVE KEY WORD : REMOVE THE KEY WORD AND  AND POP REMOVES THE INDEX VALUES

fruits = ["apple", "banana", "cherry"]
index_of_banana = fruits.index("banana")
print(index_of_banana)  # Output: 1

#sort(): Sorts the list in ascending order (can also sort in descending order if reverse=True is specified).

#python
#Copy code
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]


fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ["cherry", "banana", "apple"]

fruits = ["apple", "banana"]
more_fruits = ["cherry", "date"]
fruits.extend(more_fruits)
print(fruits)  # Output: ["apple", "banana", "cherry", "date"]

fruits = ["apple", "banana", "apple"]
count_of_apple = fruits.count("apple")
print(count_of_apple)  # Output: 2

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []
