first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
first_ = first + 0 
second_ = second + 0 
def multiply(first, second):
    a = int(first) - int(second)
    _ = ((a)**2)**(1/2)
    if first > second:
        total = first
        for i in range(int(_)):   
            total = total * (first - 1)
            first -= 1
    else:
        total = second
        for i in range(int(_)): 
            total = total * (second - 1)
            second -= 1
    if a > 0:
        print('The product of', second_, 'to', first_, 'is', total)
    elif a == 0:
        print(None)
    else:
        print('The product of', first_, 'to', second_, 'is', total)
multiply(first, second) 