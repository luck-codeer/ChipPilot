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
##   read verilog
#===========================================================
verilog_init -path $::env(RESULT_PATH)/verilog/gcd.v -top gcd

#===========================================================
##   read def
#===========================================================
#def_init -path $PRE_RESULT_PATH/gcd.def

#===========================================================
##   init floorplan
##   gcd & uart
#===========================================================
set DIE_AREA "0.0    0.0   149.96   150.128"
set CORE_AREA "9.996 10.08 139.964  140.048"

#===========================================================
##   init floorplan
##   aes_cipher_top
#===========================================================
#set DIE_AREA "0.0    0.0   1100   1100"
#set CORE_AREA "10.0 10.0 1090.0  1090.0"

set PLACE_SITE unit 
set IO_SITE unit
set CORNER_SITE unit

init_floorplan \
   -die_area $DIE_AREA \
   -core_area $CORE_AREA \
   -core_site $PLACE_SITE \
   -io_site $IO_SITE \
   -corner_site $CORNER_SITE

source $::env(SCRIPT_PATH)/iEDA/iFP_script/module/create_tracks.tcl

#===========================================================
##   Place IO Port
#===========================================================
auto_place_pins -layer met5 -width 2000 -height 2000

#===========================================================
##   Tap Cell
#===========================================================
tapcell \
   -tapcell sky130_fd_sc_hs__tap_1 \
   -distance 14 \
   -endcap sky130_fd_sc_hs__fill_1

#===========================================================
##   PDN 
#===========================================================
source $::env(SCRIPT_PATH)/iEDA/iFP_script/module/pdn.tcl 

#===========================================================
##   set clock net
#===========================================================
source $::env(SCRIPT_PATH)/iEDA/iFP_script/module/set_clocknet.tcl

#===========================================================
##   save def 
#===========================================================
def_save -path $::env(RESULT_PATH)/iFP_result_gcd.def

#===========================================================
##   report db summary
#===========================================================
report_db -path "$::env(RESULT_PATH)/report/fp_db_gcd.rpt"

#===========================================================
##   Exit 
#===========================================================
flow_exit
