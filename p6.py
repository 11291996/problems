import random 
seed = int(input('Input random seed: '))
random.seed(seed)
first = random.randint(1,9)
second = random.randint(1,9)
print('The first number is', first)
print('The second number is', second)
answer = int(input('What is the product of two numbers? '))
if answer == first * second:
    print('Your answer is correct.')
else:
    print('Your answer is wrong.')