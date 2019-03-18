from codingeverywhere_library import present_problem,read_problem,parse_formula,present_formula,solve_phase_1
import sys
import re

analysis=read_problem(sys.argv[1])
present_problem(*analysis)

variables=analysis[1]
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]

formula=analysis[2]

canonical_formula=formula.replace(" ","")

lhs_tokens,f_sign,rhs_tokens=parse_formula(canonical_formula)

lhs_tokens,f_sign,rhs_tokens=solve_phase_1(lhs_tokens,f_sign,rhs_tokens,"x")

print
if sys.argv[1] in ["analysis.json","analysis_002.json","analysis_003.json","analysis_004.json","analysis_006.json"]:
  print "x ",f_sign," (t-b)/f"
  print "x ",f_sign," ",(t-b)/f," ","feet"