from codingeverywhere_library import present_problem

import json

with open('analysis.json','r') as f: analysis=json.loads(f.read())

present_problem(*analysis)

variables=analysis[1]
b = variables[0][2]
t = variables[1][2]
f = variables[2][2]




print "x > (t-b)/f"

print "x > ",(t-b)/f," ","feet"