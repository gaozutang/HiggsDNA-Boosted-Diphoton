import awkward as ak

# 原始 awkward 数组
array = ak.Array([[], [], [[0.242], [2.78]], [], [[2.5]], [[]], []])
print(array)
# 找到每个非空子数组的最小值
print(ak.flatten(ak.min(array, axis=1, mask_identity=True)))
print(array == ak.min(array, axis=1, mask_identity=True))
min_values = ak.singletons(ak.min(array, axis=1, mask_identity=True))
print(min_values)
# 判断是否为嵌套空数组 [[]]
is_nested_empty = ak.any(ak.num(array, axis=2) == 0, axis=1)

print(is_nested_empty)
# 保留嵌套空数组 `[[]]` 和其他最小值
result = ak.where(is_nested_empty, array, ak.where(ak.is_none(array), array, min_values))

print(result)

