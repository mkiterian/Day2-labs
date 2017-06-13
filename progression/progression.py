def arith_geo(a_list):
  if len(a_list) == 0:
    return 0
  elif len(a_list) > 2:
    if is_arithmetic(a_list):
      return 'Arithmetic'
    elif is_geometric(a_list):
      return 'Geometric'
    else:
      return -1
  else:
    return -1
  
def is_arithmetic(a_list):
  diff = a_list[1] - a_list[0]
  for i in range(len(a_list)-1):
    if a_list[i+1] - a_list[i] != diff:
      return False
  
  return True

def is_geometric(a_list):
  ratio = a_list[1] / a_list[0]
  
  for i in range(len(a_list)-1):
    if abs(a_list[i+1] / a_list[i]) != abs(ratio):
      return False
      
  return True