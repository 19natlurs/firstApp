import price

print('use the following product codes')
print('mlk--> MILK, brd --> BREAD, sug --> SUGAR, mlo --> MILO, lpt --> LIPTON, bsc --> BISCUIT, swt --> SWEET, gum --> GUM, cks --> COOKIES, drk --> DRINK')
item = input ('Enter the you wish to buy')
qty = input ('Enter the quantity')

if item=='mlk':
    prices=price.MILK
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='brd':
    prices=price.BREAD
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='sug':
    prices=price.SUGAR
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='mlo':
    prices=price.MILO
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='lpt':
    prices=price.LIPTON
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='bsc':
    prices=price.BISCUIT
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='swt':
    prices=price.SWEET
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='gum':
    prices=price.GUM
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='cks':
    prices=price.COOKIES
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)
    
if item=='drk':
    prices=price.DRINK
    total=int(qty)*prices
    print('The Total price for total number of bread is :', total)