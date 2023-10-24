#===========================================================
##   init flow config
#===========================================================
flow_init -config $::env(CONFIG_DIR)/flow_config.json

#===========================================================
##   read db config
#===========================================================
db_init -config $::env(CONFIG_DIR)/db_default_config.json

#===========================================================
##   reset data path
#===========================================================
source $::env(SCRIPT_PATH)/iEDA/DB_script/db_path_setting.tcl

#===========================================================
##   reset lib
#===========================================================
source $::env(SCRIPT_PATH)/iEDA/DB_script/db_init_lib.tcl

#===========================================================
##   reset sdc
#===========================================================
source $::env(SCRIPT_PATH)/iEDA/DB_script/db_init_sdc.tcl

#===========================================================
##   read lef
#===========================================================
source $::env(SCRIPT_PATH)/iEDA/DB_script/db_init_lef.tcl

#===========================================================
##   read def
#===========================================================
def_init -path $::env(RESULT_PATH)/iPL_lg_result.def

set temp_folder_path $::env(RESULT_PATH)/rt/

init_drc
init_drc_api

init_rt -temp_directory_path $temp_folder_path \
        -log_level 0 \
        -thread_number 8 \
        -bottom_routing_layer "" \
        -top_routing_layer "" \
        -enable_output_gds_files 0 \
        -enable_idrc_interfaces 1 \
        -ra_initial_penalty 100 \
        -ra_penalty_drop_rate 0.8 \
        -ra_outer_max_iter_num 10 \
        -ra_inner_max_iter_num 10

run_rt -flow "dr"

destroy_rt

destroy_drc_api


#===========================================================
##   save def & netlist
#===========================================================
def_save -path $::env(RESULT_PATH)/iRT_result.def

#===========================================================
##   save netlist 
#===========================================================
netlist_save -path $::env(RESULT_PATH)/iRT_result.v -exclude_cell_names {}

#===========================================================
##   report db summary
#===========================================================
report_db -path "$::env(RESULT_PATH)/report/rt_db.rpt"

#===========================================================
##   Exit 
#===========================================================
flow_exit
