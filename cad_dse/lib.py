import os
def change_config_no_fix_out(key,value,directory):
    new_content = ""
    with open(directory, 'r') as f:
        content = f.readlines()
    for i in content:
        if str(key) in str(i) :
            new_item = str(key) + str(value)
            print(new_item)
            new_content = new_content + str(new_item) + "\n"
        else :
            new_content = new_content + str(i)
    with open(directory, 'w') as f_new:
        f_new.write(new_content)

def change_config_pl(key,value,directory):
    new_content = ""
    with open(directory, 'r') as f:
        content = f.readlines()
    for i in content:
        if str(key) in str(i) :
            new_item = str(key) + str(value) + ","
            print(new_item)
            new_content = new_content + str(new_item) + "\n"
        else :
            new_content = new_content + str(i)
    with open(directory, 'w') as f_new:
        f_new.write(new_content)

def change_config_pl_end(key,value,directory):
    new_content = ""
    with open(directory, 'r') as f:
        content = f.readlines()
    for i in content:
        if str(key) in str(i) :
            new_item = str(key) + str(value) 
            print(new_item)
            new_content = new_content + str(new_item) + "\n"
        else :
            new_content = new_content + str(i)
    with open(directory, 'w') as f_new:
        f_new.write(new_content)

def change_config_pl_str(key,value,directory):
    new_content = ""
    with open(directory, 'r') as f:
        content = f.readlines()
    for i in content:
        if str(key) in str(i) :
            new_item = str(key) + str(value) + "\","
            print(new_item)
            new_content = new_content + str(new_item) + "\n"
        else :
            new_content = new_content + str(i)
    with open(directory, 'w') as f_new:
        f_new.write(new_content)

def change_config_cts_str(key,value,directory):
    new_content = ""
    with open(directory, 'r') as f:
        content = f.readlines()
    for i in content:
        if str(key) in str(i) :
            new_item = str(key) + str(value) + "\","
            print(new_item)
            new_content = new_content + str(new_item) + "\n"
        else :
            new_content = new_content + str(i)
    with open(directory, 'w') as f_new:
        f_new.write(new_content)

def change_config_cts(key,value,directory):
    new_content = ""
    with open(directory, 'r') as f:
        content = f.readlines()
    for i in content:
        if str(key) in str(i) :
            new_item = str(key) + str(value) + "\","
            print(new_item)
            new_content = new_content + str(new_item) + "\n"
        else :
            new_content = new_content + str(i)
    with open(directory, 'w') as f_new:
        f_new.write(new_content)

def change_config_cts_nostr(key,value,directory):
    new_content = ""
    with open(directory, 'r') as f:
        content = f.readlines()
    for i in content:
        if str(key) in str(i) :
            new_item = str(key) + str(value) + ","
            print(new_item)
            new_content = new_content + str(new_item) + "\n"
        else :
            new_content = new_content + str(i)
    with open(directory, 'w') as f_new:
        f_new.write(new_content)

def change_config_buffer_type(key,value,directory):
    if key=="buffer_type":
        with open(directory, 'r') as f:
            content = f.readlines()
        if len(content) == 0:
            # 读取文件2
            with open('/ChipPilot/script/iEDA/iEDA_config/cts_default_config2.json', 'r') as file2:
                content2 = file2.read()
            # 写入文件1
            with open('/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json', 'w') as file1:
                file1.write(content2)
            # 读取文件2
            with open('/ChipPilot/script/iEDA/iEDA_config/pl_default_config2.json', 'r') as file4:
                content3 = file4.read()
            # 写入文件1
            with open('/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json', 'w') as file3:
                file3.write(content3)
        else:
            content[21] = '        \"' + str(value) + '\"\n'
            with open(directory, 'w') as f_new:
                f_new.writelines(content)

