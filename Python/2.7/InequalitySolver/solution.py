def print_variable(name,description,value,units):
  print name," is ",description,".","The value is ",value," ",units,"."
def display_problem_from_file(filename):
  print
  with open(filename,'r') as file: problem=file.read()
  print problem
  print
variables=(
("b","the height of the first floor",20,"feet")
,("t","a height smaller than the building's height",254,"feet")
,("f","the number of the remaining floors",26,"")
,("x","the average height of the remaining floors","unknown","feet")
)

b = 20
t = 254
f = 26

display_problem_from_file('problem.txt')
for variable in variables:print_variable(*variable)

print "b+f*x > t"

print "x > (t-b)/f"

print "x > ",(t-b)/f," ","feet"