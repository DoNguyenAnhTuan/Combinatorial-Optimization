import numpy as np


# cost_matrix = np.array([
#     [np.nan, 4, 9, 5],
#     [6, np.nan, 4, 8],
#     [9, 4, np.nan, 9],
#     [5, 8, 9, np.nan]
# ])

cost_matrix = np.array([
    [np.nan, 1, 0, 1],
    [1, np.nan, 0, 1],
    [2, 1,2, np.nan],
    [0, 0, np.nan,4]
])
# Bước 1: Tìm giá trị nhỏ nhất trong mỗi hàng
min_values = np.nanmin(cost_matrix, axis=1)

# Bước 2: Tạo ma trận RM
RM = []

for i in range(cost_matrix.shape[0]):
    row = []
    for j in range(cost_matrix.shape[1]):
        if not np.isnan(cost_matrix[i, j]):
            row.append(int(cost_matrix[i, j] - min_values[i]))  # Trừ giá trị nhỏ nhất của hàng
        else:
            row.append('×')  # Giữ lại ký tự '×' cho giá trị không hợp lệ
    row.append(int(min_values[i]))  # Thêm giá trị nhỏ nhất vào cuối hàng
    RM.append(row)

# In ma trận RM
print("Ma trận RM:")
print("     A   B   C   D    RM")
row_labels = ['A', 'B', 'C', 'D']
for i in range(len(RM)):
    print(f"{row_labels[i]}  {RM[i]}")

# Tính tổng của các giá trị nhỏ nhất
total_sum_RM = int(sum(min_values))
print(f"∑ = {' ' * 20}{total_sum_RM}\n")

# Bước 3: Tạo ma trận CM từ ma trận RM
RM_numeric = np.array([[val if isinstance(val, (int, float)) else np.nan for val in row[:-1]] for row in RM])

# Ma trận CM: Tìm giá trị nhỏ nhất của mỗi cột trong ma trận RM_numeric
CM = []
for j in range(RM_numeric.shape[1]):
    col_min = np.nanmin(RM_numeric[:, j])  # Giá trị nhỏ nhất của mỗi cột
    CM.append(int(col_min))

# Bước 4: Trừ các cột theo giá trị của CM
adjusted_RM = RM_numeric.copy()

for j in range(len(CM)):
    if CM[j] != 0:  # Nếu CM không bằng 0 thì trừ cột tương ứng
        adjusted_RM[:, j] -= CM[j]

# In ma trận CM đã điều chỉnh
print("Ma trận CM:")
print("     A   B   C   D   ∑")
for i in range(adjusted_RM.shape[0]):
    print(f"{row_labels[i]}   ", end="")
    for j in range(adjusted_RM.shape[1]):
        if np.isnan(adjusted_RM[i, j]):
            print("×   ", end="")
        else:
            print(f"{int(adjusted_RM[i, j])}   ", end="")
    print()

# In hàng CM
total_sum_CM = sum(CM)
print(f"CM   {CM[0]}   {CM[1]}   {CM[2]}   {CM[3]}   {total_sum_CM}")

# Bước 5: Tính giá trị LB
LB_initial = 0
LB_final = LB_initial + total_sum_RM + total_sum_CM

# In giá trị LB
print(f"\nLB = LB + ∑RM + ∑CM = {LB_initial} + {total_sum_RM} + {total_sum_CM} = {LB_final}")

# Bước 6: Tính toán ma trận S2
S2_matrix = []

for i in range(adjusted_RM.shape[0]):
    row = []
    for j in range(adjusted_RM.shape[1]):
        if adjusted_RM[i, j] == 0:
            # Tìm giá trị nhỏ nhất của hàng (không tính chính nó)
            row_min = np.nanmin(np.delete(adjusted_RM[i, :], j))
            # Tìm giá trị nhỏ nhất của cột (không tính chính nó)
            col_min = np.nanmin(np.delete(adjusted_RM[:, j], i))
            # Tổng giá trị nhỏ nhất của hàng và cột
            value = int(row_min + col_min)
            row.append(f"0({value})")
        elif np.isnan(adjusted_RM[i, j]):
            row.append('×')  # Giữ nguyên giá trị '×'
        else:
            row.append(f"{int(adjusted_RM[i, j])}")
    S2_matrix.append(row)

# In kết quả bước S2
print("\nKết quả bước S2:")
print("     A      B      C      D")
for i in range(len(S2_matrix)):
    print(f"{row_labels[i]}  {S2_matrix[i]}")

# Bước 7: Tìm Maximum Penalty (MP)
max_penalty = -1
max_penalty_positions = []

for i in range(len(S2_matrix)):
    for j in range(len(S2_matrix[i])):
        if isinstance(S2_matrix[i][j], str) and "0(" in S2_matrix[i][j]:
            penalty_value = int(S2_matrix[i][j][2:-1])  # Lấy giá trị trong ngoặc
            if penalty_value > max_penalty:
                max_penalty = penalty_value
                max_penalty_positions = [(i, j)]  # Cập nhật vị trí mới
            elif penalty_value == max_penalty:
                max_penalty_positions.append((i, j))  # Thêm vị trí nếu có giá trị bằng nhau

# In Maximum Penalty và các vị trí xảy ra
max_penalty_text = f"Maximum penalty MP={max_penalty}, occur at "
penalty_positions_text = " and ".join([f"X{row_labels[i]}{row_labels[j]}" for i, j in max_penalty_positions])

print(f"\n{max_penalty_text}{penalty_positions_text}")

# Lựa chọn nhánh bắt đầu
chosen_branch = f"X{row_labels[max_penalty_positions[0][0]]}{row_labels[max_penalty_positions[0][1]]}"
print(f" We choose {chosen_branch} to begin branch")

