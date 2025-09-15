import awkward as ak

# 原始 awkward 数组
array = ak.Array([[], [], [[0.242], [2.78]], [], [[2.5]], [[]], []])
print(array)
print(ak.all(array < 0.8, axis=-1))
# 找到每个子数组的最小值（保持空数组为 None）
min_values = ak.min(array, axis=1, mask_identity=True)
print(min_values)
min_values = ak.flatten(ak.fill_none(ak.pad_none(min_values, 1), 999))
print((array == min_values))
min_cut = (array == min_values)
min_cut = ak.where((array == min_values), array, 999)
print(min_cut)
print(min_values)
print(ak.min(array, axis=2, mask_identity=True))
# 广播 array 和 min_values
# broadcasted_array, broadcasted_min_values = ak.broadcast_arrays(array, min_values)

# 检查 array 和 broadcasted_min_values 是否相等，替换非最小值为 999
# 对于完全空数组，直接保留原样
# result = ak.where(ak.is_none(min_values), array, ak.where(broadcasted_array == broadcasted_min_values, broadcasted_array, 999))

# print(result)

