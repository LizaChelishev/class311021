# create list of numbers 0,1,2,3,4
list = []
for x in range(5):
    y = []
    for j in range(x + 1):
      y.append(j)
    list.append(y)
print(list)


