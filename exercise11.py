_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
o_prices = []
#for x in _prices:
#    if x > 0:
#        o_prices.append(x)
#    else:
#        o_prices.append(0)
#print(o_prices)
print([x if x > 0 else 0 for x in _prices])