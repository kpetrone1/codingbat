def cat_dog(str):
  return str.count('cat') == str.count('dog')



cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True