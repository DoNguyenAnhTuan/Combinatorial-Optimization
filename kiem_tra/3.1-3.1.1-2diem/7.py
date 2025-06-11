def activity_selection(activities):
    # Sắp xếp các hoạt động theo thời gian kết thúc
    activities.sort(key=lambda x: x[1])
    print("ANH TUẤN - Bài tập 7:")
    print("\nCác hoạt động sau khi sắp xếp theo thời gian kết thúc:")
    print(activities)
    
    # Danh sách để lưu các hoạt động đã chọn
    selected_activities = []
    
    # Hoạt động đầu tiên luôn được chọn
    last_selected = activities[0]
    selected_activities.append(last_selected)
    print(f"Chọn hoạt động: {last_selected}")

    for i in range(1, len(activities)):
        # Nếu hoạt động hiện tại bắt đầu sau hoặc đúng lúc hoạt động trước kết thúc
        if activities[i][0] >= last_selected[1]:
            selected_activities.append(activities[i])
            print(f"Chọn hoạt động: {activities[i]}")
            last_selected = activities[i]
        else:
            print(f"Bỏ qua hoạt động: {activities[i]} (bị chồng chéo với {last_selected})")
    
    return selected_activities

# Danh sách các hoạt động (thời gian bắt đầu, thời gian kết thúc)
activities = [(5,9),(1,2),(3,4),(0,6),(5,7),(8,9)]

# Gọi hàm và in kết quả
selected = activity_selection(activities)
print("\nCác hoạt động được chọn:", selected)