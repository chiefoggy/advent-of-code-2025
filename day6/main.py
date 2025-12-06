with open('input.txt') as f:
    nums = []
    operations = []
    res = 0
    for line in f:
        line = line.strip().split()
        if line[0].isdigit():
            line = [int(i) for i in line]
            nums.append(line)
        else:
            operations = line

    for i in range(len(nums[0])):
        if operations[i] == '+':
            temp = 0
            for j in range(len(nums)):
                temp += nums[j][i]
            res += temp
            
        else: 
            temp = 1
            for j in range(len(nums)):
                temp *= nums[j][i]
            res += temp
    print(res)