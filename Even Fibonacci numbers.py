F0 = 0
F1 = 1
total_sum = 0
rge =4000000
F2 =0


while F2 <= rge:
    F2 = F0+F1
    F0 = F1
    F1 = F2
    if (F2%2 == 0 and F2 <= rge):
        total_sum = total_sum + F2

print(f'total sum of even fibonacci numbers with values not exceeding {rge} equals {total_sum}')