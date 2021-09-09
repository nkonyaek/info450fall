a = []
b = None
c = ["a", "b", 3]
d = [["a", "b", 3], ["c", "d", 4]]

if a != None:
    print(*a, sep = ", ")
else:
    print("None")

if b != None:
    print(*b, sep = ", ")
else:
    print("None")

if c != None:
    print(*c, sep = ", ")
else:
    print("None")

if d != None:
    print(*d, sep = ", ")
else:
    print("None")