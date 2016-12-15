def pos_neg(a, b, negative):
  # if a<0 and b>0 or a>0 and b<0:
    
  
  # if a or b < 0:
  #   return True

  
  if negative == True:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if a > 0:
      if b < 0:
        return True
      else:
        return False
    else:
        if b > 0:
          return True
        else:
          return False
  
  
  
  
# if a > 0:
#   if b < 0:
#     return True
#   else:
#     return False
# else:
#   if b > 0:
#     return True
#   else:
#     return False