# List:-

l1 = [1,2,3,4,5]
l2 = [6,8,7,9]
l1.append(l2)
# Add the whole list l2 inside the list l1:
l1.append([11,22,33])
l1.append(10)
print(l1)

# Add the elements of l2 inside the list l1:
l1.extend(l2)
print(l1)

l1.reverse()
print(l1)

l1.insert(0, 0)
print(l1)
a = l1.pop(2)
print(a)
l2.sort(reverse=True)
print(l2)
