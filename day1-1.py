with open('day1_src.txt', 'r') as file:
    fuel_sum = 0
    for line in file:
        fuel_sum += int(int(line)/3)-2
print(fuel_sum)