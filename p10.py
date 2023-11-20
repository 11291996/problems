#inputs a sentence
string = str(input('Enter a sentence: '))
#creating a list iterable only with alphabets 
string_alpha = list(filter(str.isalnum, string))
#making the iterable a list
string_alpha = ''.join(string_alpha).lower()
if string_alpha == string_alpha[::-1]:
    print('Palindrome.')
else: 
    print('No palindrome.')