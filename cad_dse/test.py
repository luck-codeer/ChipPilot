time_cost2=67725
with open("ChipPilotReport.txt", "r") as file:
        first_line = file.readline().strip()
        parallel_cost = float(first_line.split("：")[1].strip()[:-1])
        speed_up = time_cost2 / parallel_cost
        result_str = "加速比为：%.2f" % speed_up 
        print(result_str)       
with open('BaseDSEReport.txt', 'a') as file2:
        file2.write(result_str + '\n')
