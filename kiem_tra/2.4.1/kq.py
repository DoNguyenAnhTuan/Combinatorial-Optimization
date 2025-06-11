import numpy as np

def simplex(c, A, b):
    """
    Giải bài toán lập trình tuyến tính dạng chuẩn bằng phương pháp Simplex.
    
    Hàm mục tiêu: max c.T * x
    Ràng buộc: A * x = b, x >= 0
    
    Parameters:
    c : numpy.array
        Hệ số của hàm mục tiêu.
    A : numpy.array
        Ma trận các hệ số của ràng buộc.
    b : numpy.array
        Vế phải của các ràng buộc.
        
    Returns:
    x : numpy.array
        Nghiệm tối ưu.
    z : float
        Giá trị hàm mục tiêu tại nghiệm tối ưu.
    """
    # Bước 1: Khởi tạo bảng Simplex
    num_constraints, num_variables = A.shape
    
    # Khởi tạo bảng Simplex (bao gồm cả các biến cơ sở)
    tableau = np.zeros((num_constraints + 1, num_variables + num_constraints + 1))
    
    # Điền ma trận A vào bảng
    tableau[:num_constraints, :num_variables] = A
    
    # Thêm biến dư vào bảng
    tableau[:num_constraints, num_variables:num_variables + num_constraints] = np.eye(num_constraints)
    
    # Điền vế phải của các ràng buộc vào bảng
    tableau[:num_constraints, -1] = b
    
    # Điền hệ số của hàm mục tiêu (dạng -z vì chuyển max thành min)
    tableau[-1, :num_variables] = -c
    
    print("Initial Simplex Tableau:")
    print(tableau)
    
    # Bước 2: Lặp lại quá trình tìm nghiệm tối ưu
    while True:
        # Bước 2.1: Kiểm tra nếu tất cả các giá trị ở hàng cuối không âm => Đã tối ưu
        if np.all(tableau[-1, :-1] >= 0):
            print("Found optimal solution!")
            break
        
        # Bước 2.2: Tìm cột chọn (Pivot column) - Chọn cột có giá trị âm nhỏ nhất
        pivot_col = np.argmin(tableau[-1, :-1])
        
        # Bước 2.3: Tìm hàng chọn (Pivot row)
        if np.all(tableau[:, pivot_col] <= 0):
            raise Exception("The problem is unbounded.")
        
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[tableau[:-1, pivot_col] <= 0] = np.inf
        pivot_row = np.argmin(ratios)
        
        print(f"Pivot Element at Row: {pivot_row}, Column: {pivot_col}")
        
        # Bước 2.4: Biến đổi bảng Simplex bằng cách chia hàng chọn cho phần tử pivot
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element
        
        # Biến đổi các hàng khác để đảm bảo rằng các phần tử khác trong cột chọn đều bằng 0
        for i in range(num_constraints + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]
        
        print("Simplex Tableau after Pivoting:")
        print(tableau)
    
    # Bước 3: Trích xuất nghiệm tối ưu
    x = np.zeros(num_variables)
    for i in range(num_constraints):
        basic_var_index = np.where(tableau[i, :num_variables] == 1)[0]
        if len(basic_var_index) == 1:
            x[basic_var_index[0]] = tableau[i, -1]
    
    # Giá trị hàm mục tiêu tối đa
    z = tableau[-1, -1]
    
    return x, z

# Bài toán mẫu
# c = np.array([1,0])  # Hệ số hàm mục tiêu max x1
# A = np.array([
#     [2, -1],
#     [2, 1],
#     [0, 1]
# ])  # Ràng buộc 2x1 - x2 <= 4, 2x1 + x2 <= 8, x2 <= 3
# b = np.array([4, 8, 3])  # Vế phải của ràng buộc
c = np.array([100,50,20])  # Hệ số hàm mục tiêu max 100x1 +50x2 +20x3
A = np.array([
    [3, 1, 1],
    [1, 1, 0],
])  # Ràng buộc 2x1 - x2 <= 4, 2x1 + x2 <= 8, x2 <= 3
b = np.array([5, 3])  # Vế phải của ràng buộc

# Giải bài toán bằng phương pháp Simplex
optimal_solution, optimal_value = simplex(c, A, b)

print("\nOptimal Solution:", optimal_solution)
print("Optimal Objective Value:", optimal_value)
