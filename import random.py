import random

friends = [
    'James','Ollie',
'Johnny','Aron','Sheref']

# random.randint(1, 5) --> picks a number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(friends) # picks a random friend
print('Who should I meet at school on Monday?')
print(selected)