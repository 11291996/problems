first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
if first != second:
    print('=====',first,'=====')
    for _ in range(9):
        answer = first * (_ + 1)
        print(first,'*',_ + 1,'=',format(answer, '>2'))
    print('=====',second,'=====')
    for _ in range(9):
        answer = second * (_ + 1)
        print(second,'*',_ + 1,'=',format(answer, '>2'))
else:
    print('=====',first,'=====')
    for _ in range(9):
        answer = first * (_ + 1)
        print(first,'*',_ + 1,'=',format(answer, '>2'))