def print_variable(name,description,value,units):
  print name," is ",description,".","The value is ",value," ",units,"."
def display_problem_from_file(filename):
  print
  with open(filename,'r') as file: problem=file.read()
  print problem
  print
B=("b","the height of the first floor",20,"feet")
T=("t","a height smaller than the building's height",254,"feet")
F=("f","the number of the remaining floors",26,"")
X=("x","the average height of the remaining floors","unknown","feet")

b = 20
t = 254
f = 26

display_problem_from_file('problem.txt')
print_variable(*B)
print_variable(*T)
print_variable(*F)
print_variable(*X)

print "b+f*x > t"

print "x > (t-b)/f"

print "x > ",(t-b)/f," ","feet"