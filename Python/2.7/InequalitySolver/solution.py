b = 20
t = 254
f = 26
print
with open('problem.txt','r') as file: problem=file.read()
print problem
print
print "b is the height of the first floor.","The value is ",b," ","feet","."
print "t is a height smaller than the building's height.","The value is ",t," ","feet","."
print "f is the number of remaining floors.","The value is ",f," ","","."
print "x is the average height of the remaining floors"

print "b+f*x > t"

print "x > (t-b)/f"

print "x > ",(t-b)/f," ","feet"