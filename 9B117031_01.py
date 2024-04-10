# 函式 get_even_squares(num_list)
# 接受一個整數列表 num_list 作為參數
# 使用【列表推導式(List Comprehension)】返回 num_list 中所有偶數的平方值列表
def get_even_squares(num_list):
    return [x**2 for x in num_list if x % 2 == 0]

# 函式 get_odd_cubes(num_list)
# 接受一個整數列表 num_list 作為參數
# 使用【迴圈】返回 num_list 中所有奇數的 3 次方值列表
def get_odd_cubes(num_list):
    result = []
    for num in num_list:
        if num % 2 != 0:
            result.append(num**3)
    return result

# 函式 get_sliced_list(num_list)
# 接受一個整數列表 num_list 作為參數
# 使用【切片】(slicing)返回 num_list 從第 5 個元素開始到最後一個元素(包含最後一個)的子列表
def get_sliced_list(num_list):
    return num_list[4:]
# 函式 get_sliced_list(num_list)
# 接受一個整數列表 num_list 作為參數
# 使用【切片】(slicing)返回 num_list 從第 5 個元素開始到最後一個元素(包含最後一個)的子列表
def get_sliced_list(num_list):
    return num_list[4:]

# 函式 format_numbers(numbers)
# 接受一個數字列表 numbers 作為參數
# 返回一個新列表,其中每個數字都被格式化為 8 個字元的寬度,並靠右對齊
def format_numbers(numbers):
    return [f"{num:>8}" for num in numbers]

# 在程式中建立一個整數列表
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 分別呼叫前 3 個函式,獲取偶數平方值列表、奇數立方值列表、切片子列表
even_squares = get_even_squares(num_list)
print("偶數平方值列表:", ", ".join(map(str, even_squares)))

odd_cubes = get_odd_cubes(num_list)
print("奇數立方值列表:", ", ".join(map(str, odd_cubes)))

sliced_list = get_sliced_list(num_list)
print("切片子列表:", ", ".join(map(str, sliced_list)))

# 再以上述 3 個函式的結果為基礎,呼叫最後一個函式,並搭配 print() 與 join() 進行顯示
formatted_numbers = format_numbers(sliced_list)
print("格式化後的切片子列表:", ", ".join(formatted_numbers))
