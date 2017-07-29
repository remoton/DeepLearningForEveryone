# python slicing examples

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index       0,  1,  2,  3,  4,  5,  6,  7,  8,  9
# - index   -10,-9, -8, -7, -6, -5, -4, -3, -2, -1 

print("my_list is ", my_list)

# list slicing syntax
#list[start:end:step]
# start index -> include
# end index -> exclude

#
# ex1 : if we want list of [0,1,2,3,4,5] then my_list[0:6]
print("my_list[0:6] is ", my_list[0:6])

#
# ex2 : if we want list of [3,4,5,6,7] then my_list[3:8]
print("my_list[3:8] is ", my_list[3:8])

# negative index
# ex3 : we can mix both positive and negative indexies 
# if we want list of [1,2,3,4,5,6,7] then my_list[1:-2]
print("my_list[1:-2] is ", my_list[1:-2])

# include last element
# ex4 : if we want list of [1,2,3,4,5,6,7,8,9] which includes last element then the end index let empty so my_list[1:]
print("my_list[1:] is ", my_list[1:])

# include first element
# ex5: if we want list of [0,1,2,3,4,5] which includes first element then the start index let zero or empty so my_list[0:6]
# or my_list[:6]
print("my_list[0:6] is ", my_list[0:6])
print("my_list[:6] is ", my_list[:6])

# all elemssents
# ex6 : if we want list of [0,1,2,3,4,5,6,7,8,9] which includes all element then the start and end index let empty so my_list[:]
print("my_list[:] is ", my_list[:])

# step
# if step is 2, then every second elements included
# ex7 : if we want list of [2,4,6,8] which includes every second element from 2 to last then mylist[2: :2] or my_list[2:9:2]
print("----------step-----------")
print("my_list[2::2] is ", my_list[2::2])
print("my_list[2:9:2] is ", my_list[2:9:2])

# negative step -> reverse order
# if step is -2, then elements orders are reversed 
# ex8 : if we want list of [8,6,4,2] which includes every second element from 8 to first reversely then mylist[-2:1:-2] or my_list[8:1:-2]
print("my_list[-2:1:-2] is ", my_list[-2:1:-2])
print("my_list[8:1:-2] is ", my_list[8:1:-2])

# all reverse order
# if step is -1, then all elements orders are reversed
# ex9 : if we want list of [9,8,7,6,5,4,3,2,1,0] which includes reverse order of all elements then mylist[::-1]
print("my_list[::-1] is ", my_list[::-1])





















# python slicing examples

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index       0,  1,  2,  3,  4,  5,  6,  7,  8,  9
# - index   -10,-9, -8, -7, -6, -5, -4, -3, -2, -1 

print("my_list is ", my_list)

# list slicing syntax
#list[start:end:step]
# start index -> include
# end index -> exclude

#
# ex1 : if we want list of [0,1,2,3,4,5] then my_list[0:6]
print("my_list[0:6] is ", my_list[0:6])

#
# ex2 : if we want list of [3,4,5,6,7] then my_list[3:8]
print("my_list[3:8] is ", my_list[3:8])

# negative index
# ex3 : we can mix both positive and negative indexies 
# if we want list of [1,2,3,4,5,6,7] then my_list[1:-2]
print("my_list[1:-2] is ", my_list[1:-2])

# include last element
# ex4 : if we want list of [1,2,3,4,5,6,7,8,9] which includes last element then the end index let empty so my_list[1:]
print("my_list[1:] is ", my_list[1:])

# include first element
# ex5: if we want list of [0,1,2,3,4,5] which includes first element then the start index let zero or empty so my_list[0:6]
# or my_list[:6]
print("my_list[0:6] is ", my_list[0:6])
print("my_list[:6] is ", my_list[:6])

# all elemssents
# ex6 : if we want list of [0,1,2,3,4,5,6,7,8,9] which includes all element then the start and end index let empty so my_list[:]
print("my_list[:] is ", my_list[:])

# step
# if step is 2, then every second elements included
# ex7 : if we want list of [2,4,6,8] which includes every second element from 2 to last then mylist[2: :2] or my_list[2:9:2]
print("----------step-----------")
print("my_list[2::2] is ", my_list[2::2])
print("my_list[2:9:2] is ", my_list[2:9:2])

# negative step -> reverse order
# if step is -2, then elements orders are reversed 
# ex8 : if we want list of [8,6,4,2] which includes every second element from 8 to first reversely then mylist[-2:1:-2] or my_list[8:1:-2]
print("my_list[-2:1:-2] is ", my_list[-2:1:-2])
print("my_list[8:1:-2] is ", my_list[8:1:-2])

# all reverse order
# if step is -1, then all elements orders are reversed
# ex9 : if we want list of [9,8,7,6,5,4,3,2,1,0] which includes reverse order of all elements then mylist[::-1]
print("my_list[::-1] is ", my_list[::-1])





















