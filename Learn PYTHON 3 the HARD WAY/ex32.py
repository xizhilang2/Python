theCount = {1, 2, 3, 4, 5}
fruits = {'apples', 'oranges', 'pears', 'apricots'}
change = {1, 'pennies', 2, 'dimes', 3, 'quarters'}

# this first kind of for-loop goes through a list
for number in theCount:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
# elements = range(0, 6)
ele = range(1, 4)
elements = [ele, [11, 22, 33]]

# then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print(f"Adding {i} to the list.")
#     # append is a function hat lists understand
#     elements.append(i)

# now wo can print them out too
for i in ele:
    print(f"ele was: {i}")
for i in elements:
    print(f"Element was: {i}")
