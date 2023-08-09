# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input("Please enter a letter in the alphabet (a-z or A-Z): ")

if letter.lower() in 'aeiou':
    print(f"The letter {letter} is a vowel")
else:
    print(f"The letter {letter} is a consonant")

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
while True:
    phrase = input("Please enter a word or phrase: \n")
    
    if phrase.lower() == 'quit':
        break
    
    print(f"What you entered is {len(phrase)} characters long")

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

age = int(input("Input your dog's age (years): "))
if age <= 2:
    dog_years = age * 10
else:
    dog_years = 20 + (age - 2) * 7
    
print(f"Your dog's age in 'dog years' is {dog_years}")

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lengths of the three sides of the triangle:")
# side 1
a = float(input("a: "))
# side 2
b = float(input("b: "))
# side 3
c = float(input("c: "))

# equilateral triangle
if a == b == c:
    print(f"A triangle with sides of {a}, {b} & {c} is an equilateral triangle")
elif a != b and b != c and a != c:
# scalene triangle
    print(f"A triangle with sides of {a}, {b} & {c} is a scalene triangle")
# isosceles triangle
else:
    print(f"A triangle with sides of {a}, {b} & {c} is an isosceles triangle")


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

# initial fibonacci terms are 0, 1...
n1, n2 = 0, 1
# initial counter; keeps track of term
count = 0

# loop until 50 terms
while count < 50:
    print(f"term: {count} / number: {n1}")
    # fibonacci = sum of 2 previous nums
    nth = n1 + n2
    
    # newly calculated fibonacci numbers
    n1 = n2
    n2 = nth
    
    #increment term count
    count += 1

# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

# input month
month = input("Enter the month of the year (Jan - Dec): ")

# input day of month; ensure int
day = int(input("Enter the day of the month: "))

# Winter (Dec 21 to Feb and up to Mar 19)
if (month == 'Dec' and day >= 21) or month in ('Jan', 'Feb') or (month == 'Mar' and day < 20):
    season = "Winter"
# Spring (Mar 20 to May and up to Jun 20)
elif (month == 'Mar' and day >= 20) or month in ('Apr', 'May') or (month == 'Jun' and day < 21):
    season = "Spring"
# Summer (Jun 21 to Aug and up to Sep 21)
elif (month == 'Jun' and day >= 21) or month in ('Jul', 'Aug') or (month == 'Sep' and day < 22):
    season = "Summer"
# Fall (Sep 22 to Nov and up to Dec 20)
else:
    season = "Fall"

print(f"{month} {day} is in {season}")




