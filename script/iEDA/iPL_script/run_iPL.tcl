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
def_init -path $::env(RESULT_PATH)/iTO_fix_fanout_result.def

#===========================================================
##   run Placer
#===========================================================
run_placer -config $::env(CONFIG_DIR)/pl_default_config.json

#===========================================================
##   save def 
#===========================================================
def_save -path $::env(RESULT_PATH)/iPL_result.def

#===========================================================
##   save netlist 
#===========================================================
netlist_save -path $::env(RESULT_PATH)/iPL_result.v -exclude_cell_names {}

#===========================================================
##   report 
#===========================================================
report_db -path "$::env(RESULT_PATH)/report/pl_db.rpt"

#===========================================================
##   Exit 
#===========================================================
flow_exit
