
fname = "inputs/2017_day19.txt"
with open(fname) as f:
        lines = f.readlines()

xy = dict()
y = 0
start = 0


# Build the grid
for l in lines:
    x = 0
    for m in l: 
            xy[x,y]=m
            if m == '|' and start == 0: start = x
            x+=1
    y += 1

letters = []

def move(x,y, dirn):
    # Function to move in same direction, or change if a '+' is encountered
    if xy[x,y]=='+':  
            if xy[(x+1,y)]  !=' ' and dirn !=[-1,0]:  dirn = [1,0]  # right     
            elif xy[(x-1,y)]!=' ' and dirn !=[1,0]:   dirn = [-1,0] # left  
            elif xy[(x,y+1)]!=' ' and dirn !=[0,-1]:  dirn = [0,1]  # down
            elif xy[(x,y-1)]!=' ' and dirn !=[0,1]:   dirn = [0,-1] # up
            else:  print("Ummmm:",x,y,xy[x,y]) # catch just in case!       
    if xy[x,y] not in ['|','+','-']:
            letters.append(xy[(x,y)])
    x = x + dirn[0]
    y = y + dirn[1]
    return x,y, dirn


# Main
x1 = start
y1 = 0
dirn1=[0,1]
print("Start", start)
steps = 0
while (x1,y1) in xy and xy[(x1,y1)]!= ' ':
    x1,y1, dirn1 = move(x1,y1,dirn1)
    steps+=1
            
print("Part A:",''.join(letters))
print("Part B:", steps)
