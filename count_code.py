# CODE from: http://stackoverflow.com/questions/21300450/strategies-for-searching-through-strings-in-python

def count_code(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'co' and str[i+3:i+4] == 'e':
      count += 1
  return count




count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2