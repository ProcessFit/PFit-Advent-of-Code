
# coding: utf-8

# In[287]:


fname = "inputs/2017_day22.txt"
with open(fname) as f:
        lines = f.readlines()

# setup grid 
grid =[l.strip() for l in lines]
mid = int(len(grid)-1)/2
grid_d = dict()
for row in range(len(grid)):
    for col in range(len(grid)):
        grid_d[col-mid, -(row-mid)]=grid[row][col]

# initialise values
dirns = [(1,0),(0,-1),(-1,0),(0,1)] # right, down, left, up
d = 3 # start direction
pos = [0,0] # start positions
infected_count = 0

for counter in range(10000000):
    x,y = pos
    if grid_d[x,y]=='#': # If the current node is infected, it turns to its right.
        d = (d+1)%4   
        grid_d[(x,y)] ="f" # infected --> flagged
    elif grid_d[x,y]=='w':
        infected_count +=1
        grid_d[(x,y)]="#" # weak --> infected
    elif grid_d[x,y]=='f':
        d = (d-2)%4 # reverses
        grid_d[(x,y)]="." # flag --> clean
    elif grid_d[x,y]=='.':
        d = (d-1)%4 # turns left
        grid_d[(x,y)]="w" # clean --> weak
        
    # move in direction
    x += dirns[d][0]
    y += dirns[d][1]
    pos = [x,y]
    if (x,y) not in grid_d:
        grid_d[x,y]="."

print("infected_count:", infected_count) #2512008

