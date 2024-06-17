def lavenshtein_distance(source, target):
    # Tạo ma trận lưu trữ
    len_source = len(source)
    len_target = len(target)    

    D = [[0] * (len_target + 1) for _ in range(len_source + 1)]

    # Tạo hàng và cột đầu tiên 
    for i in range(len_source + 1):
        D[i][0] = i

    for j in range(len_target + 1):
        D[0][j] = j

    # Tính toán các ô trong ma trận
    del_cost = 0
    ins_cost = 0
    sub_cost = 0

    for i in range(1, len_source + 1):
        for j in range(1, len_target + 1):
            if source[i - 1] == target[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                del_cost = D[i - 1][j] # Xét ô bên trên
                ins_cost = D[i][j - 1] # Xét ô bên trái
                sub_cost = D[i - 1][j - 1] # Xét ô chéo

                D[i][j] = min(del_cost, ins_cost, sub_cost) + 1

    return D[len_source][len_target]

print(lavenshtein_distance('hola', 'hello'))
