from codingeverywhere_library import present_problem,read_problem
import sys

analysis=read_problem(sys.argv[1])
present_problem(*analysis)

variables=analysis[1]
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]

formula=analysis[2]

potential_f_signs=[">","<","=",">=","<="]

for potential_f_sign in potential_f_signs:
  if potential_f_sign in formula:f_sign=potential_f_sign

print "x ",f_sign," (t-b)/f"
print "x ",f_sign," ",(t-b)/f," ","feet"