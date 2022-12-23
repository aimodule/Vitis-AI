#!/bin/bash

# install pytorch version compatible to cuda 11.3 
pip install numpy==1.17.2 pandas==1.1.1 pywavelets==1.1.1 ninja sklearn
pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 -f https://download.pytorch.org/whl/torch_stable.html

# nndct bugfix 
# see: https://github.com/Xilinx/Vitis-AI/issues/998
cp deploy_optimizer.py /opt/vitis_ai/conda/envs/vitis-ai-pytorch/lib/python3.7/site-packages/nndct_shared/compile/deploy_optimizer.py