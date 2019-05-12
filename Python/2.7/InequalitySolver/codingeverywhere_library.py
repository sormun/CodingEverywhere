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

def printable_token(position_in_list,token):
  if position_in_list==0 and token[0]=="+":return token[1:]
  else:return token

def present_formula(lhs_tokens,f_sign,rhs_tokens):
  for i in range(len(lhs_tokens)):
    print printable_token(i,lhs_tokens[i]),
  print f_sign,
  for i in range(len(rhs_tokens)):
    print printable_token(i,rhs_tokens[i]),
  print

def clean_zero_tokens(hs_tokens):
  if len(hs_tokens) > 1:
    if hs_tokens[0] in ["0","+0","-0"]:
      hs_tokens.pop(0)
  return hs_tokens

def solve_phase_1(lhs_tokens,f_sign,rhs_tokens,unknown):
  print
  print "Phase I:"
  present_formula(lhs_tokens,f_sign,rhs_tokens)
  
  for i in range(len(lhs_tokens)):
    token=lhs_tokens.pop(0)
    if token in ["0","-0","+0"]:continue
    if unknown in token:
      if token.startswith("+") or token.startswith("-"):
        lhs_tokens.append(token)
      else:
        lhs_tokens.append("+"+token)
    else:
      if token.startswith("-"):neg_token="+"+token[1:]
      elif token.startswith("+"):neg_token="-"+token[1:]
      else: neg_token="-"+token
      rhs_tokens.append(neg_token)
      rhs_tokens=clean_zero_tokens(rhs_tokens)
      if len(lhs_tokens)==0:
        lhs_tokens.append("0");
      print
      print "Adding (",neg_token,") on both sides ..."
      present_formula(lhs_tokens,f_sign,rhs_tokens)
  if len(lhs_tokens)==0:
    lhs_tokens.append("0");


  for i in range(len(rhs_tokens)):
    token=rhs_tokens.pop(0)
    if token in ["0","-0","+0"]:continue
    if unknown not in token:
      if token.startswith("+") or token.startswith("-"):
        rhs_tokens.append(token)
      else:
        rhs_tokens.append("+"+token)
    else:
      if token.startswith("-"):neg_token="+"+token[1:]
      elif token.startswith("+"):neg_token="-"+token[1:]
      else: neg_token="-"+token
      lhs_tokens.append(neg_token)
      lhs_tokens=clean_zero_tokens(lhs_tokens)
      if len(rhs_tokens)==0:
        rhs_tokens.append("0");
      print
      print "Adding (",neg_token,") on both sides ..."
      present_formula(lhs_tokens,f_sign,rhs_tokens)
  if len(rhs_tokens)==0:
    rhs_tokens.append("0");
  return (lhs_tokens,f_sign,rhs_tokens)