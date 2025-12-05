#naive brute force approach for p1, could be optimised with sorting the ranges then using binary search to find 
def part1():
    with open('input.txt') as f:
        ranges, nums = f.read().split('\n\n')
        ranges = [list(map(int, r.split('-'))) for r in ranges.splitlines()]
        nums = list(map(int, nums.splitlines()))
        res = 0
        for num in nums:
            for low, high in ranges:
                if low <= num <= high:
                    res +=1 
                    break
        print(res) 

part1() #511

def part2():
    with open('input.txt') as f:
        ranges, nums = f.read().split('\n\n') #can ignore the nums part
        count = 0
        ranges = sorted([list(map(int, r.split('-'))) for r in ranges.splitlines()])
        curr_min,curr_max = ranges[0]

        for i in range(1, len(ranges)):
            start, end = ranges[i]
            if start <= curr_max: #overlap
                curr_max = max(curr_max, end)
            else: #no overlap, normal case
                count += (curr_max - curr_min + 1)
                curr_min, curr_max = start, end
        count += (curr_max - curr_min + 1) #add last range
        print(count) 
part2() #350939902751909