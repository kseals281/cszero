"""Extra Credit: Equations

This extra credit assignment asks you to implement a collection of common 
equations. The idea behind this project is to give you more practice with 
various operators, but it's also to give you a chance to see how you can easily
make computers do work for you in the real world.

This assignment also requires you to test your code. Exciting!! You don't have
to use a real testing framework; all you have to do is use the Assert function
defined below. For each function you implement, you must also implement test
cases to make sure that your code works.

Start by copying this starter code, and just fill in the functions underneath
each comment. Don't remove the comments, don't change the order of things. Just
fill in the spaces where I ask you to. Please follow the format of the example.
Implement the function. Define your test function. Then call your test cases.

IF YOU DO NOT FOLLOW THE FORMAT & EXAMPLES HERE, YOU WILL NOT GET CREDIT.

This should be one of the easier extra credit assignments because each formula
is independent of each other formula.

Also, note that you must write out your own implementation for each of these
functions. If you run across a built-in function in Python that does any of this
for you, feel free to document it in the comments, but don't use it for your
implementation. The goal is to get you to practice this stuff.

Grading
    - Each problem is worth up to 5 hard points
      * Each formula's implementation is worth up to 2 hard points.
      * The test function for each formula is worth 1 hard point.
      * The test cases you think of for each function is worth up to 2 hard points.
    - You get 0 points for a problem if your test cases don't pass.
    - Remember! You will have to explain what you did for each problem to me.
      If you cannot explain (and potentially replicate) your work, you will not
      receive credit! And if it is egregious and a case of *clear* cheating, then
      I will have to take the appropriate actions (including failing you in the 
      course). There is 0 tolerance for cheating here. You have been warned.
      * You may discuss ideas with your friends, but you must understand what you
        are doing and implement the code yourself. 
"""

################################################################################
# Constants & Helper Functions
################################################################################

RED = '\033[91m'
GREEN = '\033[92m'

def Color(color, text):
    return '{0}{1}\033[0m'.format(color, text)

def Assert(condition, description):
    if not condition:
        print Color(RED, 'FAILED: {0}'.format(description))
    else:
        print Color(GREEN, 'PASSED: {0}'.format(description))


################################################################################
# Example
################################################################################

"""Sum

Define a function called Sum that takes in a parameter called "numbers". The
numbers parameter will contain an iterable of numbers. The Sum function should
return the sum of all of those numbers.
"""

# Define Sum here:
def Sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
    
# Define TestSum here:
def TestSum(numbers, expected_value):
    actual_value = Sum(numbers)
    message = 'TestSum({0}). Expected: {1}. Actual: {2}'.format(
        numbers, expected_value, actual_value)
    Assert(actual_value == expected_value, message)
    
    
# Write Tests for Sum here:
TestSum([], 0)
TestSum([1, 2, 3, 4], 10)
TestSum([-1, 5], 4)


################################################################################
# Problems
################################################################################

"""Absolute Value

Write a function called AbsoluteValue that will return the absolute value of a given
number n. Absolute value is basically just getting the positive version of the
number.

For example, the absolute value of both -1 and 1 is 1.
"""

# Define AbsoluteValue here:
def AbsoluteValue(number):
	if number < 0:
		number *= -1
	return number

