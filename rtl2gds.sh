#!/usr/bin/bash
set -e

export PROJ_PATH=$(cd "$(dirname "$0")";pwd)

export RTL_FILE=$PROJ_PATH/gcd/gcd.v
export SDC_FILE=$PROJ_PATH/gcd/gcd.sdc

export FOUNDRY_PATH=$PROJ_PATH/sky130
export RESULT_PATH=$PROJ_PATH/result
export SCRIPT_PATH=$PROJ_PATH/script
export BIN_PATH=$PROJ_PATH/bin
export PATH=$BIN_PATH/yosys/bin:$BIN_PATH:$PATH
export LD_LIBRARY_PATH=$BIN_PATH/lib:$LD_LIBRARY_PATH

# preprocess
test -e $FOUNDRY_PATH/lib/merged.lib || bash $FOUNDRY_PATH/mergelib.sh
test -e $RESULT_PATH/verilog || mkdir -p $RESULT_PATH/verilog

# run yosys
# yosys $SCRIPT_PATH/yosys/yosys_gcd.tcl

# run iEDA
bash $SCRIPT_PATH/iEDA/run_iEDA.sh
