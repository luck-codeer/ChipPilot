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
def_init -path $::env(RESULT_PATH)/iCTS_result_uart.def

report_wirelength -path  "$::env(RESULT_PATH)/report/eval/iCTS_result_wirelength_uart.rpt"

#===========================================================
##   Exit 
#===========================================================
flow_exit