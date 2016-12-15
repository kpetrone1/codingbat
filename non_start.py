def non_start(a, b):
  return a.strip(a[0]) + b.strip(b[0])





print(non_start('Hello', 'There')) #→ 'ellohere'
print(non_start('java', 'code')) #→ 'avaode'
print(non_start('shotl', 'java')) #→ 'hotlava'