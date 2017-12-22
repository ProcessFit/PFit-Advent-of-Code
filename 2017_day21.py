
# coding: utf-8

# In[1]:


import numpy as np

fname = "inputs/2017_day21.txt"
with open(fname) as f:
        lines = f.readlines()

inputs = [l.split(" =>")[0] for l in lines]
outputs = [l.split(" => ")[1].replace('\n','') for l in lines]


def build_variations(in_str):
    z = int(len(in_str)**0.5)
    variations=[]
    n = np.array(list(in_str)).reshape(z,z)
    for k in range(z):
        for r in range(4):
            n = np.rot90(n)
            variations.append(''.join(n.flatten()))
        n = np.fliplr(n)
    return variations

output_d = dict()
for i in range(len(inputs)):
    in_list = build_variations(inputs[i].replace('/',''))
    for j in in_list:
        output_d[j] = outputs[i].replace('/','')

def cut_up(str_in):
    z = 2 if len(str_in)%2==0 else 3
    z_size = int(len(str_in)**0.5)
    blocks = int(z_size//z)
    
    # cut to smaller blocks 
    y1 = np.array(list(str_in)).reshape(blocks, z, -1, z).swapaxes(1,2).reshape(-1, z, z)
    
    # read dictionary for transform
    y2 = ''.join([output_d[''.join(yy.flatten())] for yy in y1])
    y3 = np.array(list(y2)).reshape(blocks**2, z+1,z+1)

    # stitch the blocks together and return the flattened string representing matrix
    rows = []
    for j in range(blocks):
        rows.append(np.concatenate(y3[j*blocks:(j+1)*blocks,:,:], axis=1))
    y4 = np.concatenate(rows)
    return ''.join(y4.flatten())
    
# Main Program
start_grid = '.#./..#/###'
grid = start_grid.replace('/','')
counter = 0
while counter < 18:
    grid = cut_up(grid)
    counter+=1   
    print(counter, grid.count("#"))
    

