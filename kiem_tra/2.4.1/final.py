import numpy as np

def print_tableau(tableau, basic_vars, non_basic_vars):
    print("\nSimplex Tableau:")
    
    # Tiêu đề: x1, x2, ..., xn, b, B
    headers = non_basic_vars + ["b", "B"]
    print(" ".join(f"{h:>6}" for h in headers))
    
    # In các hàng của bảng Simplex
    for i, row in enumerate(tableau):
        var = basic_vars[i] if i < len(basic_vars) else "z"
        print(" ".join(f"{v:>6.2f}" for v in row[:-1]) + f" {row[-1]:>6.2f} {var}")
    
def simplex(c, A, b):
    num_constraints, num_variables = A.shape
    
    # Bảng Simplex
    tableau = np.zeros((num_constraints + 1, num_variables + num_constraints + 1))
    
    # Điền ma trận A vào bảng
    tableau[:num_constraints, :num_variables] = A
    
    # Thêm biến dư vào bảng
    tableau[:num_constraints, num_variables:num_variables + num_constraints] = np.eye(num_constraints)
    
    # Điền vế phải của ràng buộc vào bảng
    tableau[:num_constraints, -1] = b
    
    # Điền hệ số của hàm mục tiêu
    tableau[-1, :num_variables] = -c
    
    # Biến cơ bản (basic variables) và không cơ bản (non-basic variables)
    basic_vars = [f"x{num_variables + i + 1}" for i in range(num_constraints)]  # x4, x5 (biến dư)
    non_basic_vars = [f"x{i+1}" for i in range(num_variables)]  # x1, x2, x3
    
    print("\nInitial Simplex Tableau:")
    print_tableau(tableau, basic_vars, non_basic_vars)
    
    iteration = 0
    while True:
        iteration += 1
        print(f"\nIteration {iteration}:")
        
        # Kiểm tra nếu tất cả các giá trị ở hàng cuối >= 0
        if np.all(tableau[-1, :-1] >= 0):
            print("Found optimal solution!")
            break
        
        # Chọn cột pivot
        pivot_col = np.argmin(tableau[-1, :-1])
        print(f"The last row z - x{pivot_col + 1} = {tableau[-1, pivot_col]} => x{pivot_col + 1} enters.")
        
        # Tìm hàng pivot (Ratio test)
        if np.all(tableau[:, pivot_col] <= 0):
            raise Exception("The problem is unbounded.")
        
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[tableau[:-1, pivot_col] <= 0] = np.inf
        pivot_row = np.argmin(ratios)
        print(f"Ratio test: ", ", ".join([f"r{i+3} = {ratios[i]:.2f}" for i in range(len(ratios))]), 
              f"=> {basic_vars[pivot_row]} leaves.")
        
        # Lấy phần tử pivot
        pivot_element = tableau[pivot_row, pivot_col]
        
        # Chia hàng pivot cho phần tử pivot
        tableau[pivot_row, :] /= pivot_element
        
        # Biến đổi các hàng khác
        for i in range(num_constraints + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]
        
        # Cập nhật biến cơ bản
        basic_vars[pivot_row] = f"x{pivot_col + 1}"
        
        print(f"Pivot Element at Row: {pivot_row}, Column: {pivot_col}")
        print_tableau(tableau, basic_vars, non_basic_vars)
    
    # Trích xuất nghiệm tối ưu
    x = np.zeros(num_variables)
    for i in range(num_constraints):
        basic_var_index = np.where(tableau[i, :num_variables] == 1)[0]
        if len(basic_var_index) == 1:
            x[basic_var_index[0]] = tableau[i, -1]
    
    z = tableau[-1, -1]
    
    return x, z

# Bài toán mẫu
# c = np.array([1, 0])  # Hệ số hàm mục tiêu max x1 (chỉ x1 có hệ số là 1)
# A = np.array([
#     [2, -1],
#     [2, 1],
#     [0, 1]
# ])  # Ràng buộc 2x1 - x2 <= 4, 2x1 + x2 <= 8, x2 <= 3
# b = np.array([4, 8, 3])  # Vế phải của ràng buộc

c = np.array([12, 6])  # Hệ số hàm mục tiêu max x1 (chỉ x1 có hệ số là 1)
A = np.array([
    [3, 1],
    [1, 1]
    
])  # Ràng buộc 2x1 - x2 <= 4, 2x1 + x2 <= 8, x2 <= 3
b = np.array([7, 5])  # Vế phải của ràng buộc

# Giải bài toán bằng phương pháp Simplex
optimal_solution, optimal_value = simplex(c, A, b)

print("\nOptimal Solution:", optimal_solution)
print("Optimal Objective Value:", optimal_value)




