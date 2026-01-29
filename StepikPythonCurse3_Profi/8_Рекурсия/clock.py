def clock(d=1, width=16, spaces=0):
    line = ' '*spaces+str(d)*width
    print(line)
    if d < 4:
        clock(d+1, width-4, spaces+2)
        print(line)

clock()