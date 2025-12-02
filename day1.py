with open('day1input.txt') as f:
    pos = 50 #starts at 50
    res = 0
    for line in f:
        line = line.strip()
        direction = line[0]
        magnitude = int(line[1:])
        if direction == 'L': #turn left
            pos = (pos - magnitude) % 100
            
        else: #turn right
            pos = (pos + magnitude) % 100
        
        if pos == 0:
            res += 1
    print(res)