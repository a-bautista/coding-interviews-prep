'''
    def solve(nums, k):
        a = 0
        avg_vals = []
        length = len(nums)
        for i in range(0, length - k + 1):
            c_val = 0
            for j in range(i, k + a):
                c_val += nums[j]
            avg_vals.append([c_val/k])
            a += 1
        return avg_vals

        Good but how can you improve it? 

    def main():
        nums = [1, 2, 3, 4, 5]
        k = 3
        res = solve(nums, k)
        print(res)

    main()

'''

def solve_not_efficient(nums, k):
    avg_list = []
    for i in range(0, len(nums)-k+1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += nums[j]
        avg_list.append(window_sum/k)
    return avg_list

def solve_efficient(nums, k):
    avg_list = []
    window_start = 0
    window_sum = 0

    for window_end in range(len(nums)):
        window_sum += window_end
        if window_end>=k:
            avg_list.append(window_sum/k)
            window_sum -= nums[window_start]
            window_start +=1
    return avg_list

def main():
    nums = [1, 2, 3, 4, 5]
    k = 3
    res1 = solve_not_efficient(nums, k)
    res2 = solve_efficient(nums, k)
    print(res1)
    print(res2)

main()