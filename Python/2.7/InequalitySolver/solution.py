def print_variable(name,description,value,units):
  print name," is ",description,".","The value is ",value," ",units,"."
b = 20
t = 254
f = 26
print
with open('problem.txt','r') as file: problem=file.read()
print problem
print
print_variable("b","the height of the first floor",20,"feet")
print_variable("t","a height smaller than the building's height",254,"feet")
print_variable("f","the number of the remaining floors",26,"")
print_variable("x","the average height of the remaining floors","unknown","feet")

print "b+f*x > t"

print "x > (t-b)/f"

print "x > ",(t-b)/f," ","feet"