def not_string(str):
    if len(str) >= 3 and str[:3] == "not":      #? Why 3? Why "up until 3" with "str[:3]"?
        return str
    else:
        return "not " + str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))