from codingeverywhere_library import present_problem

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