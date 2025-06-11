# Danh sách các hoạt động (start_time, end_time)
# activities = [(5,9), (1,2), (3,4), (0,6), (5,7), (8,9)]
activities = [(1,3), (2,5), (3,4), (4,7), (7,10), (8,9), (9,11), (9,13), (11,12), (12,14)]
# Bước S1: Sắp xếp các hoạt động theo thời gian kết thúc (end_time)
activities_sorted = sorted(activities, key=lambda x: x[1])
print("S1. Danh sách các hoạt động đã sắp xếp:", activities_sorted)

# Bước S2: Chọn hoạt động đầu tiên
selected_activities = []
selected_activities.append(activities_sorted[0])
print("S2. Hoạt động đầu tiên được chọn:", selected_activities)

# Bước S3: Lặp qua các hoạt động còn lại và kiểm tra
for i in range(1, len(activities_sorted)):
    # Hiển thị trạng thái hiện tại của hoạt động trước và hoạt động hiện tại
    print(f"S3. Previous = {selected_activities[-1]}, Current = {activities_sorted[i]}")
    
    # Nếu thời gian bắt đầu của hoạt động hiện tại >= thời gian kết thúc của hoạt động trước đó
    if activities_sorted[i][0] >= selected_activities[-1][1]:
        selected_activities.append(activities_sorted[i])
        print(f" => Selected: {activities_sorted[i]}")
    else:
        print(f" => Skip: {activities_sorted[i]}")

# In ra danh sách các hoạt động được chọn cuối cùng
print("Kết quả cuối cùng: Các hoạt động được chọn:", selected_activities)
