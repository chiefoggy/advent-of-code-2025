def part1():
    with open('input.txt') as f:
        line = f.readline().strip()
        lines = line.split(',')
        res = 0
        for id in lines:
            firstID, lastID = id.split('-')
            for i in range(int(firstID), int(lastID)+1): #lastID inclusive in search range
                check_str = str(i)
                #this number has to be at least 2 digits (ie 10) for there to be duplicates
                if len(check_str) > 1:
                    #length of number has to be divisible by 2
                    if len(check_str) % 2 == 0:
                        if check_str[:len(check_str)//2] == check_str[len(check_str)//2:]: #check if first half = second half
                            res += i
        print(res)

part1() #19386344315

def part2():
    with open('input.txt') as f:
        line = f.readline().strip()
        lines = line.split(',')
        res = 0
        for id in lines:
            firstID, lastID = id.split('-')
            for i in range(int(firstID), int(lastID)+1): #lastID inclusive in search range
                check_str = str(i)
                n = len(check_str)
                for l in range(1, n // 2 + 1):
                    if n % l == 0:
                        unit = check_str[:l]
                        if unit * (n // l) == check_str:
                            res += i
                            break
        print(res)

part2() #34421651192



