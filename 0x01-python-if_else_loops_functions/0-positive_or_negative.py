#!/usr/bin/python3
import random
number = random.randint(-10, 10)
output = ''
if number < 0:
    output = 'negative'
elif number > 0:
    output = 'positive'
else:
    output = 'zero'
print(f'{number} is {output}')
