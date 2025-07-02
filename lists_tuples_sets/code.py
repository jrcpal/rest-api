# can modify, add, remove elements in a list. Lists keeps the order
l = ["Jane", "Jess", "Joey"]
# cannot modify, add, or remove items in a tuple. Tuples keep the order
t = ("Jane", "Jess", "Joey")
# can modify, add , remove items in a set. Set does not keep the order. Set does not allow duplicate elements 
s = {"Jane", "Jess", "Joey"}


# subscript notation allows to access individual element in list or tuple by index
print(l[0])
print(t[0])

l[0] = "Sandy"
print(l)

l.append("Dan")
print(l)


s.add("Dan")
print(s)