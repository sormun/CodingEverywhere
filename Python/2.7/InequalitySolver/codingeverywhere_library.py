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