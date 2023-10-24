LIB_PATH="$FOUNDRY_PATH/lib"
TMP_LIB="$LIB_PATH/merged.lib.tmp"

$FOUNDRY_PATH/mergeLib.pl sky130_merged   \
 $LIB_PATH/sky130_fd_sc_hs__tt_025C_1v80.lib            \
 $LIB_PATH/sky130_dummy_io.lib                          \
 $LIB_PATH/sky130_sram_1rw1r_128x256_8_TT_1p8V_25C.lib  \
 $LIB_PATH/sky130_sram_1rw1r_44x64_8_TT_1p8V_25C.lib    \
 $LIB_PATH/sky130_sram_1rw1r_64x256_8_TT_1p8V_25C.lib   \
 $LIB_PATH/sky130_sram_1rw1r_80x64_8_TT_1p8V_25C.lib    \
 > $TMP_LIB

$FOUNDRY_PATH/removeDontUse.pl  $TMP_LIB \
 "sky130_fd_sc_hs__xor3_1 *2111* *221* *311* *32* *41* *clk* *dly* *nand4* *or4*" \
 > $LIB_PATH/merged.lib

rm $TMP_LIB

echo "======= lib merged ======"
