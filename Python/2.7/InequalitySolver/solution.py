from codingeverywhere_library import present_problem,read_problem
import sys

analysis=read_problem(sys.argv[1])
present_problem(*analysis)

variables=analysis[1]
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]

print "x > (t-b)/f"
print "x > ",(t-b)/f," ","feet"