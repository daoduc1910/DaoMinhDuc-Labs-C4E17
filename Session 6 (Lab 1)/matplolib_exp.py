from matplotlib import pyplot

#1. Prepare data
machine_counts = [18, 4, 2]

#2. Prepare labels
#cho biết ý nghĩa của cái data này là gì
machine_names = ["PC", "MAC", "Linux"]

#3. Draw pie
pyplot.pie(machine_counts, labels = machine_names, autopct = "%.1f%%", shadow = True, explode = [0, 0.1, 0.2])
pyplot.title("PC vs MAC vs Linux") #viết tiêu đề cho đồ thị
#explode dùng để nhấn mạnh vào data mà mình muốn nhấn mạnh
#shadow là thêm bóng cho pie
#autopct là tự động tính phần trăm
pyplot.axis("equal")
#4. Show
pyplot.show()
