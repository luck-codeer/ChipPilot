#!/usr/bin/bash
set -e

export PROJ_PATH=$(cd "$(dirname "$0")"/..;pwd)


export SDC_FILE=$PROJ_PATH/aes/aes.sdc

export FOUNDRY_PATH=$PROJ_PATH/sky130
export RESULT_PATH=$PROJ_PATH/result
export SCRIPT_PATH=$PROJ_PATH/script
export BIN_PATH=$PROJ_PATH/bin
export PATH=$BIN_PATH/yosys/bin:$BIN_PATH:$PATH
export LD_LIBRARY_PATH=$BIN_PATH/lib:$LD_LIBRARY_PATH

# preprocess
test -e $FOUNDRY_PATH/lib/merged.lib || bash $FOUNDRY_PATH/mergelib.sh
test -e $RESULT_PATH/verilog || mkdir -p $RESULT_PATH/verilog

# # run yosys
# yosys $SCRIPT_PATH/yosys/yosys_ch_intrinsics.tcl

# # run iEDA
# bash $SCRIPT_PATH/iEDA/run_iEDA.sh
set -e

PWD="$(cd "$(dirname "$0")"/..;pwd)"
export CONFIG_DIR="${PWD}/script/iEDA/iEDA_config"
export TCL_SCRIPT_DIR="${PWD}/script/iEDA"

LOG_DIR="${RESULT_PATH}/log"
TCL_SCRIPTS="iNO_script/run_iNO_fix_fanout_aes.tcl
"

test -e $LOG_DIR || mkdir -p $LOG_DIR

for SCRIPT in $TCL_SCRIPTS; do
    echo " >>> \$iEDA -script ${TCL_SCRIPT_DIR}/${SCRIPT} <<< "
    $BIN_PATH/iEDA -script "${TCL_SCRIPT_DIR}/${SCRIPT}"
done