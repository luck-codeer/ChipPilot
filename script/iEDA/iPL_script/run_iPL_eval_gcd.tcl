#run_iPL_eval_gcd.tcl
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
##   read lef
#===========================================================
source $::env(SCRIPT_PATH)/iEDA/DB_script/db_init_lef.tcl

#===========================================================
##   read def
#===========================================================
def_init -path $::env(RESULT_PATH)/iPL_result_gcd.def

#===========================================================
##   report wire length and congestion
#===========================================================
report_wirelength -path  "$::env(RESULT_PATH)/report/eval/iPL_result_wirelength_gcd.rpt"
# puts "~~~~~~~~~~~~ report congestion"
# report_congestion -path "$::env(RESULT_PATH)/report/eval/iPL_result_congestion.rpt"

#===========================================================
##   Exit 
#===========================================================
flow_exit
