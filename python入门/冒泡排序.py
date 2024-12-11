def bubble_sort(arr):
    n = len(arr)  # 获取数组长度
    for j in range(n):  # 外层循环，遍历数组长度次数
        for i in range(n - 1 - j):  # 内层循环，每次遍历未排序部分的元素
            if arr[i] > arr[i + 1]:  # 如果当前元素大于下一个元素
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # 交换两个元素的位置
        print(arr)  # 打印每次排序后的数组

arr = [5, 3, 4, 2, 1]
bubble_sort(arr)
# 对数组从小到大排序
arr.sort()
print("从小到大排序后的数组：", arr)

# 对数组从大到小排序
arr.reverse()
print("从大到小排序后的数组：", arr)



s = "jdasjdjjddsk"
c = s.find("a")
print(c)
