def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-len(b):] == b or b[-len(a):] == a




print(end_other('Hiabc', 'abc')) #→ True
print(end_other('AbC', 'HiaBc')) #→ True
print(end_other('abc', 'abXabc')) #→ True