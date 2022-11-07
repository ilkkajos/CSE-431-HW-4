
def adjustments(start, target):
    adjustment=0
    while start != target:
        b_num = bin(start)[2::]
        r_num = b_num[::-1]
        index = r_num.rfind("1")
        while (start-2**index) < target:
            index-=1
        if (start - 2 ** index) >= target:
            start = start - 2 ** index
            adjustment += 1
    return adjustment


if __name__ == '__main__':
    num_tests = int(input())
    for test_idx in range(num_tests):
        line = input().split()
        start =int(line[0])
        target = int(line[1])
        num = adjustments(start, target)
        print(num)