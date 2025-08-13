lst = ['Apple', 'Guava', 'Mango', 'Watermelon']

print("length of list :", len(lst))
print("first element :", lst[0])
print("last element :", lst[-1])

lst.append('Grape')
print("Updated list: ", lst)

lst.remove('Guava')
print("Updated list: ", lst)

lst.sort()
print("Sorted list: ", lst)

lst.pop(1)
print("Updated list: ", lst)

lst.reverse()
print("reversed list: ", lst)