# Define TestAbsoluteValue here:
def TestAbsoluteValue(number, expected):
	actual_value = AbsoluteValue(number)
	message = 'TestAbsoluteValue({0}). Expected {1}. Actual: {2}'.format(number, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for AbsoluteValue here:
TestAbsoluteValue(1, 1)
TestAbsoluteValue(-5, 5)
TestAbsoluteValue(-3, 3)


"""Arithmetic Mean (Average)

Write a function called ArithmeticMean that will take in an iterable of numbers
(could be integers and/or floats) and returns the average of all of the numbers.
The parameter containing the numbers should be called "numbers".

Note: even if the iterable contains all ints, I should see a float average.
"""

# Define Mean here:
def Mean(numbers):
	total = 0
	for number in numbers:
		total += number
	return (total / float(len(numbers)))

# Define TestMean here:
def TestMean(numbers, expected):
	actual_value = Mean(numbers)
	message = 'TestMean({0}). Expected {1}. Actual: {2}'.format(numbers, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for Mean here:
TestMean([2, 4, 6, 8], 5)
TestMean([1, 2, 3, 4], 2.5)


"""Median

Write a function called Median that will take in a parameter called "numbers" that contains
an iterable of numbers. Median should return the middle number in that list. If the list
contains an even amount of numbers, you should average of the two middle numbers.

Note: You may assume that len(numbers) will return the length of the numbers parameter.
Note: You may not assume that the iterable is sorted. You should deal with that.
"""

# Define Median here:
def Median(numbers):
	numbers.sort()
	if (len(numbers) % 2) == 0:
		middle = (numbers[len(numbers) / 2] + numbers[(len(numbers) / 2) + 1]) / 2
	else:
		middle = numbers[len(numbers) / 2]
	return middle

# Define TestMedian here:
def TestMedian(numbers, expected):
	actual_value = Median(numbers)
	message = 'TestMedian({0}). Expected {1}. Actual: {2}'.format(numbers, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for Median here:
TestMedian([2, 3, 4, 1, 5], 3)
TestMedian([2, 6, 4, 10, 8], 6)


"""Pythagorean Theorem

Create a function called SatisfiesPythagoreanTheorem. It should take in a set of
three numbers (a, b, c) as parameters and return True if the Pythagorean Theorem
holds for that set of numbers and False otherwise.
"""

# Define SatisfiesPythagoreanTheorem here:
def SatisfiesPythagoreanTheorem(a, b, c):
	if ((a*a) + (b*b)) == (c*c):
		return True
	else:
		return False

# Define TestSatisfiesPythagoreanTheorem here:
def TestSatisfiesPythagoreanTheorem(a, b, c, expected):
	actual_value = SatisfiesPythagoreanTheorem(a, b, c)
	message = 'TestSatisfiesPythagoreanTheorem({0}, {1}). Expected {3}. Actual: {4}'.format(a, b, c, expected, actual_value)
	Assert(actual_value == expected, message)	

# Write tests for SatisfiesPythagoreanTheorem here:
TestSatisfiesPythagoreanTheorem(3, 4, 5, True)
TestSatisfiesPythagoreanTheorem(2, 4, 1, False)



"""Distance Formula

Create a function called DistanceFormula that implements the distance formula. It
will take in two tuples, named point1 and point2. Each tuple will contain two
values, the x and y coordinates. In other words, point1 could be (2, 4) where x = 2
and y = 4.

This function should return the distance between the two points as a float.

Google the distance formula if you don't know it...but don't Google the Python 
implementation of the distance formula!
"""

# Define DistanceFormula here:
def DistanceFormula(point1, point2):
	x = point2[0] - point1[0]
	x **= 2
	y = point2[1] - point1[1]
	y **= 2
	
	x += y
	
	return (x**0.5)
	
# Define TestDistanceFormula here:
def TestDistanceFormula(point1, point2, expected):
	actual_value = DistanceFormula(point1, point2)
	message = 'TestDistanceFormula({0}, {1}). Expected {2}. Actual: {3}'.format(point1, point2, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for DistanceFormula here:
TestDistanceFormula((3, 2), (4, 1), (2**0.5))
TestDistanceFormula((3, 2), (1, 2), 2)

"""Quadratic Equation

Write a function called QuadraticEquation that implements the quadratic equation. It
should take in 3 parameters (a, b, and c) and it should return a tuple containing 
the two values found by the equation. Two values because of that whole +/- thing.

Note: To return a tuple, you can just do something like "return value1, value2"
(minus the quotes, of course)
"""

# Define QuadraticEquation here:
def QuadraticEquation(a, b, c):
	x = b ** 2
	x += -4 * (a * c)
	x **= 0.5
	
	y = (b * -1) + x
	z = (b * -1) - x
	
	y /= (2 * a)
	z /= (2 * a)
	
	x = (y, z)
	
	return x
	

# Define TestQuadraticEquation here:
def TestQuadraticEquation(a, b, c, expected):
	actual_value = QuadraticEquation(a, b, c)
	message = 'TestQuadraticEquation({0}, {1}, {2}). Expected {3}. Actual: {4}'.format(a, b, c, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for QuadraticEquation here:
TestQuadraticEquation(1, 3, -4, (1, -4)) 

"""Prime Factorization

Write a function called PrimeFactorization that returns the prime factorization of
a given number n. It should return a dictionary containing the factors and their
counts.

For example, if n is 8, then the function should return {2: 3} because the prime 
factor is 2 and the number of times it goes into 8 is 3.

If n is 12, the result should be {2: 2, 3: 1} because it 2 goes into 12 2 times and 
3 goes in 1 time.

Note: Unless you decide to make this hard on yourself, you should not have to check
the primality of any numbers. However, if you implement your algorithm where you
need to check if a number is prime, define your IsPrime function in the allocated
space below (you did this in whirlybird already...right?)
"""

# [Optional] Define IsPrime(x) here:
def IsPrime(x):
    test_number = 1.0
    if test_number >= x:
        return False
    while test_number <= x:
        result = x % test_number
        if result == 0 and test_number != 1.0 and test_number != x:
            return False
        if test_number == x:
            return True
        test_number += 1.0

# Define PrimeFactorization here:
def PrimeFactorization(n):
	factors = dict([('1', 1), (str(n), 1)])
	if IsPrime(n) == True:
		return factors
	else:
		del factors['1'], factors[str(n)]
		n = int(n)
		while IsPrime(n) == False:
			for i in xrange(n - 1, 1, -1):
				if ((float(n) / i) % 1) == 0:
					if str(n / i) in factors:
						factors[str(n / i)] += 1
					else:
						factors[str(n / i)] = 1
					n = i
		if str(n) in factors:
			factors[str(n)] += 1
		else:
			factors[str(n)] = 1
		return factors

# Define TestPrimeFactorization here:
def TestPrimeFactorization(n, expected):
	actual_value = PrimeFactorization(n)
	message = 'TestPrimeFactorization({0}). Expected {1}. Actual: {2}'.format(n, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for PrimeFactorization here:
TestPrimeFactorization(12, {'2': 2, '3': 1})
TestPrimeFactorization(15, {'3': 1, '5': 1})
TestPrimeFactorization(8, {'2': 3})
TestPrimeFactorization(5, {'1': 1, '5': 1})


"""Fibonacci

Remember in lab that one time when we did Fibonacci? Well, now we have the tools
to do it *way* better. Write a function called Fibonacci that will return the
nth Fibonacci number. It should take in one parameter, n, that states which
Fibonacci number to return.

If n is less than 1, you should return None. 
The first Fibonacci number is 1.
The second Fibonacci number is 1.
Each subsequent Fibonacci number is determined by adding the previous two.
So the third Fibonacci number is 2.
The fourth Fibonacci number is 3.
And so on...

You may use loops and/or recursion (if you don't know what recursion is, don't 
worry about it).
"""

# Define Fibonacci here:
def Fibonacci(n):
	if n < 1:
		return None
	a = 1
	b = 1
	for i in xrange(3, n + 1):
		c = a + b
		a, b = b, c
	return c

# Define TestFibonacci here:
def TestFibonacci(n, expected):
	actual_value = Fibonacci(n)
	message = 'TestFibonacci({0}). Expected {1}. Actual: {2}'.format(n, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for Fibonacci here:
TestFibonacci(-4, None)
TestFibonacci(5, 5)
TestFibonacci(13, 233)


"""Triangle Numbers

Triangle numbers are attained by adding consecutive integers. They're called 
triangle numbers because you can create perfect triangles (pyramids) from each of 
them.

The first triange number is 1.
The second triangle number is 3 (1 + 2)
The third triangle number is 6 (1 + 2 + 3)
The fourth triangle number is 10 (1 + 2 + 3 + 4)

Write a function called TriangeNumber that takes in one parameter (n) and 
returns the nth triangle number. If n is less than one, the function should
return None.
"""

# Define TriangeNumber here:
def TriangeNumber(n):
	if n < 1:
		return None
	triangle = 0
	for i in xrange(1, n + 1):
		triangle += i
	return triangle

# Define TestTriangleNumber here:
def TestTriangleNumber(n, expected):
	actual_value = TriangeNumber(n)
	message = 'TestTriangleNumber({0}). Expected {1}. Actual: {2}'.format(n, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for TriangleNumber here:
TestTriangleNumber(4, 10)
TestTriangleNumber(5, 15)
TestTriangleNumber(6, 21)


"""Square Numbers

Square numbers are attained by adding consecutive odd integers. They're called 
square numbers because you can create perfect squares from each of them.

The first square number is 1.
The second square number is 4 (1 + 3)
The third square number is 9 (1 + 3 + 5)
The fourth triangle number is 16 (1 + 3 + 5 + 7)

Write a function called SquareNumber that takes in one parameter (n) and 
returns the nth square number. If n is less than one, the function should
return None.
"""

# Define SquareNumber here:
def SquareNumber(n):
	if n < 1:
		return None
	square = 0
	for i in xrange(1, n * 2, 2):
		square += i
	return square

# Define TestSquareNumber here:
def TestSquareNumber(n, expected):
	actual_value = SquareNumber(n)
	message = 'TestSquareNumber({0}). Expected {1}. Actual: {2}'.format(n, expected, actual_value)
	Assert(actual_value == expected, message)

# Write tests for SquareNumber here:
TestSquareNumber(5, 25)
TestSquareNumber(6, 36)
TestSquareNumber(7, 49)
