#!/bin/bash

echo "Compiling"

if [ ! -d yolox_pt ]; then
    mkdir yolox_pt
fi

ARCH=/workspace/arch/arch_ci560.json

vai_c_xir -o yolox_pt -n yolox_pt -x converted_qat_results/YOLOX_0_int.xmodel -a ${ARCH}