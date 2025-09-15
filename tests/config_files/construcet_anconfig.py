import json

# 定义循环的值
ggh_values = ['ggh', 'tth', 'vbf', 'vh']
GluGlu_values = ['GluGluHtoGG', 'ttHtoGG', 'VBFHtoGG', 'VHtoGG']
number_values = ['120', '125', '130']
post_values = ['post', 'pre']

# 循环生成文件
for ggh in ggh_values:
    GluGlu = GluGlu_values[ggh_values.index(f'{ggh}')]
    for number in number_values:
        for post in post_values:
            # 构建文件名
            filename = f"{ggh}_{number}_{post}_analysis.json"
            # 创建空的数据结构
            data = {"samplejson": f"sample_json/{ggh}_{number}_{post}.json", "workflow": "dystudies", "metaconditions": "Era2017_legacy_v1", "year": {f"{GluGlu}_M-{number}_{post}EE": [f"2022{post}EE"]}, "taggers": [], "systematics": {f"{GluGlu}_M-{number}_{post}EE": ["Pileup", "Scale", "Smearing", "energyErrShift", "AlphaS", "PartonShower", "LHEScale", "LHEPdf", "ElectronVetoSF", "PreselSF", "TriggerSF", "Material", "FNUF"]}, "corrections": {f"{GluGlu}_M-{number}_{post}EE": ["Pileup", "Smearing", "energyErrShift", "ElectronVetoSF", "PreselSF", "TriggerSF", "jerc_jet_syst", "Material", "FNUF"]}}
            # 写入到 JSON 文件中
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

print("文件创建完成。")
