import heapq

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def branch_and_bound(items, K):
    n = len(items)
    initial_value = 0
    initial_room = K
    initial_ub = sum(item.value for item in items)  # Tổng tất cả các giá trị là cận trên ban đầu

    # Ban đầu
    print(f"Ban đầu: Value: {initial_value}, Room: {initial_room}, UB: {initial_ub}")
    print("=====")

    # Nhánh x1=1 (chọn x1)
    value_x1_1 = initial_value + items[0].value
    room_x1_1 = initial_room - items[0].weight
    ub_x1_1 = initial_ub  # UB vẫn giữ nguyên

    print(f"Với x1=1")
    print(f"Value: {value_x1_1}, Room: {room_x1_1}, UB: {ub_x1_1}")

    # Nhánh x2=1 tại x1=1
    value_x2_1_x1_1 = value_x1_1 + items[1].value
    room_x2_1_x1_1 = room_x1_1 - items[1].weight
    ub_x2_1_x1_1 = ub_x1_1  # UB vẫn giữ nguyên

    print(f"  Với x2=1 tại nhánh x1=1")
    print(f"  Value: {value_x2_1_x1_1}, Room: {room_x2_1_x1_1}, UB: {ub_x2_1_x1_1}")

    # Nhánh x3=1 tại nhánh x2=1, x1=1
    value_x3_1_x2_1_x1_1 = value_x2_1_x1_1 + items[2].value
    room_x3_1_x2_1_x1_1 = room_x2_1_x1_1 - items[2].weight
    ub_x3_1_x2_1_x1_1 = ub_x2_1_x1_1  # UB vẫn giữ nguyên
    print(f"          Với x3=1 tại nhánh x2=1, x1=1")
    print(f"          Value: {value_x3_1_x2_1_x1_1}, Room: {room_x3_1_x2_1_x1_1}, UB: {ub_x3_1_x2_1_x1_1}")

    # Nhánh x3=0 tại nhánh x2=1, x1=1
    value_x3_0_x2_1_x1_1 = value_x2_1_x1_1
    room_x3_0_x2_1_x1_1 = room_x2_1_x1_1
    ub_x3_0_x2_1_x1_1 = sum(item.value for item in items[3:]) + value_x2_1_x1_1  # UB từ x4
    print(f"          Với x3=0 tại nhánh x2=1, x1=1")
    print(f"          Value: {value_x3_0_x2_1_x1_1}, Room: {room_x3_0_x2_1_x1_1}, UB: {ub_x3_0_x2_1_x1_1}")

    # Nhánh x2=0 tại x1=1
    value_x2_0_x1_1 = value_x1_1
    room_x2_0_x1_1 = room_x1_1
    ub_x2_0_x1_1 = sum(item.value for item in items[2:]) + value_x1_1  # UB từ x3, x4
    print(f"  Với x2=0 tại nhánh x1=1")
    print(f"  Value: {value_x2_0_x1_1}, Room: {room_x2_0_x1_1}, UB: {ub_x2_0_x1_1}")

    # Nhánh x3=1 tại nhánh x2=0, x1=1
    value_x3_1_x2_0_x1_1 = value_x2_0_x1_1 + items[2].value
    room_x3_1_x2_0_x1_1 = room_x2_0_x1_1 - items[2].weight
    ub_x3_1_x2_0_x1_1 = ub_x2_0_x1_1  # UB vẫn giữ nguyên
    print(f"  Với x3=1 tại nhánh x2=0, x1=1")
    print(f"  Value: {value_x3_1_x2_0_x1_1}, Room: {room_x3_1_x2_0_x1_1}, UB: {ub_x3_1_x2_0_x1_1}")

    # Nhánh x3=0 tại nhánh x2=0, x1=1
    value_x3_0_x2_0_x1_1 = value_x2_0_x1_1
    room_x3_0_x2_0_x1_1 = room_x2_0_x1_1
    ub_x3_0_x2_0_x1_1 = sum(item.value for item in items[3:]) + value_x2_0_x1_1  # UB từ x4
    print(f"  Với x3=0 tại nhánh x2=0, x1=1")
    print(f"  Value: {value_x3_0_x2_0_x1_1}, Room: {room_x3_0_x2_0_x1_1}, UB: {ub_x3_0_x2_0_x1_1}")
    print("=====")

    # Nhánh x1=0 (không chọn x1)
    value_x1_0 = initial_value
    room_x1_0 = initial_room
    ub_x1_0 = sum(item.value for item in items[1:])  # UB chỉ còn tính từ x2, x3, x4

    print(f"Với x1=0")
    print(f"Value: {value_x1_0}, Room: {room_x1_0}, UB: {ub_x1_0}")

    # Nhánh x2=1 tại nhánh x1=0
    value_x2_1_x1_0 = value_x1_0 + items[1].value
    room_x2_1_x1_0 = room_x1_0 - items[1].weight
    ub_x2_1_x1_0 = ub_x1_0  # UB vẫn giữ nguyên

    print(f"  Với x2=1 tại nhánh x1=0")
    print(f"  Value: {value_x2_1_x1_0}, Room: {room_x2_1_x1_0}, UB: {ub_x2_1_x1_0}")

    # Nhánh x3=1 tại nhánh x2=1, x1=0
    value_x3_1_x2_1_x1_0 = value_x2_1_x1_0 + items[2].value
    room_x3_1_x2_1_x1_0 = room_x2_1_x1_0 - items[2].weight
    ub_x3_1_x2_1_x1_0 = ub_x2_1_x1_0  # UB vẫn giữ nguyên
    print(f"         Với x3=1 tại nhánh x2=1, x1=0")
    print(f"         Value: {value_x3_1_x2_1_x1_0}, Room: {room_x3_1_x2_1_x1_0}, UB: {ub_x3_1_x2_1_x1_0}")

    # Nhánh x3=0 tại nhánh x2=1, x1=0
    value_x3_0_x2_1_x1_0 = value_x2_1_x1_0
    room_x3_0_x2_1_x1_0 = room_x2_1_x1_0
    ub_x3_0_x2_1_x1_0 = sum(item.value for item in items[3:]) + value_x2_1_x1_0  # UB từ x4
    print(f"         Với x3=0 tại nhánh x2=1, x1=0")
    print(f"         Value: {value_x3_0_x2_1_x1_0}, Room: {room_x3_0_x2_1_x1_0}, UB: {ub_x3_0_x2_1_x1_0}")

    # Nhánh x2=0 tại nhánh x1=0
    value_x2_0_x1_0 = value_x1_0
    room_x2_0_x1_0 = room_x1_0
    ub_x2_0_x1_0 = sum(item.value for item in items[2:]) + value_x1_0  # UB chỉ tính từ x3, x4

    print(f"  Với x2=0 tại nhánh x1=0")
    print(f"  Value: {value_x2_0_x1_0}, Room: {room_x2_0_x1_0}, UB: {ub_x2_0_x1_0}")

    # Nhánh x3=1 tại nhánh x2=0, x1=0
    value_x3_1_x2_0_x1_0 = value_x2_0_x1_0 + items[2].value
    room_x3_1_x2_0_x1_0 = room_x2_0_x1_0 - items[2].weight
    ub_x3_1_x2_0_x1_0 = ub_x2_0_x1_0  # UB vẫn giữ nguyên
    print(f"         Với x3=1 tại nhánh x2=0, x1=0")
    print(f"         Value: {value_x3_1_x2_0_x1_0}, Room: {room_x3_1_x2_0_x1_0}, UB: {ub_x3_1_x2_0_x1_0}")

    # Nhánh x3=0 tại nhánh x2=0, x1=0
    value_x3_0_x2_0_x1_0 = value_x2_0_x1_0
    room_x3_0_x2_0_x1_0 = room_x2_0_x1_0
    ub_x3_0_x2_0_x1_0 = sum(item.value for item in items[3:]) + value_x2_0_x1_0  # UB từ x4
    print(f"         Với x3=0 tại nhánh x2=0, x1=0")
    print(f"         Value: {value_x3_0_x2_0_x1_0}, Room: {room_x3_0_x2_0_x1_0}, UB: {ub_x3_0_x2_0_x1_0}")
    print("=====")

# Ví dụ sử dụng
items = [
    Item("X1", 4, 5),
    Item("X2", 3, 4),
    Item("X3", 2, 3),
    Item("X4", 1, 2)
]
K = 6  # Dung lượng tối đa
branch_and_bound(items, K)