def print_variable(name,description,value,units):
  print name," is ",description,".","The value is ",value," ",units,"."
def display_problem_from_file(filename):
  print
  with open(filename,'r') as file: problem=file.read()
  print problem
  print
def present_problem(filename,variables,formula):
  display_problem_from_file(filename)
  for variable in variables:print_variable(*variable)
  print formula
  print

analysis=(
  "problem.txt"
  ,(
    ("b","the height of the first floor",20,"feet")
    ,("t","a height smaller than the building's height",254,"feet")
    ,("f","the number of the remaining floors",26,"")
    ,("x","the average height of the remaining floors","unknown","feet")
  )
  ,"b+f*x > t"
)
present_problem(*analysis)

variables=analysis[1]
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]




print "x > (t-b)/f"

print "x > ",(t-b)/f," ","feet"