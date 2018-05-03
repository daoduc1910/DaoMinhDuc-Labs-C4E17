#pythonic

nums = [1, 5, -9, -81, 55, 123, -135]

x = int(input("Enter a nubmer: "))

#in

if x in nums: # in dùng đc cả cho list lẫn dictionary
    print("Found in list")
else:
    print("Not found in list")

#occurences => count()
c = nums.count(x)
print(c)
