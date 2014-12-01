"""Assignment 6: Final Practice

In the interests of helping y'all prep for the final, the last assignment is
going to be an opportunity to practice skills for the final rather than some
random project (which will still be available as extra credit).

Implement the following functions. Please follow the directions. I may be 
telling you to do something differently than you would normally do it, but
this is because I want you to practice certain skills, so please do them.

Notes:
    - You may not use exception handling of any kind (you may not use
      try/except blocks).
    - You may not use recursion in any way (calling a function from itself).
    - You may not use any imports.
    - This is intended to help you prepare for your final. As a result, you may
      only use concepts that we covered in class.
    - Just so this is perfectly clear, submissions with syntax errors, infinite
      loops, or that crash will get a 0 grade. It is *YOUR* responsibility to 
      make sure that your code runs.
    - You must do your own work. You may talk about ideas with other students,
      but you should neither look at anyone else's code let anyone else ever
      look at your code. Both behaviors are grounds for failing the assignment.
    - Download the file and fill in the functions. Don't remove the comments.
      Don't delete any functions. Just replace the "pass" statements with
      the implementation for your functions.
      
Grading Rubric:
    - Problems: 100 points (graded automatically)
    - Style/Following Instructions: 40 points (graded manually)
"""

"""Problem 1: 5 points

Using a while loop, write a function that will give the sum of all of the 
numbers in a list. It should return the total sum of all of the numbers.
"""

def SumWithWhile(numbers):
    pass


"""Problem 2: 5 points

This time, use a for loop. Write a function that will give the sum of 
all of the numbers in a list. It should return the total sum of all of
the numbers.
"""

def SumWithFor(numbers):
    pass


"""Problem 3: 5 points

Write a function that returns the first n even numbers. You must use a loop (you
may choose between using for or while). You should return a list of numbers
starting with 0 (0 is the first even number in my book).
"""

def EvenNumbers(n):
    pass


"""Problem 4: 10 points
Using a *for* loop, write a function that returns the first n powers of 2. You
must use a for loop and return a list of the powers of 2, starting with 2^0 (1).

Example:
    PowersOf2(4) returns [1, 2, 4, 8]
"""

def PowersOf2(n):
    pass


"""Problem 5: 10 points

Write a function to reverse a string. You must use at least one loop (you may
choose between for or while) in this function. It should return the reversed
string.
"""

def ReverseString(s):
    pass
    
"""Problem 6: 10 points

Using your ReverseString function, write a function to determine whether or not
a given string is a palindrome (a palindrome is a word that is the same forwards
as backwards like racecar or pop). You should return a boolean: True if it is a
palindrome, False otherwise.
"""

def IsPalindrome(s):
    pass

""" Problem 7: 10 points
Write a function to determine if one string is an anagram of another string 
(anagrams are words that use the same letters to form different words, like 
listen and silent). Return a boolean: True if the two strings are anagrams,
False otherwise.

Note: You don't have to, but you can use the sorted function on a string. For 
example, if you call sorted('hello'), you get back the list 
['e', 'h', 'l', 'l', 'o'].
"""

def AreAnagrams(a, b):
    pass


"""Problem 8: 15 points

Given a list containing comparable elements, return whether or not the list 
contains duplicates (True if there are duplicates, False otherwise). You
must use at least one loop (you can choose between for and while)
"""

def HasDuplicates(items):
    pass
    

"""Problem 9: 15 points
Write a function that will take in two strings (s and char) and tell how many
times char occurs in the string s. It should return an int representing the
number of occurrences of char in s.

Note: char will always be a 1-character string.

Examples:
    CountOccurrences('hello', 'l') returns 2 
    CountOccurrences('hello, world', 'l') returns 3
    CountOccurrences('hello', 'z') returns 0
"""

def CountOccurrences(s, char):
    pass

"""Problem 10: 15 points 

Write a simple calculator that will perform a calculation and then return the
result. The parameters x and y will be numbers (could be floats or ints; don't
worry about trying to cast any values to any particular type). The operator
parameter will be one of the constants defined below.

Your program must not raise any exceptions, so you must prevent it from trying
to divide or mod by 0. If the calculation cannot be done safely, it should
return None.

You may not hardcode any strings in your implementation; use the constants that
have been defined instead.

Examples:
    Calculate(ADD, 4, 8) returns 12
    Calculate(MODULO, 4, 0) returns None
"""

ADD = '+'
SUBTRACT = '-'
MULTIPLY = '*'
DIVIDE = '/'
MODULO = '%'

def Calculate(opearator, x, y):
    pass


"""Problem 11: 15 points 

Write a function that returns a dictionary containing all of the characters in a
given string as keys and the number of times it occurred as the value. This 
should account for all characters in the string (including punctuation and
whitespace).

Examples: 
    CharacterCounts('hello') returns {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    CharacterCounts('hi mom') returns {'h': 1, 'i': 1, 'm': 2, 'o': 1, ' ': 1}
"""

def CharacterCounts(s):
    pass


"""Problem 12 (Extra Credit): 15 points

Write a function to make change. Given some number of cents, return a dictionary
 containing the minimum number of quarters, dimes, nickles, and pennies 
 necessary to give the correct change. 

Note: that even if there are no coins of a certain denomination needed, you
should still include that in the dictionary, it's value will just be zero.

Note: you must use the modulo operator (%) and/or some sort of a loop. 

Examples:
    MakeChange(41) returns {'quarters': 1, 'dimes': 1, 'nickles': 1, 'pennies': 1}
    MakeChange(248) returns {'quarters': 9, 'dimes': 2, 'nickles': 0, 'pennies': 3}
"""

def MakeChange(cents):
    pass
