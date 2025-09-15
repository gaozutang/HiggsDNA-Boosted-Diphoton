import awkward as ak

# 输入数据
arr = ak.Array([[], [], [[0.242], [2.78]], [], [[2.5]], [[]], []])

# 对每一层的数组进行操作，首先展平第一层
flattened = ak.flatten(arr, axis=1)

# 找到最小值
min_val = ak.min(flattened[flattened != 0])

# 替换非最小值为999
modified = ak.where(arr == min_val, arr, 999)

# 输出结果
print(modified)

