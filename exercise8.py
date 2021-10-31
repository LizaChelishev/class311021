string = 'i wake up at 6:00 am'
#print([dig for dig in string if dig.isdigit()])
#print([alpha for alpha in string if alpha.isalpha()])
only_digit= []
only_letters = []
for x in string:
    if x.isdigit():
        only_digit.append(x)
    elif x.isalpha():
        only_letters.append(x)
print(only_letters)
print(only_digit)



