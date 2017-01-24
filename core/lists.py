import numpy as np

# Simple list
groceries_list = ['Juice', 'Tomatoes', 'Onions']
print 'First Item:', groceries_list[0]

groceries_list[0] = 'Green Juice'
print 'First Item:', groceries_list[0]

# print subset of a list
print groceries_list[1:3]

# join items in list by comma
print 'To-do List:', ', '.join(groceries_list)

# save a list of lists
other_chores = ['Pay bills', 'Wash car']

to_do_list = [ other_chores, groceries_list ]
print to_do_list

# what's my second item in my second list?
print 'my second item in my second list=', to_do_list[1][1]

# append items to groceries list
groceries_list.append('Potatoes')
print to_do_list

# insert item at index
groceries_list.insert(1, 'Apples')
print to_do_list

# remove item from list
groceries_list.remove('Apples')
print to_do_list

# sort items
groceries_list.sort()
# print to_do_list

# reverse list
groceries_list.reverse()
# print to_do_list

del groceries_list[3]
print to_do_list
