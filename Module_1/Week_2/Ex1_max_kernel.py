def max_kernel(num_list, k):
    result = []

    for i in range(len(num_list)):
        if i+k <= len(num_list):
            area = num_list[i:i+k]
            max_num = max(area)
            result.append(max_num)

    print(result)

max_kernel([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1], 3)

