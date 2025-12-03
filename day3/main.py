def part1():
    with open('input.txt') as f:
        res = 0
        for line in f:
            curr_max = 0
            line = line.strip()
            #loop through every possible combination
            for i in range(len(line)):
                for j in range(i+1, len(line)):
                    curr_num = 10*int(line[i]) + int(line[j])
                    curr_max = max(curr_max, curr_num)
            res += curr_max
        print(res)
part1() #17095

def part2():
    with open('input.txt') as f:
        res = 0
        for line in f:
            line = line.strip()
            remove = len(line) - 12

            stack = []
            for char in line:
                while stack and remove > 0 and stack[-1] < char:
                    stack.pop()
                    remove -= 1
                stack.append(char)
            curr_max = ''.join(stack[:12])
            res += int(curr_max)
        print(res)
part2() #168794698570517

