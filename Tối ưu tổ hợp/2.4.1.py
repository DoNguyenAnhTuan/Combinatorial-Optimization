# ex 5
# x1: số giờ thực thi P1
# x2: số giờ thực thi P2

# min 5x1+3x2

# st( ràng buộc) 
# 3x1 + x2 >=100  (do phải cần tối thiểu 100A)
#  x1 + x2 >=50 (B)
#  x1      >=20 (C)
#  x1,x2   >=0







# ex6
# x1: mẫu lúa mì
# x2: mẫu ngô

# max 200x1 + 250x2

# st( ràng buộc) 
            #   x1 + x2  <=135 
            #  4x1 + 2x2 <=100 
            #  3x1 + 5x2 <=120
            #  x1,x2   >=0
import numpy as np

# Hệ số của các biến x1, x2
A = np.array([[3, 5], [4, 2]])

# Hệ số phía bên phải của dấu bằng
B = np.array([120, 100])

# Giải hệ phương trình
solution = np.linalg.solve(A, B)

# In kết quả
x1, x2 = solution
print(f"Giá trị của x1 = {x1}, x2 = {x2}")
