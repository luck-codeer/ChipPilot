import os
import re
os.system("python3 base_DSE.py")
os.system("python3 run_ChipPilot.py")
with open('./report.txt', 'r') as file:
    content = file.read()
    # 使用正则表达式提取数字
    pattern = r"\d+.\d+"  # 匹配一个或多个数字，然后是一个小数点，再跟着一个或多个数字
    matches = re.findall(pattern, content)

    # 获取匹配到的数字
    if matches:
        time1 = float(matches[0]) 
        time2 = float(matches[1])
speed_up = time1 / time2
result_str = "加速比为：%.2f" % speed_up        
with open('report.txt', 'a') as file2:
    file2.write(result_str + '\n')