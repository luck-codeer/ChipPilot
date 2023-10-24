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
#def_init -path $::env(RESULT_PATH)/iTO_fix_fanout_result.def

#===========================================================
##   run Placer
#===========================================================
#run_placer -config $::env(CONFIG_DIR)/pl_default_config.json

#===========================================================
##   run gui
#===========================================================
def_init -path $::env(RESULT_PATH)/iPL_result.def
gui_start -type global_place
gui_show_pl -dir $::env(RESULT_PATH)/pl/gui/


