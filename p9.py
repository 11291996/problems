while True:
    address = str(input('Enter your e-mail address: '))
    index = address.rfind('@')
    if index == -1:
        print('Incorrect e-mail address')
        break
    print('Username:', address[0:index])
    print('Hostname:', address[index+1:])
