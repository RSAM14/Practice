number_to_factorise = 600851475143
factor = 2

prime_number = number_to_factorise

"""
list_of_factors =[]
while factor < number_to_factorise:
     if number_to_factorise%factor == 0:
        list_of_factors.append(factor)
    factor = factor + 1
factor = 2
print(f'list of factors {list_of_factors}')
"""
while factor*factor <= prime_number:
    while prime_number%factor == 0 :
        if prime_number/factor != 1:
            prime_number = prime_number/factor
        else:
            break
    factor = factor + 1
print(f'highest prime factor {prime_number}')

