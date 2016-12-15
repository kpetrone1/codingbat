def missing_char(str, n):
  front = str[:n]   # up to, but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
  

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'


# def missing_char(str, n):
#   if n > 0 and n <= len(str):
#     list1 = list(str)
#     return list1.remove(list1[n])
#   # else:
#     # print("Ensure "n" is within range of length of "str".")
    
    
    # def missing_char(str, n):
    # if n > 0 and n <= len(str):
    #     list1 = list(str)
    #     x = list1[n]
    #     return list1.remove(x)

# print(missing_char('kitten',4))