lst1 = [1,1,1,3,3,8,4,4,5,5,2,2,9]
print(lst1)
lst2 = []
for i in lst1:
    n = lst1.count(i)
    if n == 1:
        lst2.append(i)
print(f"список неповторяющихся элементов: {lst2}")
