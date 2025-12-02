def part1():
    with open('input.txt') as f:
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
#could move more than 100 with each rotation!!
part1() #1158

def part2():
    with open('input.txt') as f:
        pos = 50
        res = 0 
        for line in f:
            line = line.strip()
            direction = line[0]
            magnitude = int(line[1:])
            for _ in range(magnitude):
                if direction == 'L':
                    pos = (pos - 1) % 100
                else:
                    pos = (pos + 1) % 100
                if pos == 0:
                    res += 1
    print(res)
#got too lazy to try to 'math it out' and just simulated the whole process
part2() #6860
