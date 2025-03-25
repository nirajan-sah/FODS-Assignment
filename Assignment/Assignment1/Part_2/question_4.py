'''
Program to find the Euclidean distance between two points.
The mathematical formula to calculate the distance between two point is ((x2 - x1)**2 + (y2 - y1)**2)**0.5
'''

#prompt user to input co-ordinate
x1 = int(input("Enter x1 coordinate: "))
y1 = int(input("Enter y1 coordinate: "))

x2 = int(input("Enter x2 coordinate: "))
y2 = int(input("Enter y2 coordinate: "))

#formula to calculate the distance
Euclidean = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#print result
print(f"The Euclidean distance between the coordinates {x1, y1} and {x2, y2} is {round(Euclidean, 5)}")