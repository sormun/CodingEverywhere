import json
import re

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
def read_problem(json_filename):
  with open(json_filename,'r') as f: analysis=json.loads(f.read())
  return analysis

def get_f_sign(formula):
  potential_f_signs=[">","<","=",">=","<="]
  for potential_f_sign in potential_f_signs:
    if potential_f_sign in formula:f_sign=potential_f_sign
  return f_sign

def parse_formula(formula):
  f_sign=get_f_sign(formula)

  hsides=formula.split(f_sign)
  lhs=hsides[0]
  rhs=hsides[1]

  lhs_tokens=re.findall("[\+\-]*[a-zA-Z0-9 _\*]+",lhs)
  rhs_tokens=re.findall("[\+\-]*[a-zA-Z0-9 _\*]+",rhs)

  return (lhs_tokens,f_sign,rhs_tokens)