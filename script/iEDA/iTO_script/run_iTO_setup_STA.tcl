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
def_init -path $::env(RESULT_PATH)/iTO_setup_result.def

#===========================================================
##   run STA and report
#===========================================================
run_sta -output $::env(RESULT_PATH)/to/setup/sta/

#===========================================================
##   Exit 
#===========================================================
flow_exit