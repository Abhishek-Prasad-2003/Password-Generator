import string
import random

letters, numbers, symbols = list(string.ascii_letters), list(string.digits), list(string.punctuation)

def get_input():
    return input('Easy/Medium/Hard password to generate: ').capitalize()

def password_generate(user_input):

    if user_input == 'easy'.capitalize():
        shuffled_list = random.sample(letters, 10)#you can change it to numbers and punctuations
        random.shuffle(shuffled_list)
    elif user_input == 'medium'.capitalize():
        shuffled_list = random.sample(letters, 10) + random.sample(numbers, 10)
        random.shuffle(shuffled_list)

    elif user_input == 'hard'.capitalize():
        shuffled_list = random.sample(letters, 16) + random.sample(numbers, 10) + random.sample(symbols, 12)
        random.shuffle(shuffled_list)
    else:
       return f'Wrong input!'

    return ''.join(shuffled_list)

inp = get_input()
print(password_generate(inp))