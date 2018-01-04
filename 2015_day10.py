# day 10 - see it speak it number

in_str = "1113122113"

def process(the_string):
    j = 0
    num = ''
    while j < len(in_str):
        test = in_str[j]
        count = 1
        if j != len(in_str)-1:
            while in_str[j+count]==test:
                count +=1
        num += str(count)+str(test)   
        j += count
    return num

for run in range(50):
    in_str = process(in_str)
len(in_str)