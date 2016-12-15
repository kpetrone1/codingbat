def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    """
  return "Hello {}!" .format(name)


print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('X'))
