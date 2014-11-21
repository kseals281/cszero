"""Howard SYCS100 Programming Assignment 5: Algorithms

Hooray!! It's time to start playing with algorithms :)

You are going to implement 4 algorithms. Instructions for
implementing each algorithm is below. 

This is a community project. You each have to submit your own solutions,
but you are allowed to discuss it in whatever ways you like that will
help you and your classmates understand it. In other words, for the
programming portion of this assignment, all cheating restrictions have
been lifted. Help each other understand!

This project is intended to have you practice a few things:
    - Using both while and for loops
    - Writing a program from scratch
    - Defining and calling functions
    - Using raw_input
    - Slightly more advanced string manipulation
  

Grading Rubric:
    - Functionality: 20 pts
	- Style: 20 pts (graded manually)
	- Comprehension (Individual): 20 pts
	- Comprehension (Group): 40 pts
	  * The whole class gets 40 * average grade for the quiz.
	  * At least 50 students must take the quiz or the whole class gets 0
	    points for the Group Comprehension score.
	  * If a student does not take the quiz, he gets 0% for the
	    whole assignment--so you'd better take the quiz!

Extra Credit:
	- For every % above 85% the quiz average is, everyone in the class gets
	  1 extra point.
	- Implement RecursiveBinarySearch (2 pts)
	- Implement InsertionSort (2 pts)
	- Implement MergeSort (4 pts)
	- Implement QuickSort (4 pts)
	- See Sabrina for more sorting algorithms and their values.

Notes:
    - No exception handling (try/except blocks) may be used.
	- No use of the 'global' keyword, and no imports.
	- You absolutely may not use the index() function.
	- You may not use the 'in' keyword in the search functions.
	- Don't use anything we haven't explicitly covered in class!
	- Let other students code review your code. I will blast you on style/not
	  following coding guidelines.
	- I'm happy to review submissions before the due date.
	- There will be no late submissions allowed for this assignment.
	  In other words, the 60%/40% policy does not apply.
    - Copy the current contents of this file as your starting point.
	  Do not delete the comments; just write the functions where I specify.
    - Follow directions *carefully*. The autograder isn't very tolerant.
    - You may define helper functions in this file, but be sure that you 
      definitely have all of the required functions and they are in the format
      described in the comments.
    - All functions take in a list as a parameter. 
      * You may assume the list is a list, but it could be empty.
      * You may assume all items in the list are comparable (e.g. <, ==, etc.
        all work as expected).
      * You may not assume the list is sorted.
"""

"""Linear Search

Define a function called LinearSearch that takes in an item to look for and a
list of items to search. The parameter containing the item to look for should
be named x. The parameter containing the list of items to search should be 
called items.

Linear search just iterates through each item in the list and compares it to the 
value being searched for. If the item is found in the list, then it should 
return the index at which the item was found. If the item is not found, the
function should return -1. 
"""

#Define LinearSearch here
def LinearSearch(x, items):
    for i in xrange(len(items)):
        if x == items[i]:
            return i
    return -1

"""Binary Search

Define a function called BinarySearch that takes in an item to look for and a
list of items to search. The parameter containing the item to look for should
be named x. The parameter containing the list of items to search should be 
called items.

Binary search is when you search through a *sorted* list and keep halving your
search space. You start in the middle, and then you compare the value in the 
middle to the value you're looking for. If your target value is less than the 
middle value, then you know (if it's there), it would be in the right left half.
If the target value is greater than the middle value, you know it'll be in the
right half. Once you know which side to look on, you go to the middle of what's 
left on that side and start the process over again. Eventually, you run out of
values you could look at. If you haven't found a match by then, you can return 
-1 (because it isn't there). If you find the item, return its index.

Remember: I said you can't assume the list is already sorted, so you should do
something about that.
"""

#Define BinarySearch here
def BinarySearch(x, items):
    items = BubbleSort(items)
    top = len(items) - 1
    bottom = 0
    while bottom <= top:
        middle = (top + bottom) / 2
        if x == items[middle]:
            return middle
        elif x > items[middle]:
            bottom = middle + 1
        elif x < items[middle]:
            top = middle - 1
    return -1

