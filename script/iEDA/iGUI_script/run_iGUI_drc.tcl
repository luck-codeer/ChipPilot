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
def_init -path $::env(RESULT_PATH)/iRT_result.def

#===========================================================
##   run DRC
#===========================================================
#run_drc -config $::env(CONFIG_DIR)/drc_default_config.json -path $::env(RESULT_PATH)/report/drc/iRT_drc.rpt

#===========================================================
##   run gui drc
#===========================================================
gui_start

gui_show_drc -path $::env(RESULT_PATH)/drc/detail.drc -max_num ""

