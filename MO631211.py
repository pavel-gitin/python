# 631211
# Für eine natürliche Zahl n sei P(n) das Produkt ihrer von 0 verschiedenen Ziffern.
# Beispielsweise ist also P(2023) = 2 · 2 · 3 = 12.
# Man ermittle, wie viele vierstellige Zahlen n mit der Eigenschaft P(n) = 12 existieren.

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
