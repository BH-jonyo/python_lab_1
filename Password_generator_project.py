##importing relevant modules
import string
import random

##list of all uppercase and lowercase characters in python
all_alphabets = list(string.ascii_letters)
#print(f'all the alphabets in the english language {all_alphabets}')
all_digits = list(string.digits)
#print(f'all numbers in the english language {all_digits}')
all_symbols = list(string.punctuation)
#print(f'all symbols in the english language {all_symbols}')

##How many letters they would like in their password
no_of_letters = int(input('How many letters would you like to have in your password?'))
#print(f'you chose {no_of_letters} letters')

##How many digits they would like in their password
no_of_digits = int(input('How many digits would you like to have in your password?'))
#print(f'you chose {no_of_digits} digits')

##How many symbils they would like to have in their password
no_of_symbols = int(input('How many symbols would you like to have in your password?'))
#print(f'you chose {no_of_symbols} symbols')

##set accumulator for password characters list
password_character_list = []

##Get the random letter for the password
##Randomly select the characters
for number in range (no_of_letters):
    #print(number)
##       select a random character from list of alphabets and append to the password characters list 
    random_letter = random.choice(all_alphabets)
    #print(random_letter)
    password_character_list.append(random_letter)
    
#print(password_character_list)

##set accumulator for password number list
password_number_list = []
##Get the random number for the password
##randomly select the characters
for number in range (no_of_digits):
## select a random character from list of alphabets and append to the password character list
    random_digit = random.choice(all_digits)
    #print(random_digit)
    password_number_list.append(random_digit)
    
#print(password_number_list)

##set accumulator for password number list
password_symbol_list =[]
##Get the random number for the password
##randomly select the characters
for number in range (no_of_symbols):
    #print(number)
## select a random character from list of alphabets and append to the password character list
    random_symbol = random.choice(all_symbols)
    #print(all_symbols)
    password_symbol_list.append(random_symbol)
    
#print(password_symbol_list)

## Add the lists to get the final_password_list and shuffle the final_password_list
final_password_list = password_character_list + password_number_list + password_symbol_list

print(final_password_list)
## Shuffling the final_password_list
random.shuffle(final_password_list)
print(final_password_list)

## Changing the final_password_list to string
final_password_list = str(final_password_list)
print(type(final_password_list))