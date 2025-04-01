import random

# Set variables of each character. 2 each of lowercase letters, uppercase letters, digits, and special characters using ASCII decimal numbers
lower_1 = random.randint(97, 122)
lower_2 = random.randint(97, 122)
upper_1 = random.randint(65, 90)
upper_2 = random.randint(65, 90)
digit_1 = random.randint(48, 57)
digit_2 = random.randint(48, 57)
sym_1 = random.randint(33, 47)
sym_2 = random.randint(33, 47)

# Take all the randomly generated decimal numbers and convert them into their respective ASCII character and adds them to an array. 
gen_pass = [chr(lower_1), chr(lower_2), chr(upper_1), chr(upper_2), chr(digit_1), chr(digit_2), chr(sym_1), chr(sym_2)]

# Shuffles the array of characters
random.shuffle(gen_pass)

# Joins all the characters of the array into a single line
new_pass = "".join(gen_pass)

# Print generated password
print(new_pass)