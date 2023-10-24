import optuna
from lib import eda_tools
import sqlite3
import multiprocessing
import os
from lib import init
import time

def objective(trial):
    max_fanout=trial.suggest_int("max_fanout",20,40)
    is_max_length_opt = trial.suggest_int("is_max_length_opt",0,1)
    max_length_constraint = trial.suggest_int("max_length_constraint", 100000,1000000)
    is_timing_aware_mode = trial.suggest_int("is_timing_aware_mode",0,1)
    ignore_net_degree = trial.suggest_int("ignore_net_degree", 10,1000)
    num_threads = trial.suggest_int("num_threads", 1, 64)
    init_wirelength_coef=trial.suggest_float("init_wirelength_coef",0,1)
    reference_hpwl=trial.suggest_int("reference_hpwl",100,1000000)
    min_wirelength_force_bar=trial.suggest_int("min_wirelength_force_bar",0,1000 )
    target_density=trial.suggest_float("target_density",0,1)
    bin_cnt_x=trial.suggest_categorical("bin_cnt_x",[16,32,64,128,256,512,1024])
    bin_cnt_y = trial.suggest_categorical("bin_cnt_y", [16, 32, 64, 128, 256, 512, 1024])
    max_iter=trial.suggest_int("max_iter",50,2000)
    max_backtrack=trial.suggest_int("max_backtrack",0,100)
    init_density_penalty=trial.suggest_float("init_density_penalty",0,1)
    target_overflow=trial.suggest_float("target_overflow",0,1)
    initial_prev_coordi_update_coef=trial.suggest_int("initial_prev_coordi_update_coef",10,10000)
    min_precondition=trial.suggest_int("min_precondition",1,100)
    min_phi_coef=trial.suggest_float("min_phi_coef",0,1)
    max_phi_coef=trial.suggest_float("max_phi_coef",0,1)
    max_buffer_num=trial.suggest_int("max_buffer_num",0,10000000)
    max_displacement=trial.suggest_int("max_displacement",10000,1000000)
    global_right_padding=trial.suggest_int("global_right_padding",0,10)
    solution_type=trial.suggest_categorical("solution_type",["BStarTree","SequencePair"])
    perturb_per_step=trial.suggest_int("perturb_per_step",10,1000)
    cool_rate=trial.suggest_float("cool_rate",0,1)
    parts=trial.suggest_int("parts",10,100)
    ufactor=trial.suggest_int("ufactor",10,1000)
    new_macro_density=trial.suggest_float("new_macro_density",0,1)
    halo_x=trial.suggest_int("halo_x",0,1000000)
    halo_y=trial.suggest_int("halo_y",0,1000000)
    read_cts_data=trial.suggest_categorical("read_cts_data",["OFF"])
    write_cts_data=trial.suggest_categorical("write_cts_data",["ON"])
    router_type=trial.suggest_categorical("router_type",["SlewAware"])
    delay_type=trial.suggest_categorical("delay_type",["elmore"])
    skew_bound=trial.suggest_categorical("skew_bound",["0.08"])
    max_buf_tran=trial.suggest_categorical("max_buf_tran",["1"])
    max_sink_tran=trial.suggest_categorical("max_sink_tran",["1"])
    max_cap=trial.suggest_categorical("max_cap",["0.15183"])
    max_fanout2=trial.suggest_categorical("max_fanout2",["32"])
    max_length=trial.suggest_categorical("max_length",["30"])
    scale_size=trial.suggest_int("scale_size",50,50)
    cluster_type=trial.suggest_categorical("cluster_type",["kemans"])
    cluster_size=trial.suggest_int("cluster_size",32,32)
    buffer_type=trial.suggest_categorical("buffer_type",["sky130_fd_sc_hs__buf_1"])
    routing_layer_1=trial.suggest_int("routing_layer_1",4,4)
    routing_layer_2=trial.suggest_int("routing_layer_2",5,5)
    external_model=trial.suggest_categorical("external_model",["[]"])
    use_netlist=trial.suggest_categorical("use_netlist",["OFF"])
    clock_name=trial.suggest_categorical("clock_name",["core_clock"])
    net_name=trial.suggest_categorical("net_name",["clk"])


    area,latency=eda_tools(max_fanout,is_max_length_opt,max_length_constraint,is_timing_aware_mode,ignore_net_degree,num_threads,init_wirelength_coef,
                                 reference_hpwl,min_wirelength_force_bar,target_density,bin_cnt_x,bin_cnt_y,max_iter,max_backtrack,init_density_penalty,target_overflow,
    initial_prev_coordi_update_coef,min_precondition,min_phi_coef,max_phi_coef,max_buffer_num,max_displacement,global_right_padding,solution_type,perturb_per_step,cool_rate,
                                 parts,ufactor,new_macro_density,halo_x,halo_y,read_cts_data,write_cts_data,router_type,delay_type,skew_bound,max_buf_tran,max_sink_tran,max_cap,
                                 max_fanout2,max_length,scale_size,cluster_type,cluster_size,buffer_type,routing_layer_1,routing_layer_2,external_model,use_netlist,clock_name,net_name)
    return area,latency
study = optuna.create_study(directions=["minimize", "minimize"],study_name="1222",storage="sqlite:///data/data.db",load_if_exists=True)
def worker():
    init()
    study.optimize(objective, n_trials=2)
if __name__ == "__main__":
    num_processes = 1  # 设置要创建的进程数量
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=worker)
        processes.append(process)

    start_time = time.time()

    # 启动所有进程
    for process in processes:
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    end_time = time.time()
    time_cost = end_time - start_time #time_cost即为程序运行的时间，单位是秒
    print("第三次单进程串行实际运行时间为：%.2f秒" % time_cost)
    result_str = "第三次单进程串行运行时间为：%.2f秒" % time_cost
    with open('BaseDSEReport.txt', 'w') as file:
        file.write(result_str + '\n')

    time_cost2 = time_cost*100 #time_cost即为程序运行的时间，单位是秒
    print("第三次单进程串行预测运行时间为：%.2f秒" % time_cost2)
    result_str = "第三次单进程串行预测运行时间为：%.2f秒" % time_cost2
    with open('BaseDSEReport3.txt', 'a') as file:
        file.write(result_str + '\n')
    # with open("ChipPilotReport.txt", "r") as file:
    #     first_line = file.readline().strip()
    #     parallel_cost = float(first_line.split("：")[1].strip()[:-1])
    # speed_up = time_cost2 / parallel_cost
    # result_str = "加速比为：%.2f" % speed_up 
    # print(result_str)       
    # with open('BaseDSEReport.txt', 'a') as file2:
    #     file2.write(result_str + '\n')
