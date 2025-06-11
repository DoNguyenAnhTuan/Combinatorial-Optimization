import numpy as np

# Ma trận chi phí gốc
cost_matrix = np.array([
    [np.nan, 5, 8, 4, 5],
    [5, np.nan, 7, 4, 5],
    [8, 7, np.nan, 8, 6],
    [4, 4, 8, np.nan, 8],
    [5, 5, 6, 8, np.nan]
])
# Ma trận chi phí gốc
# cost_matrix = np.array([
#     [np.nan, 4, 9, 5],
#     [6, np.nan, 4, 8],
#     [9, 4, np.nan, 9],
#     [5, 8, 9, np.nan]

# ])
# Bước 1: Tìm giá trị nhỏ nhất trong mỗi hàng
min_values = np.nanmin(cost_matrix, axis=1)

# Bước 2: Tạo ma trận RM
RM = []

for i in range(cost_matrix.shape[0]):
    row = []
    for j in range(cost_matrix.shape[1]):
        if not np.isnan(cost_matrix[i, j]):
            row.append(cost_matrix[i, j] - min_values[i])
        else:
            row.append('×')  # Giữ lại ký tự '×' cho giá trị không hợp lệ
    row.append(min_values[i])  # Thêm giá trị nhỏ nhất vào cuối hàng
    RM.append(row)

# In kết quả
print("Ma trận RM:")
print("     A   B   C   D   E   RM")
row_labels = ['A', 'B', 'C', 'D', 'E']
for i in range(len(RM)):
    print(f"{row_labels[i]}  {RM[i]}")

# Tính tổng của các giá trị nhỏ nhất
total_sum = sum(min_values)
print(f"∑ = {total_sum}")
