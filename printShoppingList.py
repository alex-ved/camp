from greet import greet
greet("John")
with open('Shopping List.txt') as f:
    for item in f:
        print(item, end="")