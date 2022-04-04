# use the function blackbox(lst) that is already defined

mylist = [1, 2, 3, 4, 5]

newlist = blackbox(mylist)

if id(mylist) == id(newlist):
    print("modifies")
else:
    print("new")