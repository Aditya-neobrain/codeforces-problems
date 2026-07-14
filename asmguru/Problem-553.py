# Problem 553: Sultan's Pearls
# Problem url: https://codeforces.com/problemsets/acmsguru/problem/99999/553

import random

total_pearl = random.randint(2,20)
hanging_pearl = random.randint(1,total_pearl-1)
friction_coefficient = random.randint(1,10)
mass_price_list = []

for i in range(total_pearl):
    mass = random.randint(1,10)
    price = random.randint(1,10)
    mass_price_list.append((mass, price))

print(total_pearl, hanging_pearl, friction_coefficient)
for mass, price in mass_price_list:
    print(mass, price)


def steal(n, m, k, pearls):
    table_pearls = pearls[:n-m]
    hanging_pearls = pearls[n-m:]
    
    table_mass = k * sum(w for w, c in table_pearls)
    hanging_mass = sum(w for w, c in hanging_pearls)

    steal_sequence = []
    stolen_pearls = 0
    stolen_value = 0

    while table_mass > 0 and hanging_mass > 0:
        if hanging_mass > table_mass:
            stolen_pearl = hanging_pearls.pop()
            steal_sequence.append('H')
            stolen_pearls += 1
            stolen_value += stolen_pearl[1]
            hanging_mass -= stolen_pearl[0]
            if hanging_pearls:
                hanging_mass += hanging_pearls[-1][0] 
        else:
 
            stolen_pearl = table_pearls.pop(0)
            steal_sequence.append('T')
            stolen_pearls += 1
            stolen_value += stolen_pearl[1]
            table_mass -= k * stolen_pearl[0]

    print(stolen_pearls, stolen_value)
    print(''.join(steal_sequence))

steal(total_pearl, hanging_pearl, friction_coefficient, mass_price_list)


      

