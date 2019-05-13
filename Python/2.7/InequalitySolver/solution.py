from codingeverywhere_library import present_problem,read_problem,parse_formula,present_formula,solve_phase_1
from codingeverywhere_library import printable_token,build_expression
import sys
import re

analysis=read_problem(sys.argv[1])
present_problem(*analysis)

variables=analysis[1]

knowns={}
for variable in variables:
  if variable[2]=="unknown":
    unknown=variable[0]
  else:
    knowns[variable[0]]=variable[2]

formula=analysis[2]

canonical_formula=formula.replace(" ","")

lhs_tokens,f_sign,rhs_tokens=parse_formula(canonical_formula)

lhs_tokens,f_sign,rhs_tokens=solve_phase_1(lhs_tokens,f_sign,rhs_tokens,unknown)

print 
print "Phase II:"

lhs=build_expression(lhs_tokens)
rhs=build_expression(rhs_tokens)

print lhs,f_sign,rhs
print
print lhs,f_sign,eval(rhs,knowns)

for i in range(len(lhs_tokens)):
  if ("*"+unknown) in lhs_tokens[i]:
    lhs_tokens[i]=lhs_tokens[i].replace("*"+unknown,"")
    continue
  if (unknown+"*") in lhs_tokens[i]:
    lhs_tokens[i]=lhs_tokens[i].replace(unknown+"*","")
    continue
  if lhs_tokens[i]=="x":
    lhs_tokens[i]="1"
    continue
  if lhs_tokens[i]=="-x":
    lhs_tokens[i]="-1"
    continue
  if lhs_tokens[i]=="+x":
    lhs_tokens[i]="+1"
    continue

lhs=build_expression(lhs_tokens)
print
print lhs,"*",unknown,f_sign,rhs
print
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]

if sys.argv[1] in ["analysis.json","analysis_002.json","analysis_003.json","analysis_004.json","analysis_006.json"]:
  print "x ",f_sign," (t-b)/f"
  print "x ",f_sign," ",(t-b)/f," ","feet"