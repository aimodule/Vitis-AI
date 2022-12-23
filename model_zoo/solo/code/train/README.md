
# SOLO: Segmenting Objects by Locations

This project hosts the code for implementing the SOLO algorithms for instance segmentation.

> [**SOLO: Segmenting Objects by Locations**](https://arxiv.org/abs/1912.04488),            
> Xinlong Wang, Tao Kong, Chunhua Shen, Yuning Jiang, Lei Li    
> In: Proc. European Conference on Computer Vision (ECCV), 2020  
> *arXiv preprint ([arXiv 1912.04488](https://arxiv.org/abs/1912.04488))*   


> [**SOLOv2: Dynamic and Fast Instance Segmentation**](https://arxiv.org/abs/2003.10152),            
> Xinlong Wang, Rufeng Zhang, Tao Kong, Lei Li, Chunhua Shen     
> In: Proc. Advances in Neural Information Processing Systems (NeurIPS), 2020  
> *arXiv preprint ([arXiv 2003.10152](https://arxiv.org/abs/2003.10152))*  



## Installation
This implementation is based on [mmdetection](https://github.com/open-mmlab/mmdetection)(v1.0.0). Please refer to [INSTALL.md](docs/INSTALL.md) for installation and dataset preparation.

```shell
conda create -n solo python=3.7 -y
conda activate solo
pip install -r requirements.txt 
```

## Usage

### A quick demo

Once the installation is done, you can download the provided models and use [inference_demo.py](demo/inference_demo.py) to run a quick demo.

### Train with multiple GPUs, modified the data PATH to coco dataset in config.py and download the resnet50 pretrained model
    ./tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM}

    Example: 
    ./tools/dist_train.sh ../configs/decoupled_solo_light_r50_fpn_8gpu_3x.py 8

### Train with single GPU
    python tools/train.py ${CONFIG_FILE}
    
    Example:
    python tools/train.py ../configs/decoupled_solo_light_r50_fpn_8gpu_3x.py

### Visualization

    python tools/test_ins_vis.py ${CONFIG_FILE} ${CHECKPOINT_FILE} --show --save_dir  ${SAVE_DIR}
    
    Example: 
    python tools/test_ins_vis.py ../configs/decoupled_solo_light_r50_fpn_8gpu_3x.py  model.pth --show --save_dir  work_dirs/vis_solo

## License

For academic use, this project is licensed under the 2-clause BSD License - see the LICENSE file for details. For commercial use, please contact [Xinlong Wang](https://www.xloong.wang/) and  [Chunhua Shen](https://cs.adelaide.edu.au/~chhshen/).
