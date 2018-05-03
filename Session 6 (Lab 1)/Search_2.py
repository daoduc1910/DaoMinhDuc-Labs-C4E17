nums = [3, 4, -99, 78, 4, -99, 3]

x = int(input("Enter a number: "))

#must not use count() or in or index()
found = False
for num in nums:
    if num == x:
        found = True
        break

# print(found)

if found:   # tương đương if True:
    print("Found")
else:
    print("Not found")
