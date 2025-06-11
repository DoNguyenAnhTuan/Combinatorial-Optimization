def knapsack(weights, values, max_weight):
    # Số lượng các vật phẩm
    n = len(weights)
    
    # Tạo bảng m[i][w] với kích thước (n+1) x (max_weight+1), khởi tạo các giá trị là 0
    m = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    # Điền vào bảng theo công thức
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i-1] > w:
                m[i][w] = m[i-1][w]
            else:
                m[i][w] = max(m[i-1][w], m[i-1][w - weights[i-1]] + values[i-1])
    
    # In bảng kết quả
    print("i\\w", end="\t")
    for w in range(max_weight + 1):
        print(w, end="\t")
    print()
    for i in range(n + 1):
        print(i, end="\t")
        for w in range(max_weight + 1):
            print(m[i][w], end="\t")
        print()
    
    return m

# Ví dụ về sử dụng
weights = [5, 8, 3]
values = [45, 48, 35]
max_weight = 10
# weights = [4,3,2,1]
# values = [5,4,3,2]
# max_weight = 6
m = knapsack(weights, values, max_weight)
