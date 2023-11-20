while True:
    mode = input('Enter a mode: ')
    if mode == 'c':
        first = input('Enter the first number: ')
        second = input('Enter the second number: ')
        if (int(first) % int(second)) == 0:
            print(first, 'is a multiple of', second)
        else:
            print(first, 'is not a multiple of', second)
    elif mode =='q':
        print('Terminate the program..')   
        break 