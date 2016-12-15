def front_back(str):
    word = list(str)
    first_chr = word[0]
    last_chr = str[len(word)-1]
    word[0] = last_chr
    word[len(word)-1] = first_chr
    word = str(word)
    return word

print(front_back('code'))






# def front_back(str):
#     word = str
#     first_chr = word[0]
#     last_chr = str[len(word)-1]
#     last_as_first = word.replace(first_chr, last_chr)
#     # first_as_last = last_as_first.replace()
#     # new_word = last_as_first.replace(last_chr,first_chr)
#     last_as_first[len(word)-1] = first_chr
#     return new_word

# print(front_back('code'))


# def front_back(str):
#     word = str
#     first_chr = str[0]
#     last_chr = str[len(str)-1]
#     last_as_first = word.replace(first_chr, last_chr)
#     # first_as_last = last_as_first.replace(last_chr, first_chr)
#     return first_as_last

# print(front_back('code'))





# def front_back(str):
#     word = str
#     first_chr = word[0]
#     last_chr = str[len(word)-1]
#     last_as_first = word.replace(first_chr, last_chr)
#     last_as_first[len(word)-1] = first_chr
#     return last_as_first


#     # last_as_first = word.replace(first_chr, last_chr)
#     # first_as_last = word.replae

#     # first_as_last = word.replace(last_chr, first_chr)
#     return last_as_first

# print(front_back('code'))
