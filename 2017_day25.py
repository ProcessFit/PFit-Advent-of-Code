
# coding: utf-8

# In[1]:


# Advent of code Day 25

# Rules
inst = dict() 
inst['a'] = [[1,1,'b'],[0,-1,'b']]
inst['b'] = [[0,1,'c'],[1,-1,'b']]
inst['c'] = [[1,1,'d'],[0,-1,'a']]
inst['d'] = [[1,-1,'e'],[1,-1,'f']]
inst['e'] = [[1,-1,'a'],[0,-1,'d']]   
inst['f'] = [[1,1,'a'],[1,-1,'e']]

# Initial Values
state = 'a'
pos = 0
ticker_tape = dict()
ticker_tape[0]=0

def next_step(the_pos, the_state):
    pp = ticker_tape[the_pos]
    new_pos = the_pos + inst[the_state][pp][1]
    new_state = inst[the_state][pp][2]
    ticker_tape[the_pos] = inst[the_state][pp][0]
    if new_pos not in ticker_tape: ticker_tape[new_pos]=0
    return(new_pos, new_state)

steps = 1
while steps < 12586542:
    pos, state = next_step(pos, state) 
    steps+=1
sum([ticker_tape[i] for i in ticker_tape if ticker_tape[i]==1])    