def change_config_routing_layer(key,value,directory):
    if key=="routing_layer_1":
        with open(directory, 'r') as f:
            content = f.readlines()
        if len(content)>24:
            content[24] = '        ' + str(value) + ',\n'
            with open(directory, 'w') as f_new:
                f_new.writelines(content)
    if key=="routing_layer_2":
        with open(directory, 'r') as f:
            content = f.readlines()
        if len(content)>24:
            content[25] = '        ' + str(value) + '\n'
            with open(directory, 'w') as f_new:
                f_new.writelines(content)

def eda_tools(max_fanout,is_max_length_opt,max_length_constraint,is_timing_aware_mode,ignore_net_degree,num_threads,init_wirelength_coef,
                                 reference_hpwl,min_wirelength_force_bar,target_density,bin_cnt_x,bin_cnt_y,max_iter,max_backtrack,init_density_penalty,target_overflow,
    initial_prev_coordi_update_coef,min_precondition,min_phi_coef,max_phi_coef,max_buffer_num,max_displacement,global_right_padding,solution_type,perturb_per_step,cool_rate,
                                 parts,ufactor,new_macro_density,halo_x,halo_y,read_cts_data,write_cts_data,router_type,delay_type,skew_bound,max_buf_tran,max_sink_tran,max_cap,
                                 max_fanout2,max_length,scale_size,cluster_type,cluster_size,buffer_type,routing_layer_1,routing_layer_2,external_model,use_netlist,clock_name,net_name):
    change_config_no_fix_out('    \"max_fanout\": ',max_fanout,"/ChipPilot/script/iEDA/iEDA_config/no_default_config_fixfanout.json")
    change_config_pl('        \"is_max_length_opt\": ',is_max_length_opt,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"max_length_constraint\": ',max_length_constraint,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"is_timing_aware_mode\": ',is_timing_aware_mode,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"ignore_net_degree\": ',ignore_net_degree,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"num_threads\": ',num_threads,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"init_wirelength_coef\": ',init_wirelength_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"reference_hpwl\": ',reference_hpwl,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"min_wirelength_force_bar\": ',min_wirelength_force_bar,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"target_density\": ',target_density,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"bin_cnt_x\": ',bin_cnt_x,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"bin_cnt_y\": ',bin_cnt_y,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"max_iter\": ',max_iter,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"max_backtrack\": ',max_backtrack,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"init_density_penalty\": ',init_density_penalty,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"target_overflow\": ',target_overflow,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"initial_prev_coordi_update_coef\": ',initial_prev_coordi_update_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"min_precondition\": ',min_precondition,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"min_phi_coef\": ',min_phi_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"max_phi_coef\": ',max_phi_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"max_buffer_num\": ',max_buffer_num,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"max_displacement\": ',max_displacement,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('            \"global_right_padding\": ',global_right_padding,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_str('            \"solution_type\": \"',solution_type,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"perturb_per_step\": ',perturb_per_step,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"cool_rate\": ',cool_rate,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"parts\": ',parts,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"ufactor\": ',ufactor,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"new_macro_density\": ',new_macro_density,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"halo_x\": ',halo_x,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"halo_y\": ',halo_y,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_cts('        \"read_cts_data\": \"',read_cts_data,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('        \"write_cts_data\": \"',write_cts_data,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"router_type\": \"',router_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"delay_type\": \"',delay_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"skew_bound\": \"',skew_bound,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_buf_tran\": \"',max_buf_tran,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_sink_tran\": \"',max_sink_tran,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_cap\": \"',max_cap,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_fanout\": \"',max_fanout2,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_length\": \"',max_length,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts_nostr('    \"scale_size\": ',scale_size,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"cluster_type\": \"',cluster_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts_nostr('    \"cluster_size\": ',cluster_size,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"external_model\": \"',external_model,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_buffer_type("buffer_type",buffer_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_routing_layer("routing_layer_1",routing_layer_1,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_routing_layer("routing_layer_2",routing_layer_2,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    os.chdir('/ChipPilot/taskflow')
    os.system('./pipeline')
    with open('/ChipPilot/result/cts/sta/gcd.rpt', 'r') as file:
        # 读取文件内容并转换为列表
        lines = file.readlines()
        # 检查文件是否至少有5行
        if len(lines) >= 5:
            line = lines[4]  # 获取第五行（下标从0开始）
            symbols = line.split('|')  # 以 "|" 分割字符串
            # 检查是否至少有8个 "|" 符号
            if len(symbols) >= 8:
                latency = float(symbols[8].strip())  # 获取第八个符号后的数字并去除首尾空格
    with open('/ChipPilot/result/report/cts_db_gcd.rpt', 'r') as file:
        # 读取文件内容并转换为列表
        lines = file.readlines()
        # 检查文件是否至少有5行
        if len(lines) >= 5:
            line = lines[20]  # 获取第21行（下标从0开始）
            symbols = line.split('|')  # 以 "|" 分割字符串
            # 检查是否至少有8个 "|" 符号
            if len(symbols) >= 2:
                area1 = symbols[2].strip()  # 获取第八个符号后的数字并去除首尾空格  
                area2  = area1.split(' ')
                area = float(area2[0]) # 去除末尾的空格       
    return area,latency

def init():
    with open('./params.txt', 'r') as file:
        lines = file.readlines()

    # 解析每一行
    for line in lines:
        # 删除空格和换行符
        line = line.strip()
        # 提取等号后面的值
        if '=' in line:
            name, value = line.split('=')
            name = name.strip()
            value = value.strip()
            # 根据参数名设置对应的变量值
            if name == 'max_fanout':
                max_fanout = int(value)
            elif name == 'is_max_length_opt':
                is_max_length_opt = int(value)
            elif name == 'max_length_constraint':
                max_length_constraint = int(value)
            elif name == 'is_timing_aware_mode':
                is_timing_aware_mode = int(value)
            elif name == 'ignore_net_degree':
                ignore_net_degree = int(value)
            elif name == 'num_threads':
                num_threads = int(value)
            elif name == 'init_wirelength_coef':
                init_wirelength_coef = int(value)
            elif name == 'reference_hpwl':
                reference_hpwl = int(value)
            elif name == 'min_wirelength_force_bar':
                min_wirelength_force_bar = int(value)
            elif name == 'target_density':
                target_density = int(value)
            elif name == 'bin_cnt_x':
                bin_cnt_x = int(value)
            elif name == 'bin_cnt_y':
                bin_cnt_y = int(value)
            elif name == 'max_iter':
                max_iter = int(value)
            elif name == 'max_backtrack':
                max_backtrack = int(value)
            elif name == 'init_density_penalty':
                init_density_penalty = int(value)
            elif name == 'target_overflow':
                target_overflow = int(value)
            elif name == 'initial_prev_coordi_update_coef':
                initial_prev_coordi_update_coef = int(value)
            elif name == 'min_precondition':
                min_precondition = int(value)
            elif name == 'min_phi_coef':
                min_phi_coef = int(value)
            elif name == 'max_phi_coef':
                max_phi_coef = int(value)
            elif name == 'max_buffer_num':
                max_buffer_num = int(value)
            elif name == 'max_displacement':
                max_displacement = int(value)
            elif name == 'global_right_padding':
                global_right_padding = int(value)
            elif name == 'solution_type':
                solution_type = value
            elif name == 'perturb_per_step':
                perturb_per_step = value
            elif name == 'cool_rate':
                cool_rate = float(value)
            elif name == 'parts':
                parts = int(value)
            elif name == 'ufactor':
                ufactor = int(value)
            elif name == 'new_macro_density':
                new_macro_density = float(value)
            elif name == 'halo_x':
                halo_x = int(value)
            elif name == 'halo_y':
                halo_y = int(value)
            elif name == 'read_cts_data':
                read_cts_data = value
            elif name == 'write_cts_data':
                write_cts_data = value
            elif name == 'router_type':
                router_type = value
            elif name == 'delay_type':
                delay_type = value
            elif name == 'skew_bound':
                skew_bound = value
            elif name == 'max_buf_tran':
                max_buf_tran = value
            elif name == 'max_sink_tran':
                max_sink_tran = value
            elif name == 'max_cap':
                max_cap = value
            elif name == 'max_fanout2':
                max_fanout2 = value
            elif name == 'max_length':
                max_length = value
            elif name == 'scale_size':
                scale_size = int(value)
            elif name == 'cluster_type':
                cluster_type = value
            elif name == 'cluster_size':
                cluster_size = int(value)
            elif name == 'buffer_type':
                buffer_type = value
            elif name == 'routing_layer_1':
                routing_layer_1 = int(value)
            elif name == 'routing_layer_2':
                routing_layer_2 = int(value)
            elif name == 'external_model':
                external_model = value
            elif name == 'use_netlist':
                use_netlist = value
            elif name == 'clock_name':
                clock_name = value
            elif name == 'net_name':
                net_name = value
    change_config_no_fix_out('    \"max_fanout\": ',max_fanout,"/ChipPilot/script/iEDA/iEDA_config/no_default_config_fixfanout.json")
    change_config_pl('        \"is_max_length_opt\": ',is_max_length_opt,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"max_length_constraint\": ',max_length_constraint,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"is_timing_aware_mode\": ',is_timing_aware_mode,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"ignore_net_degree\": ',ignore_net_degree,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('        \"num_threads\": ',num_threads,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"init_wirelength_coef\": ',init_wirelength_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"reference_hpwl\": ',reference_hpwl,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"min_wirelength_force_bar\": ',min_wirelength_force_bar,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"target_density\": ',target_density,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"bin_cnt_x\": ',bin_cnt_x,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"bin_cnt_y\": ',bin_cnt_y,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"max_iter\": ',max_iter,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"max_backtrack\": ',max_backtrack,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"init_density_penalty\": ',init_density_penalty,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"target_overflow\": ',target_overflow,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"initial_prev_coordi_update_coef\": ',initial_prev_coordi_update_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"min_precondition\": ',min_precondition,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"min_phi_coef\": ',min_phi_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"max_phi_coef\": ',max_phi_coef,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"max_buffer_num\": ',max_buffer_num,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"max_displacement\": ',max_displacement,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('            \"global_right_padding\": ',global_right_padding,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_str('            \"solution_type\": \"',solution_type,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"perturb_per_step\": ',perturb_per_step,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"cool_rate\": ',cool_rate,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"parts\": ',parts,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('                \"ufactor\": ',ufactor,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl_end('                \"new_macro_density\": ',new_macro_density,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"halo_x\": ',halo_x,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_pl('            \"halo_y\": ',halo_y,"/ChipPilot/script/iEDA/iEDA_config/pl_default_config.json")
    change_config_cts('        \"read_cts_data\": \"',read_cts_data,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('        \"write_cts_data\": \"',write_cts_data,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"router_type\": \"',router_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"delay_type\": \"',delay_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"skew_bound\": \"',skew_bound,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_buf_tran\": \"',max_buf_tran,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_sink_tran\": \"',max_sink_tran,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_cap\": \"',max_cap,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_fanout\": \"',max_fanout2,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"max_length\": \"',max_length,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts_nostr('    \"scale_size\": ',scale_size,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"cluster_type\": \"',cluster_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts_nostr('    \"cluster_size\": ',cluster_size,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_cts('    \"external_model\": \"',external_model,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_buffer_type("buffer_type",buffer_type,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_routing_layer("routing_layer_1",routing_layer_1,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    change_config_routing_layer("routing_layer_2",routing_layer_2,"/ChipPilot/script/iEDA/iEDA_config/cts_default_config.json")
    os.chdir('/ChipPilot/taskflow')
    os.system('g++ -std=c++17 examples/pipeline.cpp -I. -O2 -pthread -o pipeline')
    os.system('./pipeline')