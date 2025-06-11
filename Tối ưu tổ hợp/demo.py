import numpy as np

# Tạo ma trận chi phí
cost_matrix = np.array([
    [np.nan, 5, 8, 4, 5],
    [5, np.nan, 7, 4, 5],
    [8, 7, np.nan, 8, 6],
    [4, 4, 8, np.nan, 8],
    [5, 5, 6, 8, np.nan]
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

# Chuyển đổi RM thành numpy array
RM = np.array(RM)

# In ma trận RM
print("Ma trận RM:")
print("     A   B   C   D   E   RM")
row_labels = ['A', 'B', 'C', 'D', 'E']
for i in range(len(RM)):
    print(f"{row_labels[i]}  {RM[i]}")

# Lấy giá trị tại hàng C (chỉ số 2) và cột E (chỉ số 4)
row_index = 2  # Chỉ số hàng C
col_index = 3  # Chỉ số cột E

# Giá trị tại vị trí hàng C và cột E
value_CE = RM[row_index, col_index]
print(f"\nGiá trị tại vị trí hàng C và cột E là: {value_CE}")