"""Bubble Sort

Define a function called BubbleSort that takes in a list of items to sort as a
parameter named items.

Bubble sort is an algorithm that walks through the list of items and, when it
compares 2 items, will swap them if they are out of order. Each time you run
through the list, you can stop looking at one more item at the end of the list.
Eventually, you run out of items to sort and you're done. (See the wikipedia
article for a good explanaton/visualization).
"""

# Define BubbleSort here
def BubbleSort(items):
    length = len(items)
    for i in xrange(len(items)):
        for x in xrange(length - 1):
            if items[x] > items[x + 1]:
                higherNumber = items[x]
                items[x], items[x + 1] = items[x + 1], items[x]
        length -= 1
    return items
    
"""Selection Sort

Define a function called SelectionSort that takes in a list of items to sort as a 
parameter named items.

Selection sort is an algorithm that will start at the beginning of the list and 
find the smallest item in the list and swap it with the one in the first spot.
Then it moves to the second spot, searches through the rest of the list to find
the smallest remaining algorithm and swaps so that it is in the second spot.
This process continues until we get to the end of the list and there's nothing
left to search/swap.
"""

# Define SelectionSort here
def SelectionSort(items):
    if len(items) == 0 or len(items) == 1:
        return items
    index = 0
    for x in xrange(len(items)):
		smallest = items[x]
		for i in xrange(x, len(items)):
			if items[i] <= smallest:
				smallest = items[i]
				index = i
		del items[index]
		items.insert(x, smallest)   
    return items

"""Extra Credit

Any problems that you want to do for extra credit, define them below this comment.
"""

def RecursiveBinarySearch(thing, items):
    items = SelectionSort(items)
    return RecursiveBinarySearching(items, len(items), 0, thing)

def RecursiveBinarySearching(items, top, bottom, thing):
    if bottom == top:
        return -1
    elif (bottom + 1) == top:
        return -1
    else:
        middle = (top + bottom) / 2
        if items[middle] > thing:
            top = middle
        elif items[middle] < thing:
            bottom = middle
        else:
            return middle
        return RecursiveBinarySearching(items, top, bottom, thing)


def InsertionSort(items):
    for i in xrange(len(items)):
        value = items[i]
        i -= 1
        while (i >= 0) and (items[i] > value):
            items[i + 1] = items[i]
            i -= 1
        items[i + 1] = value
    return items
                   

def MergeSort(items):
    if len(items) <= 1:
        return items
    
    left = []
    right = []
    middle = len(items) / 2
    
    for i in xrange(len(items)):
        if i < middle:
            left.append(items[i])
        elif i >= middle:
            right.append(items[i])

    left = MergeSort(left)
    right = MergeSort(right)

    del items[:]

    while len(left) > 0 :
        i = 0

        if left[i] >= right[i]:
            items.append(right[i])
            del right[i]

            if len(right) == 0:

                for i in xrange(len(left)):
                    items.append(left[i])
                break
        else:
            items.append(left[i])
            del left[i]

            if len(left) == 0:

                for i in xrange(len(right)):
                    items.append(right[i])
                break
        i += 1

    return items
    

def QuickSort(items):
    
    if len(items) > 1:

        less = []
        equal = []
        greater = []
        key = items[len(items) / 2]

        for i in items:
            if i > key:
                greater.append(i)
            elif i < key:
                less.append(i)
            elif i == key:
                equal.append(i)                    

        less = QuickSort(less)
        greater = QuickSort(greater)

        del items[:]

        if less == None:
            less = []
        if len(less) > 0:
            for i in xrange(len(less)):
                items.append(less[i])
                
        if equal == None:
            equal = []
        if len(equal) > 0:
            for i in xrange(len(equal)):
                items.append(equal[i])
            
        if greater == None:
            greater = []
        if len(greater) > 0:
            for i in xrange(len(greater)):
                items.append(greater[i])        

    return items

#x = 0
#items = ['map', 'disk', 'love', 'lose', 'beat']
#items = [5, 1, 0, 3, 6, 4, 9, 6, 7, 2, 61, 13, 17, 16, 18]
#list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
#print items
#items.sort()
#print items

#print LinearSearch(x, items)
#print BinarySearch(x, items)
#print RecursiveBinarySearch(x, items)
#print BubbleSort(items)
#print SelectionSort(items)
#print InsertionSort(items)
#print MergeSort(items)
#print QuickSort(items)
