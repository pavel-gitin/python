counter = 0
for i in range(1000,10000):
    product = 1
    for j in range(0,4):
        digit = int(str(i)[j])
        if digit > 0:
            product = product * digit
    #print(product)
    if product == 12:
        counter += 1
        
print(counter)