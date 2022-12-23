# FPGA Deployable SOLO Training on MSCOCO2017
### Contents
1. [Installation](#installation)
2. [Preparation](#preparation)
3. [Train/Test/Quant/Dump](#eval/test)
4. [Performance](#performance)
5. [Model_info](#model_info)

### Installation
1. Environment requirement
    - pytorch, opencv, more details seen in requirements.txt
    - vai_q_pytorch(Optional, required by quantization)
    - XIR Python frontend (Optional, required by quantization)

2. Installation with Docker

   - Please refer to [vitis-ai](https://github.com/Xilinx/Vitis-AI/tree/master/) for how to obtain the docker image.

   - Activate pytorch virtual envrionment in docker:
   ```shell
   conda activate vitis-ai-pytorch
   # the default gcc version is gcc-9, we should config to gcc-8 to make it compatible with cudatoolkit=11.3
   sudo update-alternatives --config gcc # choice 2
   ```
   - Install all the python dependencies using pip:
   ```shell
   pip install --user -r requirements.txt
   ```

### Preparation

1. Dataset description
   - download COCO2017 dataset.(refer to this repo https://github.com/ultralytics/yolov5)

2. Dataset diretory structure
   ```
   + data/coco
     + annotations
       + instance_train2017.json
       + instance_val2017.json
       + instance_val2017.json
     + images
       + images_2017
       + train_2017
       + val_2017
   ```
### Train/Test/Quant/Dump

1. Training. modfied the data_root path in config file 
    ```shell
    cd code/train/
    bash run_train.sh 
    ```

2. Test and Evaluation
    ```shell
    cd code/test/
    bash run_test.sh 
    ```

3. Quantization
    ```shell
    cd code/test
    bash run_quant.sh
    ```

4. Qaunt Testing and Dump xmodel
   ```shell
   cd code/test
   bash run_test_quant.sh 
   ```    

5. Compile for DPU
   ```shell
   cd code/test
   bash run_compile.sh 
   ```    

### Performance
Note the performance is evaluated on COCO2017 val.
- Float model

| model | input size | FLOPs | AP|
|-------|------------|--------------|-----------|
| Decouple-solo-modified| 640x640 | 107G| 24.2 |
- Quantize model

| model | input size | FLOPs | INT8 AP|
|-------|------------|--------------|-----------|
| Decouple-solo-modified| 640x640 | 107G | 21.2 |

### Model_info

1. Data preprocess
  ```
  data channel order: RGB(0~255)                  
  input size: h * w = 640 * 640
  mean = (123.675, 116.28, 103.53)
  std = (58.395, 57.12, 57.375)
  ```
