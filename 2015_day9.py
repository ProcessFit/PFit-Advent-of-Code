import itertools
import re

fname = "inputs/2015_day9.txt"
with open(fname) as f:
        lines = f.readlines()
        
# split lines and extract data
locns = [re.findall(r'(.+?)\sto\s(.+?)\s.+?(\d+)', l)[0] for l in lines]
loc = set([l[0] for l in locns]+[l[1] for l in locns])

# create dictionary for distances (in both directions)
distances = dict()
for i in range(len(locns)):
    lc = locns[i]
    distances[lc[0:2]]=lc[2]
    distances[lc[0:2][::-1]]=lc[2]

# use itertools to create all permutations of location
perms = list(itertools.permutations(loc_copy, 8))
min_dist, max_dist = 999999, 0

# determine route distance for each permutation
for p in perms:
    p_dist = 0
    for i in range(len(p)-1): p_dist += int(distances[p[i:i+2]])
    if p_dist < min_dist: 
        min_dist, the_combo = p_dist, p
    elif p_dist > max_dist: 
        max_dist, the_combo_max = p_dist, p
        
        
print(min_dist, the_combo)
print(max_dist, the_combo_max)
