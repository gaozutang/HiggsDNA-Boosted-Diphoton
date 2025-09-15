import awkward
from higgs_dna.selections.Fatjet_selections import select_min

threshold = 0.8

data = awkward.Array([[], [], [[0.242], [0.3], [2.78]], [], [[2.5]], [[]], [[5],[4],[0.4]]])
print(data)
data_sel = select_min(data)
print(data_sel)
# print(fla_data)
# min_mval = awkward.min(data, axis=1)
# print(min_mval)
# min_cut = (fla_data == min_mval)
# print(min_cut)
dr_cut = awkward.all(data_sel < threshold, axis=-1)
print(dr_cut)

# import awkward as ak

# # 定义你的awkward数组
# arr = ak.Array([[], [], [[0.242], [2.78]], [], [[2.5]], [[]], []])

# # 使用awkward内置函数来处理数组
# def replace_with_min(arr):
#     # 在每个子数组中找到最小的元素
#     min_vals = ak.min(arr, axis=1, mask_identity=999)  # 在axis=1方向上找到最小值
#     # 将最小值放回去，其他位置的数字变为999
#     return ak.where(arr != min_vals[..., None], 999, arr)

# # 处理数组
# modified_arr = replace_with_min(arr)

# print(modified_arr)


