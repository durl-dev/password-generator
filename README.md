# Random Password Generator
This is a simple Python script that generates a random string of characters that includes 2 each of lowercase letters, uppercase letters, digits, and special characters.

## How It's Made:

**Tech used:** Python

I created 8 variables to generate an 8-character long password. Each variable generates a random number from a range of numbers that correspond to ASCII / Unicode decimal numbers for the given type of character. Once the numbers are generated, an array is created and then the elements are shuffled to add further randomization. 

Once shuffled, the elements of the array are joined together to create one line of characters which then gets printed.
