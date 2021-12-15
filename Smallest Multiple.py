

starting_number = 20
number = starting_number
i = 2
found = False
while found is False:
    while number%i == 0:   
        i = i+1
        if i == (starting_number+1):
            print(number)
            found = True
            break
    number = number + starting_number
    i = 2 
