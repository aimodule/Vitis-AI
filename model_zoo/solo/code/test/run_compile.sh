#!/bin/bash

echo "Compiling"

if [ ! -d solo_pt ]; then
    mkdir solo_pt
fi

OPTIONS=`python get_compile_params.py`
ARCH=/workspace/arch/arch_ci550.json

vai_c_xir -o solo_pt -n solo_pt -x quantize_result/SOLO_0_int.xmodel -a ${ARCH} --options "${OPTIONS}"
