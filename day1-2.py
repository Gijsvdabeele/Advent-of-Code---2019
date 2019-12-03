def fuel_addition(m):
    added_fuel = 0
    while 1>0:
        m = int(int(m)/3)-2
        if m<=0:
            break
        else:
            added_fuel += m
    return added_fuel

with open('day1_src.txt', 'r') as file:
    fuel_sum = 0
    for line in file:
        fuel_sum += (int(int(line)/3)-2)+fuel_addition((int(int(line)/3)-2))
print(fuel_sum)
