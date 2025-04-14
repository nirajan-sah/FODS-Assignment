'''
Program to see how to manipulate set
'''

set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

#Code to find union
union = set1.union(set2)
print(len(union))

#Code to find intersection
intersection = set1.intersection(set2)
print("The intersection is ", intersection)

#Code to find symmetric difference
symm = set1.symmetric_difference(set2)
print("The symmetric difference is ", symm)

#Code to add to set
set1.add(40)
print(set1)
#The set didn't change

#Code to delete from set
set2.discard(20)
print(set2)
#The set did change
