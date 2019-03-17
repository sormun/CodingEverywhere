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

canonical_formula=formula.replace(" ","")

lhs_tokens,f_sign,rhs_tokens=parse_formula(canonical_formula)
print "STEP 0 :"
present_formula(lhs_tokens,f_sign,rhs_tokens)

for i in range(len(lhs_tokens)):
  token=lhs_tokens.pop(0)
  if "x" in token:
    lhs_tokens.append(token)
  else:
    if token.startswith("-"):neg_token="+"+token[1:]
    elif token.startswith("+"):neg_token="-"+token[1:]
    else: neg_token="-"+token
    rhs_tokens.append(neg_token)
    present_formula(lhs_tokens,f_sign,rhs_tokens)
print

print "x ",f_sign," (t-b)/f"
print "x ",f_sign," ",(t-b)/f," ","feet"