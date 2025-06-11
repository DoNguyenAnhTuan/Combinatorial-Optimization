from itertools import combinations

# Danh sách các item (weight, value)

items = [
    ("X1", 5, 10),
    ("X2", 4, 40),
    ("X3", 6, 30),
    ("X4", 3, 50)
]
# items = [
#     ("X1", 5, 45),
#     ("X2", 8, 48),
#     ("X3", 3, 35)
# ]
# Trọng lượng tối đa của balo
K = 10

# Hàm liệt kê và kiểm tra tổ hợp
def knapsack(items, K):
    n = len(items)
    max_value = 0
    optimal_combination = []
    print(f"{'Tổ hợp':<20} {'Trọng lượng (Size)':<20} {'Giá trị (Value)':<20} {'Infeasible'}")

    # Kiểm tra tất cả các tổ hợp khả thi
    for r in range(1, n + 1):
        for combination in combinations(items, r):
            weight = sum(item[1] for item in combination)
            value = sum(item[2] for item in combination)
            item_names = [item[0] for item in combination]

            # Kiểm tra nếu tổng trọng lượng <= K (feasible)
            if weight <= K:
                infeasible = ""
                # Cập nhật tổ hợp tối ưu
                if value > max_value:
                    max_value = value
                    optimal_combination = item_names
            else:
                infeasible = "Yes"

            # In kết quả
            print(f"{item_names!s:<20} {weight:<20} {value:<20} {infeasible}")

    return max_value, optimal_combination

# Chạy chương trình
max_value, optimal_combination = knapsack(items, K)

# Kết quả cuối cùng
print("\nKết quả cuối cùng:")
print(f"Giá trị tối đa: {max_value}")
print(f"Tổ hợp tối ưu: {', '.join(optimal_combination)}")



# x1 lấy hoặc k lấy item X1
# x2 lấy hoặc k lấy item X2
# x3 lấy hoặc k lấy item X3


# max 45x1+48x2+35x3
# 5x1+8x2+3x3<=10
# x1,x2,x3 thuộc {0,1}