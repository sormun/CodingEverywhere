from codingeverywhere_library import present_problem,read_problem,get_f_sign
import sys
import re

analysis=read_problem(sys.argv[1])
present_problem(*analysis)

variables=analysis[1]
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]

formula=analysis[2]

f_sign=get_f_sign(formula)

hsides=formula.split(f_sign)
lhs=hsides[0]
rhs=hsides[1]

lhs_tokens=re.findall("[\+\-]*[a-zA-Z0-9 _\*]+",lhs)
print
print "LHS : ",lhs
for lhs_token in lhs_tokens:print lhs_token
print
print "RHS : ",rhs
print

print "x ",f_sign," (t-b)/f"
print "x ",f_sign," ",(t-b)/f," ","feet"