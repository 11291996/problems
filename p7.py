list = [3, 5, 7, -1, 2, -64, 23, 84, -10]
total = 1 
for _ in range(len(list)):
    if list[_] > 0:
        total *= list[_]
print('The product of positive numbers is', total)