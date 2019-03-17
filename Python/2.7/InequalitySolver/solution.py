from codingeverywhere_library import present_problem,read_problem,parse_formula,present_formula
import sys
import re

analysis=read_problem(sys.argv[1])
present_problem(*analysis)

variables=analysis[1]
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]

formula=analysis[2]

lhs_tokens,f_sign,rhs_tokens=parse_formula(formula)
print "STEP 0 :"
present_formula(lhs_tokens,f_sign,rhs_tokens)



print "x ",f_sign," (t-b)/f"
print "x ",f_sign," ",(t-b)/f," ","feet"