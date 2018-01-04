# Advent of Code Day 15 - 2015

import itertools
import pandas as pd

# puzzle input
ingredients = """Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8"""

# input as dictionary
ing = {"sprinkles":[5,-1,0,0,5], 
       "peanutbutter":[-1,3,0,0,1], 
       "frosting":[0,-1,4,0,6], 
       "sugar":[-1,0,0,2,8]}

# Convert to dataframe
df = pd.DataFrame(ing)
df['parameter'] = ['capacity','durability','flavour','texture','calories']
df.set_index('parameter', inplace = True)
df = df.T

print(df)


# Check for valid combinations of teaspoons adding to 100
valids = []
for i in range(1,96):
    for j in range(i,96):
        for k in range(j,96):
            for l in range(k,96):
                if i+j+k+l==100: valids.append([i,j,k,l])
len(valids)

# check for valid combos for capacity (i.e. not negative) and calculate max
max_v = 0
for valid in valids:
    permu = list(itertools.permutations(valid))
    for each in permu:
            if sum(df['calories']*each)==500: # required for part 2
            # need to do all permutations of 'each'!
                new_sum = [max(sum(df['capacity']*each),0),
                     max(sum(df['durability']*each),0),
                     max(sum(df['flavour']*each),0),
                     max(sum(df['texture']*each),0)]

                total = new_sum[0]*new_sum[1]*new_sum[2]*new_sum[3]
                if (total > max_v):
                    max_combo = each
                    max_v = total
                    cal_count = df['calories']*each

print("\nMax value:", max_v, max_combo,'\n', cal_count)